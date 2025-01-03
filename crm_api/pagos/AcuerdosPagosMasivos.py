from rest_framework.views import APIView
import pandas as pd 
from rest_framework.response import Response
from rest_framework import status

class AcuerdosPagosMasivos(APIView):
    def post(self, request, *args, **kwargs):
        try:
            archivo_acuerdos = request.FILES.get('acuerdos_pago')
            if archivo_acuerdos:
                df = pd.read_excel(archivo_acuerdos)

                # print (df)

                for _, fila in df.iterrows():
                    print('---------------------------------------------------------------------')
                    print(f'fila--> {fila}')
                    print('---------------------------------------------------------------------')

                return Response({'mensaje': 'Acuerdos de pago recibidos exitosamente'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            import traceback
            error_trace = traceback.format_exc()
            print(error_trace)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)