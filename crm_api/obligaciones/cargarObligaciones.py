import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from .ingresarDatos import ingresar_datos
from .validarCampos import validar_fila
import os



def cargarObligaciones(id_campaña, archivo):
    if not archivo:
        return Response({'error': 'No se ha proporcionado un archivo'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:    
        df = pd.read_excel(archivo)

        print(f'dataframe original ----> {df}')

        columnas_obligatorias = ['nit', 'valor_vencido', 'nombre', 'telefono_1']

        # Validar que las filas tengan los campos obligatorios
        filas_incompletas = df[columnas_obligatorias].isna().any(axis=1)

        # Crear un DataFrame con las filas que vienen incompletas
        df_filas_eliminadas = df[filas_incompletas].copy()
        df_filas_eliminadas["motivo"] = "Campos obligatorios incompletos"
        print(f'dataframe filas eliminadas ---> {df_filas_eliminadas}')
        
        df = df[~filas_incompletas]

        print(f'dataframe limpio -->  {df}')

        filas_invalidas = []
        motivos_invalidos = []
        for index, fila in df.iterrows():
            motivos = validar_fila(fila)
            if motivos:
                filas_invalidas.append(index)
                motivos_invalidos.append(", ".join(motivos))

        print(f'filas inválidas ---> {filas_invalidas}')

        # Agregar las filas inválidas a df_filas_eliminadas con motivos
        df_invalidas = df.loc[filas_invalidas].copy()
        df_invalidas["motivo"] = motivos_invalidos
        df_filas_eliminadas = pd.concat([df_filas_eliminadas, df_invalidas])

        # Guardar las filas eliminadas en un archivo
        ruta_descargas = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        nombre_archivo = 'obligaciones_no_subidas.xlsx'
        ruta_completa = os.path.join(ruta_descargas, nombre_archivo)
        df_filas_eliminadas.to_excel(ruta_completa, index=False)

        # Eliminar las filas inválidas del DataFrame original
        df = df.drop(filas_invalidas)

        # Ingresar los datos
        df['fecha_vencimiento'] = df['fecha_vencimiento'].apply(lambda x: x.date() if not pd.isnull(x) else None)
        ingresar_datos(df, id_campaña)

        return Response({'mensaje': 'Obligaciones guardadas exitosamente'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(error_trace)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




















        
