
from crm_api.serializers.serializers import *
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from . import auth_routes
from .consultasPersonalizadas.consultasPersonalizadas import *
from .pagos.ActualizarAcuerdoPagos import ActualizarAcuerdosPagoView
from .pagos.EjecutarPagos import EjecutarPagos
from .pagos.PagosMasivos import PagosMasivos
from .views import *
from .wolkwox_api.wolkvox_colgar import ColgarAPIView
from .wolkwox_api.wolkvox_dial import DialWolkvoxAPIView
from .wolkwox_api.wolkvox_mutear import MutearAPIView
from .consultasPersonalizadas.passwordChange import *
from .consultasPersonalizadas.generalStatistics import *

from .obligaciones.crearCliente import ClientesViewSet

router = DefaultRouter()

router.register(r'roles', RolesViewSet, basename='Roles')
router.register(r'campanas-api', CampañasViewSet, basename='Campañas')
router.register(r'clientes', ClientesViewSet, basename='Clientes')
router.register(r'telefono_cliente', Telefono_clienteViewSet, basename='Telefono cliente')
router.register(r'referencias', ReferenciasViewSet, basename='Referencias')
router.register(r'telefono_referencias', Telefono_referenciaViewSet, basename='Telefono referencia')
router.register(r'obligaciones', ObligacionesViewSet, basename='Obligaciones')
router.register(r'pagos', PagosViewSet, basename='Pagos')
router.register(r'resultadosGestion', ResultadosGestionViewSet, basename='ResultadosGestion')
router.register(r'gestiones', GestionesViewSet, basename='Gestiones')
router.register(r'chat', ChatViewSet, basename='Chat')
router.register(r'codeudores', CodeudoresViewSet, basename='Codeudores')
router.register(r'telefono_codeudor', Telefono_codeudorViewSet, basename='Telefono codeudor')
router.register(r'acuerdo_pago', Acuerdo_pagoViewSet, basename='Acuerdos de Pago')
router.register(r'CampanasUsuario', CampañaUsuarioViewSet, basename='campanasUsuario') 
router.register(r'CustomUser', CustomUserViewSet, basename='custom-user') 
router.register(r'tipo_gestion', TipoGestionViewSet, basename='tipo_gestion') 
router.register(r'historial_gestiones', HistorialGestionesViewSet, basename='historial_gestiones')


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
    path('campa/', CampañasView.as_view(), name='campa'),
    path('cliente_obligaciones/', ClientesObligaciones.as_view(), name='cliente_obligaciones'),
    path('colletion-management/', CollectionAndManagementView.as_view(), name='colletion-management'),
    path('campanas/interacciones/', InteraccionCampañasView.as_view(), name='get_interacciones_por_fecha'),
    path('resultados_gestion/campaña/', ResultadosGestionView.as_view(), name='resultados_gestion_por_campaña'),
    path('campanas-por-usuario/', CampañasPorUsuario.as_view(), name='campanas-por-usuario'),  
    path('borrarCampañas/', CampañaUsuarioDeleteView.as_view(), name='borrarCampañas'),  
    path('dial/', DialWolkvoxAPIView.as_view(), name='dial-wolkvox'),  
    path('colgar/', ColgarAPIView.as_view(), name='colgar'),
    path('mutear/', MutearAPIView.as_view(), name='mutear'),
    path('change-password/', change_user_password, name='change_password'),
    path('request-password-change/', change_user_password, name='request_password_change'),
    path('get-password-change-requests/', get_password_change_requests, name='get_password_change_requests'),
    path('reject-password-change-request/<str:username_or_email>/', reject_password_change_request),
    path('get-password-change-history/', get_password_change_history, name='get-password-change-history'),  # URL para obtener el historial de contraseñas
    path('gestiones-por-dia/', gestiones_por_dia, name='gestiones_por_dia'),
    path('estadisticas-asesor/', estadisticas_asesor, name='estadisticas_asesor'),
]
