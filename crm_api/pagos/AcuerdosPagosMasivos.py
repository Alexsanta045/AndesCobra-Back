from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import hashlib
from ..models import Acuerdo_pago, ArchivoProcesado

class AcuerdosPagosMasivos(APIView):
    def post(self, request, *args, **kwargs):
        try:
            archivo_acuerdos = request.FILES.get('acuerdos_pago')
            
            if not archivo_acuerdos:
                return Response({
                    'error': 'No se encontró el archivo de acuerdos de pago'
                }, status=status.HTTP_400_BAD_REQUEST)

            if not archivo_acuerdos.name.endswith(('.xls', '.xlsx')):
                return Response({
                    'error': 'El archivo debe ser un archivo Excel (.xls o .xlsx)'
                }, status=status.HTTP_400_BAD_REQUEST)

            # Calcular el hash único del archivo
            file_hash = hashlib.md5(archivo_acuerdos.read()).hexdigest()
            archivo_acuerdos.seek(0)  # Reiniciar el puntero del archivo

            # Verificar si el archivo ya fue procesado
            if ArchivoProcesado.objects.filter(hash=file_hash).exists():
                return Response({
                    'error': 'Este archivo ya fue subido y procesado anteriormente.'
                }, status=status.HTTP_400_BAD_REQUEST)

            # Leer el Excel con las columnas específicas
            try:
                df = pd.read_excel(
                    archivo_acuerdos,
                    names=[
                        'valor_cuota',
                        'fecha_pago',
                        'fecha_gestion',
                        'codigo_resultado_gestion',
                        'resultado_gestion',
                        'codigo_obligacion',
                        'codigo_asesor',
                        'descripcion'
                    ]
                )
            except Exception as e:
                return Response({
                    'error': f'Error al leer el archivo Excel: {str(e)}'
                }, status=status.HTTP_400_BAD_REQUEST)

            if df.empty:
                return Response({
                    'error': 'El archivo Excel está vacío'
                }, status=status.HTTP_400_BAD_REQUEST)

            # Iterar y guardar cada fila
            registros_guardados = 0
            for _, fila in df.iterrows():
                try:
                    acuerdo = Acuerdo_pago(
                        valor_cuota=fila['valor_cuota'],
                        fecha_pago=fila['fecha_pago'],
                        fecha_gestion=fila['fecha_gestion'],
                        codigo_resultado_gestion=fila['codigo_resultado_gestion'],
                        resultado_gestion=fila['resultado_gestion'],
                        codigo_obligacion=fila['codigo_obligacion'],
                        # Si no hay código de asesor, omitirlo o usar un valor por defecto
                        codigo_asesor=fila.get('codigo_asesor', None),
                        descripcion=fila['descripcion'] if pd.notna(fila['descripcion']) else 'sin descripcion'
                    )
                    acuerdo.save()
                    registros_guardados += 1
                except Exception as e:
                    return Response({
                        'error': f'Error al guardar la fila {registros_guardados + 1}: {str(e)}'
                    }, status=status.HTTP_400_BAD_REQUEST)

            # Guardar el hash del archivo como procesado
            ArchivoProcesado.objects.create(hash=file_hash)

            return Response({
                'mensaje': f'Datos guardados exitosamente. Se guardaron {registros_guardados} registros.'
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(f"Error: {str(e)}")
            return Response({
                'error': f"Error procesando el archivo: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
