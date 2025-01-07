import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from .ingresarDatos import ingresar_datos
from .validarCampos import validar_fila
import os

def cargarObligaciones(id_campaña, archivo):
    # Verificar si no se proporcionó un archivo
    if not archivo:
        return Response({'error': 'No se ha proporcionado un archivo'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Leer el archivo Excel
        df = pd.read_excel(archivo)

        # Imprimir el DataFrame original para depuración
        print(f'dataframe original ----> {df}')

        # Definir las columnas obligatorias que deben estar presentes en cada fila
        columnas_obligatorias = ['nit', 'valor_vencido', 'nombre', 'telefono_1']

        # Validar que las filas no tengan valores faltantes en las columnas obligatorias
        filas_incompletas = df[columnas_obligatorias].isna().any(axis=1)

        # Crear un DataFrame con las filas que tienen campos faltantes
        df_filas_eliminadas = df[filas_incompletas].copy()
        df_filas_eliminadas["motivo"] = "Campos obligatorios incompletos"
        print(f'dataframe filas eliminadas ---> {df_filas_eliminadas}')
        
        # Eliminar las filas con campos obligatorios incompletos del DataFrame original
        df = df[~filas_incompletas]

        # Imprimir el DataFrame limpio (sin filas incompletas)
        print(f'dataframe limpio -->  {df}')

        # Lista para almacenar las filas inválidas y sus motivos
        filas_invalidas = []
        motivos_invalidos = []

        # Validar cada fila utilizando la función validar_fila
        for index, fila in df.iterrows():
            motivos = validar_fila(fila)  # Validar la fila
            if motivos:
                filas_invalidas.append(index)  # Agregar el índice de la fila inválida
                motivos_invalidos.append(", ".join(motivos))  # Unir los motivos de invalidación

        # Imprimir las filas inválidas para depuración
        print(f'filas inválidas ---> {filas_invalidas}')

        # Agregar las filas inválidas al DataFrame de filas eliminadas con los motivos
        df_invalidas = df.loc[filas_invalidas].copy()
        df_invalidas["motivo"] = motivos_invalidos
        df_filas_eliminadas = pd.concat([df_filas_eliminadas, df_invalidas])

        # Guardar las filas eliminadas en un archivo Excel en la carpeta de descargas
        ruta_descargas = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        nombre_archivo = 'obligaciones_no_subidas.xlsx'
        ruta_completa = os.path.join(ruta_descargas, nombre_archivo)
        df_filas_eliminadas.to_excel(ruta_completa, index=False)

        # Eliminar las filas inválidas del DataFrame original
        df = df.drop(filas_invalidas)

        # Ingresar los datos
        df['fecha_vencimiento'] = df['fecha_vencimiento'].apply(lambda x: x.date() if not pd.isnull(x) else None)
        ingresar_datos(df, id_campaña)

        # Retornar respuesta indicando que los datos fueron guardados exitosamente
        return Response({'mensaje': 'Obligaciones guardadas exitosamente'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        # Capturar cualquier excepción y devolver el mensaje de error
        import traceback
        error_trace = traceback.format_exc()
        print(error_trace)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
