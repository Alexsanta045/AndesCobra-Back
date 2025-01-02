
from crm_api.serializers.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import  viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
import pandas as pd
from django.db.models import Sum


from .obligaciones.cargarObligaciones import cargarObligaciones
from .gestionesMasivas.cargarGestiones import cargarGestiones
from .filters import *
from .models import *
from .serializers import *
from .serializers.clienteObligacionesSerializer import ClienteObligacionesSerializer
from .serializers.historialGestiones import HistorialGestionesSerializer


class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


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

#     filter_backends = (DjangoFilterBackend, OrderingFilter)
#     filterset_class = ClientesFilter

#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]


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

class CargarObligacionesViewSet(APIView):
    def post(self, request, *args, **kwargs):
        archivo = request.FILES.get('archivo')
        id_campaña = request.data.get('id_campaign')

        return cargarObligaciones( id_campaña, archivo)

class CargarGestionesViewSet(APIView):
    def post(self, request, *args, **kwargs):
        archivo = request.FILES.get('archivo')
        id_campaña = request.data.get('id_campaign')
        return cargarGestiones(id_campaña, archivo)



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
    
# class DepartamentoViewSet(viewsets.ModelViewSet):
#     queryset = Departamento.objects.all()
#     serializer_class = DepartamentoSerializer

#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
    
# class CiudadViewSet(viewsets.ModelViewSet):
#     queryset = Ciudad.objects.all()
#     serializer_class = CiudadSerializer

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

class Telefono_referenciaViewSet(viewsets.ModelViewSet):
    queryset = Telefono_referencia.objects.all()
    serializer_class = Telefono_referenciaSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
# class Direccion_clienteViewSet(viewsets.ModelViewSet):
#     queryset = Direccion_cliente.objects.all()
#     serializer_class = Direccion_clienteSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
# class Direccion_codeudorViewSet(viewsets.ModelViewSet):
#     queryset = Direccion_codeudor.objects.all()
#     serializer_class = Direccion_codeudorSerializer

#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
    
# class Direccion_referenciaViewSet(viewsets.ModelViewSet):
#     queryset = Direccion_referencia.objects.all()
#     serializer_class = Direccion_referenciaSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
# class CanalesViewSet(viewsets.ModelViewSet):
#     queryset = Canales.objects.all()
#     serializer_class = CanalesSerializer

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class Acuerdo_pagoViewSet(viewsets.ModelViewSet):
    queryset = Acuerdo_pago.objects.all()
    serializer_class = Acuerdo_pagoSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = AcuerdoPagoFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
class CodigosEstadoViewSet(viewsets.ModelViewSet):
    queryset = CodigosEstado.objects.all()
    serializer_class = CodigosEstadoSerializer
    
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CodigosEstadoFilter
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

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

# class RecaudoCampañaViewSet(APIView):
#     def get(self, request, *args, **kwargs):
#         campaña = request.query_params.get('campaña')
#         fecha_inicio = request.query_params.get('fecha_inicio')
#         fecha_fin = request.query_params.get('fecha_fin')

#         if not campaña:
#             return Response(
#                 {"error": "El parámetro 'campaña' es obligatorio."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
        
#         try:
#             # Construir el filtro dinámico
#             filtros = {'campaña': campaña}
#             if fecha_inicio and fecha_fin:
#                 filtros['fecha__range'] = [fecha_inicio, fecha_fin]

#             # Filtrar registros y calcular la sumatoria
#             registros = Obligaciones.objects.filter(**filtros)
#             suma = registros.aggregate(total=Sum('valor_vencido'))['total'] or 0

#             # Responder con la sumatoria
#             return Response({"campaña": campaña, "suma": suma}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(
#                 {"error": f"Error al procesar la solicitud: {str(e)}"},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )


class CantidadAcuerdosPagoViewSet(APIView):
    def get(self, request):
        campaña = request.query_params.get('campaña')

        if not campaña:
            return Response(
                {'Error': 'El parámetro campaña es obligatorio'},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            acuerdos = Acuerdo_pago.objects.filter(
                codigo_obligacion__campaña__id=campaña
            )

            # Agregar anotaciones para contar y sumar `valor_cuota`
            resultados = acuerdos.values('estado').annotate(
                total=Count('id'),
                suma_valor_cuota=Sum('valor_cuota')
            )

            # Construir los datos de respuesta
            data = {
                estado['estado']: {
                    'Cantidad': estado['total'],
                    'valor_total': estado['suma_valor_cuota'] or 0
                } for estado in resultados
            }

            # Calcular los totales generales
            total_acuerdos = sum(estado['total'] for estado in resultados)
            suma_total_cuotas = sum(estado['suma_valor_cuota'] or 0 for estado in resultados)

            # Agregar los totales generales bajo la clave `Creados`
            data['Creados'] = {
                'Cantidad': total_acuerdos,
                'valor_total': suma_total_cuotas
            }

            return Response(data)
        except Exception as e:
            return Response(
                {'error': f'Error al obtener la cantidad de acuerdos de pago: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    

