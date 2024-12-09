
import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from ..models import Obligaciones
from .listaCamposCargarObligaciones import *
# from .crearCliente import crear_cliente_si_no_existe

def cargarObligaciones( id_campaña, archivo):
        
        if not archivo:
            return Response({'error': 'No se ha proporcionado un archivo'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            df = pd.read_excel(archivo)

            # Se obtiene la lista de campos requeridos para poder llenar cada modelo
            columnas_clientes_requeridas = campos_clientes_necesarios
            columnas_codeudores_requeridos = campos_codeudores_necesarios
            columnas_referencias_requeridos = campos_referencias_necesarios
            columnas_obligaciones_requeridos = campos_obligaciones_necesarios

            # Se valida si estan las columnas necesarias en el dataframe para llenar los modelos
            existen_columnas_cliente = all(col in df.columns for col in columnas_clientes_requeridas)
            existen_columnas_codeuores = all(col in df.columns for col in columnas_codeudores_requeridos)
            existen_columnas_referencias = all(col in df.columns for col in columnas_referencias_requeridos)
            existen_columnas_obligaciones = all(col in df.columns for col in columnas_obligaciones_requeridos)

            # return Response({'error': 'Faltan columnas requeridas en el archivo para cargar el cliente'}, status=status.HTTP_400_BAD_REQUEST)
            
            if('codigo_obligacion' in df.columns):
                for _, fila in df.iterrows():

                    #si si estan las columnas necesarias si crea el cliente si no existe en la base de datos
                    # if(existen_columnas_cliente == True):
                    #     crear_cliente_si_no_existe(fila, campos_clientes_opcionales)
                    # else:
                    #     return Response({'error': 'Faltan columnas requeridas en el archivo para cargar el cliente'}, status=status.HTTP_400_BAD_REQUEST)

                         
                         
    
                    obligacion = Obligaciones(
                        codigo_obligacion=fila['Codigo obligacion'],
                        campaña_id=fila['Codigo campaña'],
                        cliente_id=fila['Documento cliente'],
                        fecha_obligacion=fila['Fecha obligacion'],
                        fecha_vencimiento_cuota=fila['Fecha vencimiento'],
                        valor_capital=fila['Valor obligacion'],
                        valor_mora=fila['Valor mora']
                    )

        #             columnas_adicionales = {
        #                 col: fila[col]
        #                 for col in df.columns if col not in columnas_requeridas
        #             }
        #             obligacion.campos_opcionales = columnas_adicionales
        #             obligacion.save()
        #     else: # si no esta el codigo de la obligacion lo deja vacion
        #         for _, fila in df.iterrows():
    
        #             obligacion = Obligaciones(
        #                 codigo_obligacion= None,
        #                 campaña_id=fila['Codigo campaña'],
        #                 cliente_id=fila['Documento cliente'],
        #                 fecha_obligacion=fila['Fecha obligacion'],
        #                 fecha_vencimiento_cuota=fila['Fecha vencimiento'],
        #                 valor_capital=fila['Valor obligacion'],
        #                 valor_mora=fila['Valor mora']
        #             )

        #             columnas_adicionales = {
        #                 col: fila[col]
        #                 for col in df.columns if col not in columnas_requeridas
        #             }
        #             obligacion.campos_opcionales = columnas_adicionales
        #             obligacion.save()

        #     return Response({'mensaje': 'Obligaciones guardadas exitosamente'}, status=status.HTTP_201_CREATED)
        except Exception as e:
        #     # import traceback
        #     # error_trace = traceback.format_exc()
        #     # print(error_trace)  # Rastreo completo del error en logs
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)