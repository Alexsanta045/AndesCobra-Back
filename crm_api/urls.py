# -*- coding: utf-8 -*-

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .serializers import *
from . import auth_routes



router = DefaultRouter()

router.register(r'roles', RolesViewSet, basename='Roles')
router.register(r'usuarios', UsuariosViewSet, basename='Usuarios')
router.register(r'campanas', CampañasViewSet, basename='Campañas')
router.register(r'clientes', ClientesViewSet, basename='Clientes')
router.register(r'telefono_cliente', Telefono_clienteViewSet, basename='Telefono cliente')
router.register(r'direccion_cliente', Direccion_clienteViewSet, basename='Dirección cliente')
router.register(r'referencias', ReferenciasViewSet, basename='Referencias')
router.register(r'obligaciones', ObligacionesViewSet, basename='Obligaciones')
router.register(r'pagos', PagosViewSet, basename='Pagos')
router.register(r'resultadosGestion', ResultadosGestionViewSet, basename='ResultadosGestion')
router.register(r'gestiones', GestionesViewSet, basename='Gestiones')
router.register(r'chat', ChatViewSet, basename='Chat')
router.register(r'tipo_identificacion', Tipo_identificacionViewSet, basename='Tipo de identificacion')
router.register(r'pais', PaisViewSet, basename='País')
router.register(r'departamento', DepartamentoViewSet, basename='Departamento')
router.register(r'ciudad', CiudadViewSet, basename='Ciudad')
router.register(r'codeudores', CodeudoresViewSet, basename='Codeudores')
router.register(r'telefono_codeudor', Telefono_codeudorViewSet, basename='Telefono codeudor')
router.register(r'direccion_codeudor', Direccion_codeudorViewSet, basename='Dirección codeudor')
router.register(r'canales', CanalesViewSet, basename='Canales')
router.register(r'acuerdo_pago', Acuerdo_pagoViewSet, basename='Acuerdos de Pago')
router.register(r'CampanasUsuario', CampañaUsuarioViewSet, basename='campanasUsuario') 



urlpatterns = [
    path('', include(router.urls)),
    path('login/', auth_routes.login, name='login'),
    path('register/', auth_routes.register, name='register'),
    path('profile/', auth_routes.profile, name='profile'),
]
