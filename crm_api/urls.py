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
router.register(r'codeudores', CodeudoresViewSet, basename='Codeudores')
router.register(r'referencias', ReferenciasViewSet, basename='Referencias')
router.register(r'obligaciones', ObligacionesViewSet, basename='Obligaciones')
router.register(r'pagos', PagosViewSet, basename='Pagos')
router.register(r'resultadosGestion', ResultadosGestionViewSet, basename='ResultadosGestion')
router.register(r'gestiones', GestionesViewSet, basename='Gestiones')



urlpatterns = [
    path('', include(router.urls)),
    path('login/', auth_routes.login, name='login'),
    path('register/', auth_routes.register, name='register'),
    path('profile/', auth_routes.profile, name='profile'),
]