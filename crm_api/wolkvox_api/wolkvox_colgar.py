from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class ColgarAPIView(APIView):
    def post(self, request):
        # Obtén los parámetros necesarios del request si aplica
        agent_id = request.data.get('agent_id')
        api_action = request.data.get('api')
        token = request.headers.get('wolkvox-token')

        # URL de la API externa
        url = f"https://wv0042.wolkvox.com/api/v2/agentbox.php?agent_id={agent_id}&api={api_action}"

        headers = {
            "wolkvox-token": token,
        }

        try:
            # Realiza la solicitud a la API externa
            response = requests.post(url, headers=headers)

            # Intenta convertir la respuesta a JSON
            try:
                response_data = response.json()
            except ValueError as e:

                return Response({'error': 'La respuesta de la API no es un JSON válido.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Retorna la respuesta de la API externa al cliente
            return Response(response_data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            # Manejo de errores

            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
