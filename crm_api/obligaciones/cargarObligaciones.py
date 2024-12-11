
import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from .ingresarDatos import ingresar_datos

def validar_fila(fila):
    # Validar columna 'nit' (debe ser entero o cadena numérica)
    if not isinstance(fila['nit'], (int, str)) or not str(fila['nit']).isdigit():
        return False
    
    # Validar columna 'valor_vencido' (debe ser número positivo)
    if not isinstance(fila['valor_vencido'], (int, float)) or fila['valor_vencido'] < 0:
        return False
    
    # Validar columna 'nombre' (debe ser cadena no vacía)
    if not isinstance(fila['nombre'], str):
        return False
    
    # # Validar columna 'telefono' (debe ser cadena numérica de 10 dígitos)
    # if not isinstance(fila['telefono'], str) or not fila['telefono'].isdigit() or len(fila['telefono']) != 10:
    #     return False
    
    return True


def cargarObligaciones( id_campaña, archivo):
     
    if not archivo:
        return Response({'error': 'No se ha proporcionado un archivo'},
                    status=status.HTTP_400_BAD_REQUEST)
    try:    
        df = pd.read_excel(archivo)

        print(f'dataframe original ----> {df}')

        columnas_obligatorias = ['nit', 'valor_vencido', 'nombre', 'telefono']
        

        #Se valida que las filas tengan los campos obligatorios
        filas_incompletas = df[columnas_obligatorias].isna().any(axis=1)
        print(f'filas incompletas----> {filas_incompletas}')

        #se crea un df con las filas que vienen incompletas
        df_filas_eliminadas = df[filas_incompletas]
        print(f'dataframe filas eliminadas ---> {df_filas_eliminadas}')
        
        df = df[~filas_incompletas]

        print(f'dataframe limpió -->  {df}')


        filas_invalidas = []
        for index, fila in df.iterrows():
            if not validar_fila(fila):
                filas_invalidas.append(index)

        print(f'filas invaidas ---> {filas_invalidas}')
        # Agregar las filas inválidas a df_filas_eliminadas
        df_filas_eliminadas = pd.concat([df_filas_eliminadas, df.loc[filas_invalidas]])

        # Eliminar las filas inválidas del df original
        df = df.drop(filas_invalidas)
        
        
        #ingresar los datos
        ingresar_datos(df, id_campaña)

        return Response({'mensaje': 'Obligaciones guardadas exitosamente'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        #     # import traceback
        #     # error_trace = traceback.format_exc()
        #     # print(error_trace)  # Rastreo completo del error en logs
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


















        
