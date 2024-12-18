from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class DialWolkvoxAPIView(APIView):
    def post(self, request):
        # Recuperar datos enviados desde el cliente
        agent_id = request.data.get('agent_id')
        customer_phone = request.data.get('customer_phone')
        customer_id = request.data.get('customer_id', '')  # Opcional
        customer_name = request.data.get('customer_name', '')  # Opcional
        token = request.headers.get('wolkvox-token')

        # Validar los datos requeridos
        if not agent_id or not customer_phone or not token:
            print("Faltan datos requeridos: agent_id, customer_phone o token")
            return Response({"error": "Datos requeridos no proporcionados"}, status=status.HTTP_400_BAD_REQUEST)

        # Construir la URL de la API externa
        wolkvox_server = "wv0042"  # Cambiar por tu servidor específico si es diferente
        url = f"https://{wolkvox_server}.wolkvox.com/api/v2/agentbox.php"
        params = {
            "agent_id": agent_id,
            "api": "dial",
            "customer_phone": f'9{customer_phone}',
            "customer_id": customer_id,
            "customer_name": customer_name,
        }

        # Configurar encabezados
        headers = {
            "wolkvox-token": token,
        }

        try:
            # Consumir la API de Wolkvox
            response = requests.post(url, params=params, headers=headers)
            response.raise_for_status()  # Lanza un error si el código no es 2xx

            # Devolver respuesta al cliente
            return Response(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            # Capturar y registrar errores
            print(f"Error al consumir la API de Wolkvox: {e}")
            return Response({"error": "Error al realizar la solicitud externa"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

