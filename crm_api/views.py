
from rest_framework import status
import requests
from crm_api.serializers.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import *
from .models import *
from .serializers import *
from .serializers.clienteObligacionesSerializer import ClienteObligacionesSerializer
from .serializers.historialGestiones import HistorialGestionesSerializer


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
    

class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CampañasViewSet(viewsets.ModelViewSet):
    queryset = Campañas.objects.all()
    serializer_class = CampañasSerializer
    
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CampañasFilter
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class CampañaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = CampañasUsuarios.objects.all()
    serializer_class = CampañasUsuariosSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CampañaUsuarioFilter


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ClientesFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class CodeudoresViewSet(viewsets.ModelViewSet):
    queryset = Codeudores.objects.all()
    serializer_class = CodeudoresSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CodeudoresFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ReferenciasViewSet(viewsets.ModelViewSet):
    queryset = Referencias.objects.all()
    serializer_class = ReferenciasSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ReferenciasFilter


class ObligacionesViewSet(viewsets.ModelViewSet):
    queryset = Obligaciones.objects.all()
    serializer_class = ObligacionesSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ObligacionesFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PagosFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ResultadosGestionViewSet(viewsets.ModelViewSet):
    queryset = ResultadosGestion.objects.all()
    serializer_class = ResultadosGestionSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ResultadosGestionFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class GestionesViewSet(viewsets.ModelViewSet):
    queryset = Gestiones.objects.all()
    serializer_class = GestionesSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = GestionesFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class HistorialGestionesViewSet(viewsets.ModelViewSet):
    queryset = Gestiones.objects.all().order_by('-fecha')
    serializer_class = HistorialGestionesSerializer
    
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = GestionesFilter
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Tipo_identificacionViewSet(viewsets.ModelViewSet):
    queryset = Tipo_identificacion.objects.all()
    serializer_class = Tipo_identificacionSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

class Telefono_clienteViewSet(viewsets.ModelViewSet):
    queryset = Telefono_cliente.objects.all()
    serializer_class = Telefono_clienteSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Telefono_codeudorViewSet(viewsets.ModelViewSet):
    queryset = Telefono_codeudor.objects.all()
    serializer_class = Telefono_codeudorSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Direccion_clienteViewSet(viewsets.ModelViewSet):
    queryset = Direccion_cliente.objects.all()
    serializer_class = Direccion_clienteSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Direccion_codeudorViewSet(viewsets.ModelViewSet):
    queryset = Direccion_codeudor.objects.all()
    serializer_class = Direccion_codeudorSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class CanalesViewSet(viewsets.ModelViewSet):
    queryset = Canales.objects.all()
    serializer_class = CanalesSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Acuerdo_pagoViewSet(viewsets.ModelViewSet):
    queryset = Acuerdo_pago.objects.all()
    serializer_class = Acuerdo_pagoSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = AcuerdoPagoFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-estado')  # Primero los activos
    serializer_class = UserSerializer


class ClienteObligacionesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteObligacionesSerializer

class TipoGestionViewSet(viewsets.ModelViewSet):
    queryset = Tipo_gestion.objects.all()
    serializer_class = TipoGestionSerializer
  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
