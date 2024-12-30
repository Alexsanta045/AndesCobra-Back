import requests
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WolkvoxTipificar(APIView):
    
    #proteccion del endpoint
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    API View para tipificar llamadas en Wolkvox.
    
    Esta vista permite tipificar la llamada del agente utilizando la API v2 de Wolkvox.
    Requiere autenticación mediante token en los headers.
    
    Límites de la API:
    - Tiempo máximo de respuesta: 60 segundos
    - Máximo 2 solicitudes simultáneas por token
    """
    
    TIMEOUT = 60  # Tiempo límite de la petición

    def validate_required_fields(self, data):
        """Valida que todos los campos requeridos estén presentes y no vacíos."""
        required_fields = {
            'agent_id': 'ID del agente',
            'cod_act': 'Código de actividad 1'
        }
        
        for field, description in required_fields.items():
            if not data.get(field):
                raise ValueError(f"{description} es requerido")

    def post(self, request):
        try:
            # Validar token
            token = request.headers.get('wolkvox-token')
            if not token:
                return Response(
                    {"error": "Token de autorización no proporcionado"}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Validar campos requeridos
            try:
                self.validate_required_fields(request.data)
            except ValueError as e:
                return Response(
                    {"error": str(e)}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Obtener datos
            agent_id = request.data.get('agent_id')
            cod_act = request.data.get('cod_act')
            cod_act2 = request.data.get('cod_act_2', '')  # Renombrado para coincidir con la documentación
            comments = request.data.get('comments', '')  # Opcional
            
            wolkvox_server = "wv0042"  # Debe configurarse según la operación

            # Headers según documentación
            headers = {
                "wolkvox-token": token,
                'Content-Type': 'application/json'
            }

            # Parámetros de la solicitud
            params = {
                "agent_id": agent_id,
                "api": "type",
                "cod_act": cod_act,
                "cod_act_2": cod_act2,
                "comments": comments
            }

            base_url = f"https://{wolkvox_server}.wolkvox.com/api/v2/agentbox.php"

            # Realizar la solicitud
            response = requests.post(
                base_url,
                params=params,
                headers=headers,
                timeout=self.TIMEOUT
            )
            
            response.raise_for_status()
            
            # Log de éxito
            logger.info(f"Tipificación exitosa para agent_id: {agent_id}")
            
            return Response(response.json(), status=response.status_code)
            
        except requests.exceptions.Timeout:
            logger.error(f"Timeout al tipificar para agent_id: {agent_id}")
            return Response(
                {"error": "Tiempo de espera agotado (60 segundos)"}, 
                status=status.HTTP_504_GATEWAY_TIMEOUT
            )
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al tipificar para agent_id {agent_id}: {str(e)}")
            return Response(
                {"error": "Error al realizar la solicitud externa"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Exception as e:
            logger.error(f"Error inesperado: {str(e)}")
            return Response(
                {"error": "Error interno del servidor"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )