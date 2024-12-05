
from crm_api.serializers.serializers import *
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from . import auth_routes
from .consultasPersonalizadas.consultasPersonalizadas import *
from .pagos.ActualizarAcuerdoPagos import ActualizarAcuerdosPagoView
from .pagos.EjecutarPagos import EjecutarPagos
from .pagos.PagosMasivos import PagosMasivos
from .views import *

router = DefaultRouter()

router.register(r'roles', RolesViewSet, basename='Roles')
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
router.register(r'CustomUser', CustomUserViewSet, basename='custom-user') 
router.register(r'ClienteObligaciones', ClienteObligacionesViewSet, basename='cliente-obligaciones')



urlpatterns = [
    path('', include(router.urls)),
    path('register/', auth_routes.register, name='register'),
    path('login/', auth_routes.login, name='login'),
    path('logout/', auth_routes.logout, name='logout'), 
    path('obliga/', ObligacionesView.as_view(), name='obliga'), 
    path('acuer/', AcuerdosDePagoView.as_view(), name='acuer'), 
    path('clie/', ClientesView.as_view(), name='clie'), 
    path('usu/', UsuariosView.as_view(), name='usu'), 
    path('pag/', PagosView.as_view(), name='pag'), 
    path('gest/', GestionesView.as_view(), name='gest'), 
    path('ejecutar_pagos/', EjecutarPagos.as_view(), name='ejecutar_pagos'),
    path('pagos_masivos/', PagosMasivos.as_view(), name='pagos_masivos'),
    path('actualizar_acuerdos_pagos/', ActualizarAcuerdosPagoView.as_view(), name='actualizar_acuerdos_pagos'),
    path('client-data/', ClientDataView.as_view(), name='client-data'),
    path('campanas-por-usuario/', CampañasPorUsuario.as_view(), name='campanas-por-usuario'),  
    path('borrarCampañas/', CampañaUsuarioDeleteView.as_view(), name='borrarCampañas'),  
    path('dial/', DialWolkvoxAPIView.as_view(), name='dial-wolkvox'),  
    path('colgar/', ColgarAPIView.as_view(), name='colgar'),
    path('mutear/', MutearAPIView.as_view(), name='mutear'),
]
