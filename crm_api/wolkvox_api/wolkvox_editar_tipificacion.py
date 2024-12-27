import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class WolkvoxEditarTipificacion(APIView):
    def post(self, request):
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
            return Response({"error": "Token no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
        
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
        
        wolkvox_server = "wv0042"
        url = f"https://{wolkvox_server}.wolkvox.com/api/v2/configuration.php?api=edit_cod_act"
        
        #Realizar la solicitud PUT
        response = requests.put(url, json=payload, headers=headers)
        
        # Manejar la respuesta de la API
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=response.status_code)