from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


class MutearAPIView(APIView):
    def post(self, request):
        # Obtén los parámetros necesarios del request
        agent_id = request.data.get('agent_id')
        api_action = 'mute'  # Cambié la acción a "mute" para silenciar al agente
        token = request.headers.get('wolkvox-token')

        # Verificar que los parámetros requeridos estén presentes
        if not agent_id or not token:
            return Response(
                {'error': 'El agent_id y el token son obligatorios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # URL de la API externa
        url = f"https://wv0042.wolkvox.com/api/v2/agentbox.php?agent_id={agent_id}&api={api_action}"

        headers = {
            "wolkvox-token": token,
        }

        try:
            # Realiza la solicitud a la API externa
            response = requests.post(url, headers=headers)

            # Verificar si la respuesta es exitosa
            if response.status_code == 200:
                # Intenta convertir la respuesta a JSON
                try:
                    response_data = response.json()
                    # Mensaje de éxito
                    return Response(
                        {'message': 'El agente fue muteado exitosamente.'},
                        status=status.HTTP_200_OK
                    )
                except ValueError:
                    return Response(
                        {'error': 'La respuesta de la API no es un JSON válido.'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )
            else:
                # Si la API devuelve un error
                return Response(
                    {'error': f'Error al mutear: {response.text}'},
                    status=response.status_code
                )
        except requests.exceptions.RequestException as e:
            # Manejo de errores en la solicitud a la API externa
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
