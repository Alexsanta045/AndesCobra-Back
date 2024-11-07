from rest_framework import status
from rest_framework.views import APIView
from ..models import Obligaciones, Pagos
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

class EjecutarPagos(APIView):

    def post(self, request, *args, **kwargs):        
        # Validación de datos de entrada
        codigo_obligacion = request.data.get('codigo_obligacion')
        valor_pagado = request.data.get('valor_pagado')
        fecha_pago = request.data.get('fecha_pago')
        
        valor = valor_pagado

        if not codigo_obligacion or not valor_pagado or not fecha_pago:
            return Response(
                {'error': 'Faltan campos requeridos: codigo_obligacion, valor_pagado, o fecha_pago'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            valor_pagado = float(valor_pagado)
            if valor_pagado <= 0:
                return Response(
                    {'error': 'El valor pagado debe ser un número positivo'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except ValueError:
            return Response(
                {'error': 'El valor pagado debe ser un número válido'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        # Consultar la información de la obligación
        try:
            obligacion = Obligaciones.objects.get(codigo=codigo_obligacion)
        except ObjectDoesNotExist:
            return Response(
                {'error': 'La obligación con el código proporcionado no existe'},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        # Aplicar el pago a valor_mora y ajustar el saldo restante en valor_pagado
        # Restar del valor de mora y ajustar el valor pagado restante
        if obligacion.valor_mora > 0:
            if valor_pagado >= obligacion.valor_mora:
                valor_pagado -= obligacion.valor_mora
                obligacion.valor_mora = 0
            else:
                obligacion.valor_mora -= valor_pagado
                valor_pagado = 0

        
        # Verificar si queda algún saldo para aplicar al capital
        if valor_pagado <= 0:
            obligacion.save()
            return Response(
                {'message': 'Pago aplicado a mora, saldo actual en capital: 0'},
                status=status.HTTP_200_OK,
            )
        
        # Aplicar el pago al valor_capital si hay saldo restante
        try:
            obligacion.valor_capital -= valor_pagado
            obligacion.save()
            
            # Crear un registro de pago en la tabla de pagos
            Pagos.objects.create(
                obligacion=obligacion,
                valor=valor,
                fecha=fecha_pago,
            )
            
            return Response(
                {
                    'message': 'Pago registrado exitosamente',
                    'codigo_obligacion': obligacion.codigo,
                    'valor_pagado': valor,
                    'fecha_pago': fecha_pago,
                    'saldo_actual_capital': obligacion.valor_capital,
                    'saldo_actual_mora': obligacion.valor_mora,
                },
                status=status.HTTP_200_OK,
            )
        
        # Si el saldo restante es mayor al valor_capital, notificar que el pago excede el saldo
        except :
            Response(
            {
                'error': 'Error al efectuar el pago',
                'saldo_pendiente': obligacion.valor_capital,
                'saldo_mora': obligacion.valor_mora
                
            },
            status=status.HTTP_400_BAD_REQUEST,
            )
