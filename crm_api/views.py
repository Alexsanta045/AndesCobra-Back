from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class RolesViewSet(viewsets.ModelViewSet):
    
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    
class CampañasViewSet(viewsets.ModelViewSet):
    queryset = Campañas.objects.all()
    serializer_class = CampañasSerializer
    
class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
class CodeudoresViewSet(viewsets.ModelViewSet):
    queryset = Codeudores.objects.all()
    serializer_class = CodeudoresSerializer
    
class ReferenciasViewSet(viewsets.ModelViewSet):
    queryset = Referencias.objects.all()
    serializer_class = ReferenciasSerializer
    
class ObligacionesViewSet(viewsets.ModelViewSet):
    queryset = Obligaciones.objects.all()
    serializer_class = ObligacionesSerializer
    
class PagosViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer

class ResultadosGestionViewSet(viewsets.ModelViewSet):
    queryset = ResultadosGestion.objects.all()
    serializer_class = ResultadosGestionSerializer
    
class GestionesViewSet(viewsets.ModelViewSet):
    queryset = Gestiones.objects.all()
    serializer_class = GestionesSerializer
    
    
class CampañaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = CampañasUsuarios.objects.all()
    serializer_class = CampañasUsuariosSerializer    

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    
class Tipo_identificacionViewSet(viewsets.ModelViewSet):
    queryset = Tipo_identificacion.objects.all()
    serializer_class = Tipo_identificacionSerializer
    
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    
    
class Telefono_clienteViewSet(viewsets.ModelViewSet):
    queryset = Telefono_cliente.objects.all()
    serializer_class = Telefono_clienteSerializer
    
class Telefono_codeudorViewSet(viewsets.ModelViewSet):
    queryset = Telefono_codeudor.objects.all()
    serializer_class = Telefono_codeudorSerializer
    
class Direccion_clienteViewSet(viewsets.ModelViewSet):
    queryset = Direccion_cliente.objects.all()
    serializer_class = Direccion_clienteSerializer
    
class Direccion_codeudorViewSet(viewsets.ModelViewSet):
    queryset = Direccion_codeudor.objects.all()
    serializer_class = Direccion_codeudorSerializer
    
class CanalesViewSet(viewsets.ModelViewSet):
    queryset = Canales.objects.all()
    serializer_class = CanalesSerializer
    
class Acuerdo_pagoViewSet(viewsets.ModelViewSet):
    queryset = Acuerdo_pago.objects.all()
    serializer_class = Acuerdo_pagoSerializer
    