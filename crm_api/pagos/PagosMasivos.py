from rest_framework.views import APIView
from ..models import Pagos, Obligaciones, Clientes
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
        
        # se recorren todos los datos del dataframe para registrar los pagos
        for index, row in df.iterrows():
            valor_pagado = row['Valor Pagado']
            fecha_pago = row['Fecha Pago']
            valor = valor_pagado
            
            try:
                obligacion = Obligaciones.objects.get(codigo_obligacion=row['Codigo'])

                 #se aplica el pago primero en la mora
                if obligacion.valor_vencido > 0:
                    if valor_pagado >= obligacion.valor_vencido:
                        valor_pagado -= obligacion.valor_vencido
                        obligacion.valor_vencido = 0
                    else: 
                        obligacion.valor_vencido -= valor_pagado
                        valor_pagado = 0
                        
                if valor_pagado <= 0:
                    obligacion.save()

                try:
                    
                    # obligacion.valor_capital -= valor_pagado
                    # obligacion.save()
                    
                    pago = Pagos(
                        obligacion=obligacion,
                        valor=valor,
                        fecha=fecha_pago,
                    )
                    # inserta los pagos al arreglo
                    nuevos_pagos.append(pago)
                except Exception as e:
                    print(f"Error al guardar el pago: {e}")
                
            # si el codigo no coincide con ninguna obligacion se busca por numero de documento
            except Obligaciones.DoesNotExist:
                cliente = Clientes.objects.get(nit=row['Codigo'])
                if cliente:
                    while valor_pagado > 0:
                        # se obtienen todas las obligaciones del cliente con valor_vencido superior a $0
                        obligaciones = Obligaciones.objects.filter(cliente_id=cliente).exclude(valor_vencido=0)
                        obligacion_menor = obligaciones[0].valor_vencido
                        # si el cliente tiene dos o mas obligaciones
                        for obligacion in obligaciones:
                            if obligacion.valor_vencido <= obligacion_menor:
                                obligacion_menor = obligacion.valor_vencido
                                
                        obligacion = obligaciones.get(cliente_id=cliente, valor_vencido=obligacion_menor)
    
                        #se aplica el pago primero en la mora
                        if obligacion.valor_vencido > 0:
                            if valor_pagado >= obligacion.valor_vencido:
                                valor_pagado -= obligacion.valor_vencido
                                obligacion.valor_vencido = 0
                            else: 
                                obligacion.valor_vencido -= valor_pagado
                                valor_pagado = 0
                                
                        if valor_pagado <= 0:
                            obligacion.save()

                        try:
                            # obligacion.valor_capital -= valor_pagado
                            # obligacion.save()
                            
                            pago = Pagos(
                                obligacion=obligacion,
                                valor=valor,
                                fecha=fecha_pago,
                            )
                            # inserta los pagos al arreglo
                            nuevos_pagos.append(pago)
                        except :
                            print(f"error al efectuar el pago a la obligacion: {obligacion} ")                        
                        
                else:
                    obligacion = None
                    
            if not obligacion:
                raise ObjectDoesNotExist
      
        # insertar en bloque todos los pagos del archivo
        Pagos.objects.bulk_create(nuevos_pagos)
        return Response(status=status.HTTP_201_CREATED)
