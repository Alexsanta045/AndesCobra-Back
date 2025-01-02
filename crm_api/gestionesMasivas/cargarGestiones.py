import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from .ingresarGestiones import ingresar_gestiones
from .validarCampos import validar_fila
import os



def cargarGestiones(id_campaña, archivo):
    if not archivo:
        return Response({'error': 'No se ha proporcionado un archivo'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:    
        df = pd.read_excel(archivo)

        print(f'dataframe original ----> {df}')

        columnas_obligatorias =  [ 'nit_cliente', 'nombres_cliente','telefono_cliente', 'codigo_resultado_gestion', 'comentarios_gestion' ]
        filas_incompletas = df[columnas_obligatorias].isna().any(axis=1)
        df_filas_eliminadas = df[filas_incompletas].copy()
        df_filas_eliminadas['motivo'] = 'campos obligatorios incompletos'
        print('---------------------------------------------------------------------------------------')
        print(f'Dataframe de filas eliminadas --> {df_filas_eliminadas}')

        df = df[~filas_incompletas]


        print('---------------------------------------------------------------------------------------')
        print(f'Dataframe sin las filas incompletas --> {df}')

        filas_invalidas = []
        motivos_invalidos = []
        for index, fila  in df.iterrows():
            motivos = validar_fila(fila)
            if motivos:
                filas_invalidas.append(index)
                motivos_invalidos.append(','.join(motivos))
        
        print('---------------------------------------------------------------------------------------')
        print(f'filas invalidas --> {filas_invalidas}')
        
        # Agregar las filas inválidas a df_filas_eliminadas con motivos
        df_invalidas = df.loc[filas_invalidas].copy()
        df_invalidas['motivos'] = motivos_invalidos

        df_filas_eliminadas = pd.concat([df_filas_eliminadas, df_invalidas])

        ruta_descarga = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        nombre_archivo = 'gestiones_no_subidas.xlsx'
        ruta_completa = os.path.join(ruta_descarga, nombre_archivo)
        df_filas_eliminadas.to_excel(ruta_completa, index=False)

        # Eliminar las filas invalodas del dataframe original
        df = df.drop(filas_invalidas)
        print('---------------------------------------------------------------------------------------')

        print(f'Dataframe limpió:  {df}')

        # Ingresar las gestiones
        ingresar_gestiones(id_campaña, df)

        return Response({'mensaje': 'Obligaciones guardadas exitosamente'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(error_trace)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   




















        