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
    