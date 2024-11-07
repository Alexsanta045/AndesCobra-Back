from rest_framework.views import APIView
from ..models import Pagos, Obligaciones
import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

class PagosMasivos(APIView):
    def post(self, request, *args, **kwargs):
        try: 
            archivo_pagos = request.FILES.get('pagos')
            
            if archivo_pagos:
                df = pd.read_excel(archivo_pagos)
                
                # Llama a la función para procesar los pagos
                self.llenarPagos(df)
                
                return Response({"mensaje": "Pagos procesados correctamente"}, status=status.HTTP_200_OK)
            else: 
                return Response({"error": "No se ha subido un archivo"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(f"Error procesando el archivo: {e}")
            return Response({"error": "Error procesando el archivo"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def llenarPagos(self, df):
        nuevos_pagos = []
        
        for index, row in df.iterrows():
            try:
                obligacion = Obligaciones.objects.get(codigo=row['Obligacion'])
                valor_pagado = row['Valor Pagado']
                fecha_pago = row['Fecha Pago']
                
                valor = valor_pagado
                             
                #se aplica el pago primero en la mora
                if obligacion.valor_mora > 0:
                    if valor_pagado >= obligacion.valor_mora:
                        valor_pagado -= obligacion.valor_mora
                        obligacion.valor_mora = 0
                    else: 
                        obligacion.valor_mora -= valor_pagado
                        valor_pagado = 0
                        
                if valor_pagado <= 0:
                    obligacion.save()
                    return Response(
                        {'message': 'Pago aplicado a mora, saldo actual en capital: 0'},
                        status=status.HTTP_200_OK,
                    )
                    
                try:
                    obligacion.valor_capital -= valor_pagado
                    obligacion.save()
                    
                    pago = Pagos(
                        obligacion=obligacion,
                        valor=valor,
                        fecha=fecha_pago,
                    )
                    # inserta los pagos al arreglo
                    nuevos_pagos.append(pago)
                except :
                    Response(
                    {
                        'error': 'Error al efectuar el pago',
                        'saldo_pendiente': obligacion.valor_capital,
                        'saldo_mora': obligacion.valor_mora
                        
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                    )
                        
            except ObjectDoesNotExist:
                print(f"Obligación no encontrada para el número: {row['Obligacion']}")
        
        # insertar en bloque todos los pagos del archivo
        Pagos.objects.bulk_create(nuevos_pagos)
        
        return Response(status=status.HTTP_201_CREATED)
