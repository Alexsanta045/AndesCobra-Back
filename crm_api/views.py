from crm_api.serializers.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

from  .obligaciones.cargarObligaciones import cargarObligaciones
from .filters import *
from .models import *
from .models import CampañasUsuarios
from .serializers import *
from .serializers.clienteObligacionesSerializer import ClienteObligacionesSerializer


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

# class ClientesViewSet(viewsets.ModelViewSet):
#     queryset = Clientes.objects.all()
#     serializer_class = ClientesSerializer

#     filter_backends = (DjangoFilterBackend, OrderingFilter)
#     filterset_class = ClientesFilter

#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]

#     def crear_cliente_si_no_existe(self, datos_cliente):
#         try:
#             cliente, creado = Clientes.objects.get_or_create(
#                 documento=datos_cliente['Documento cliente'],
#                 defaults={
#                     # Aquí agregas los campos para nuevos clientes
#                     'nit': datos_cliente.get('Documento cliente'),
#                     'nombres': datos_cliente.get('Nombre', ''),
#                     'email': datos_cliente.get('Apellido', ''),
#                     # Agrega más campos según tu modelo
#                 }
#             )
#             return cliente
#         except Exception as e:
#             # Manejo de errores si falla la creación
#             print(f"Error creando cliente: {e}")
#             return None


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

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # -----------------------------------------------------------------------------------------------------
class CargarObligacionesViewSet(APIView):
    def post(self, request, *args, **kwargs):
        archivo = request.FILES.get('archivo')
        id_campaña = request.data.get('id_campaign')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        print(id_campaña)

        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return cargarObligaciones( id_campaña, archivo)
        # if not archivo:
        #     return Response({'error': 'No se ha proporcionado un archivo'}, 
        #                     status=status.HTTP_400_BAD_REQUEST)
        # try:
        #     df = pd.read_excel(archivo)
        #     print (df)

        #     # Columnas requeridas
        #     columnas_requeridas = [
        #         # 'Codigo obligacion',
        #         'Codigo campaña',
        #         'Documento cliente',
        #         'Valor obligacion',
        #         'Fecha obligacion',
        #         'Fecha vencimiento',
        #         'Valor mora' 
        #     ]

        #     if not all(col in df.columns for col in columnas_requeridas):
        #             return Response({'error': 'Faltan columnas requeridas en el archivo'}, status=status.HTTP_400_BAD_REQUEST)
        #     if('Codigo obligacion' in df.columns):
        #         for _, fila in df.iterrows():
    
        #             obligacion = Obligaciones(
        #                 codigo_obligacion=fila['Codigo obligacion'],
        #                 campaña_id=fila['Codigo campaña'],
        #                 cliente_id=fila['Documento cliente'],
        #                 fecha_obligacion=fila['Fecha obligacion'],
        #                 fecha_vencimiento_cuota=fila['Fecha vencimiento'],
        #                 valor_capital=fila['Valor obligacion'],
        #                 valor_mora=fila['Valor mora']
        #             )

        #             columnas_adicionales = {
        #                 col: fila[col]
        #                 for col in df.columns if col not in columnas_requeridas
        #             }
        #             obligacion.campos_opcionales = columnas_adicionales
        #             obligacion.save()
        #     else: # si no esta el codigo de la obligacion lo deja vacion
        #         for _, fila in df.iterrows():
    
        #             obligacion = Obligaciones(
        #                 codigo_obligacion= None,
        #                 campaña_id=fila['Codigo campaña'],
        #                 cliente_id=fila['Documento cliente'],
        #                 fecha_obligacion=fila['Fecha obligacion'],
        #                 fecha_vencimiento_cuota=fila['Fecha vencimiento'],
        #                 valor_capital=fila['Valor obligacion'],
        #                 valor_mora=fila['Valor mora']
        #             )

        #             columnas_adicionales = {
        #                 col: fila[col]
        #                 for col in df.columns if col not in columnas_requeridas
        #             }
        #             obligacion.campos_opcionales = columnas_adicionales
        #             obligacion.save()

        #     return Response({'mensaje': 'Obligaciones guardadas exitosamente'}, status=status.HTTP_201_CREATED)
        # except Exception as e:
        #     # import traceback
        #     # error_trace = traceback.format_exc()
        #     # print(error_trace)  # Rastreo completo del error en logs
        #     return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # -----------------------------------------------------------------------------------------------------

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