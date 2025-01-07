from rest_framework.response import Response
from rest_framework import status
from ..models import Acuerdo_pago
from django.db.models import Sum
from django.db.models import Count

def estadisticasAcuerdosPago(campaña):
    if not campaña:  
        return Response(
            {'Error': 'El parámetro campaña es obligatorio'},
            status=status.HTTP_400_BAD_REQUEST
        )
        
    try:
        acuerdos = Acuerdo_pago.objects.filter(
            codigo_obligacion__campaña__id=campaña
        )

        # Agregar anotaciones para contar y sumar `valor_cuota`
        resultados = acuerdos.values('estado').annotate(
            total=Count('id'),
            suma_valor_cuota=Sum('valor_cuota')
        )

        # Construir los datos de respuesta
        data = {
            estado['estado']: {
                'Cantidad': estado['total'],
                'valor_total': estado['suma_valor_cuota'] or 0
            } for estado in resultados
        }

        # Calcular los totales generales
        total_acuerdos = sum(estado['total'] for estado in resultados)
        suma_total_cuotas = sum(estado['suma_valor_cuota'] or 0 for estado in resultados)

        # Agregar los totales generales bajo la clave `Creados`
        data['Creados'] = {
            'Cantidad': total_acuerdos,
            'valor_total': suma_total_cuotas
        }

        return Response(data)
    except Exception as e:
        return Response(
            {'error': f'Error al obtener la cantidad de acuerdos de pago: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )