from crm_api.serializers.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from .filters import *
from .models import *
from .models import CampañasUsuarios
from .serializers import *
from .serializers.clienteGestionSerializer import ClienteObligacionesSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CampañasViewSet(viewsets.ModelViewSet):
    queryset = Campañas.objects.all()
    serializer_class = CampañasSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CampañasFilter

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
