import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class WolkvoxCrearTipificacion(APIView):

    def post(self, request):
        # Obtener los datos del cuerpo de la solicitud
        type_code = request.data.get('type_code')
        cod_act = request.data.get('cod_act')
        description_cod_act = request.data.get('description_cod_act')
        hit = request.data.get('hit')
        rpc = request.data.get('rpc')
        chat = request.data.get('chat')
        studio = request.data.get('studio')
        voice = request.data.get('voice')
        interactions = request.data.get('interactions')
        token = request.headers.get('wolkvox-token')
        
        # Verificar si el token está presente
        if not token:
            print("No se encontró token")
            return Response({"error": "Token no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Preparar los datos para enviar a Wolkvox como JSON
        payload = {
            "type_code": type_code,
            "cod_act": cod_act,
            "description_cod_act": description_cod_act,
            "hit": hit,
            "rpc": rpc,
            "chat": chat,
            "studio": studio,
            "voice": voice,
            "interactions": interactions
        }
        
        # Encabezados necesarios para la solicitud
        headers = {
            'wolkvox-token': token,
            'Content-Type': 'application/json'
        }
        
        # URL de la API de Wolkvox
        wolkvox_server = "wv0042"  # Asegúrate de que este sea el servidor correcto
        url = f"https://{wolkvox_server}.wolkvox.com/api/v2/configuration.php?api=create_cod_act"
        
        try:
            # Enviar la solicitud POST con JSON
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            
            # Si la respuesta es correcta, devolverla al cliente
            response.raise_for_status()  # Lanza una excepción si hay un error HTTP
            return Response(response.json(), status=response.status_code)
        
        except requests.exceptions.RequestException as e:
            # Capturar cualquier excepción y devolver un error
            print(f"Error al consumir la API de Wolkvox: {e}")
            return Response({"error": "Error al realizar la solicitud externa"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
