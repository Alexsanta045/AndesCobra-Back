from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .serializers import *


router = DefaultRouter()
router.register(r'Roles', RolesViewSet, basename='Roles')
router.register(r'Usuarios', UsuariosViewSet, basename='Usuarios')
router.register(r'Campañas', CampañasViewSet, basename='Campañas')
router.register(r'Clientes', ClientesViewSet, basename='Clientes')
router.register(r'Codeudores', CodeudoresViewSet, basename='Codeudores')
router.register(r'Referencias', ReferenciasViewSet, basename='Referencias')
router.register(r'Obligaciones', ObligacionesViewSet, basename='Obligaciones')
router.register(r'Pagos', PagosViewSet, basename='Pagos')
router.register(r'ResultadosGestion', ResultadosGestionViewSet, basename='ResultadosGestion')
router.register(r'Gestiones', GestionesViewSet, basename='Gestiones') 



urlpatterns = [
    path('', include(router.urls)),
]