from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import *
from ..models import *
from crm_api.serializers.serializers import *
from crm_api.serializers.clientDataSerializer import ClientDataSerializer
from ..serializers import *
from ..serializers.clienteObligacionesSerializer import ClienteObligacionesSerializer
from crm_api.serializers.collectionAndManagement import CollectionAndManagement
from crm_api.serializers.interaccionSerializer import InteraccionSerializer
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class ObligacionesView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        campaña = request.query_params.get('campaña')
    
        try:
            nit_cliente = request.query_params.get('cliente')
        except Exception as e:
            return print(f"no se proporcionó nit")
        
        try:
            celular = request.query_params.get('celular')
        except Exception as e:
            return print(f"no se proporcionó celular")
         
        # Si ambos parámetros son nulos, devolvemos un error.
        if not campaña and not nit_cliente and not celular:
            return Response(
                {"error": "Debe proporcionar al menos un parámetro: 'campaña' o 'cliente' o 'celular."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Filtrar por campaña y cliente solo si ambos parámetros existen.
            if campaña and nit_cliente:
                # Filtrar por ambos parámetros: campaña y cliente (NIT)
                obligaciones = Obligaciones.objects.filter(campaña__id=campaña, cliente__nit=nit_cliente)
            elif campaña and celular:
                celular_cliente = Telefono_cliente.objects.get(numero=celular)
                cliente = Clientes.objects.get(nit=celular_cliente.cliente.nit)
                obligaciones = Obligaciones.objects.filter(campaña__id=campaña, cliente=cliente)
            elif campaña:
                # Solo filtrar por campaña
                obligaciones = Obligaciones.objects.filter(campaña__id=campaña)
            elif nit_cliente:
                # Solo filtrar por cliente
                obligaciones = Obligaciones.objects.filter(cliente__nit=nit_cliente)
            elif celular:
                celular_cliente = Telefono_cliente.objects.get(numero=celular)
                cliente = Clientes.objects.get(nit=celular_cliente.cliente.nit)
                obligaciones = Obligaciones.objects.filter(cliente=cliente)

            # Si no se encuentran resultados, retornamos un 404.
            if not obligaciones.exists():
                return Response(
                    {"error": "No se encontraron obligaciones con los parámetros proporcionados."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Serializar los datos y devolverlos.
            serializer = ObligacionesSerializer(obligaciones, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # Si ocurre un error inesperado, devolvemos un error genérico.
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class AcuerdosDePagoView(APIView):
    def get(self, request, *args, **kwargs):
        campaña = request.query_params.get('campaña')

        try:
            obligaciones = Obligaciones.objects.filter(campaña=campaña)
            
            for obligacion in obligaciones:
                acuerdos = Acuerdo_pago.objects.filter(codigo_obligacion=obligacion)
                
                serializer = Acuerdo_pagoSerializer(acuerdos, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Obligaciones.DoesNotExist:
            return Response({"error": "No se encontraron acuerdos de pago para esta campaña"}, status=status.HTTP_404_NOT_FOUND)
        

class ClientesView(APIView):
    def get(self, request, *args, **kwargs):
        campaña = request.query_params.get('campaña')

        try:
            obligaciones = Obligaciones.objects.filter(campaña=campaña)
            clientes_data = []
            clientes_nits = set() 

            for obligacion in obligaciones:
                cliente = obligacion.cliente
                if cliente.nit not in clientes_nits:
                    clientes_nits.add(cliente.nit)
                    serializer = ClientesSerializer(cliente)
                    clientes_data.append(serializer.data)

            return Response(clientes_data, status=status.HTTP_200_OK)
        
        except Obligaciones.DoesNotExist:
            return Response({"error": "No se encontraron clientes para esta campaña"}, status=status.HTTP_404_NOT_FOUND)


class UsuariosView(APIView):
    def get(self, request, *args, **kwargs):
        campaña_id = request.query_params.get('campana')    
        
        try:
            relaciones = CampañasUsuarios.objects.filter(campañas_id=campaña_id)
            usuarios = [relacion.usuarios_id for relacion in relaciones]
            
            serializer = UserSerializer(usuarios, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except CampañasUsuarios.DoesNotExist:
            return Response({"error": "No se encontraron usuarios para esta campaña"}, status=status.HTTP_404_NOT_FOUND)
        


class PagosView(APIView):
    def get(self, request, *args, **kwargs):
        campaña = request.query_params.get('campaña')
        pagos_data = []

        try:
            obligaciones = Obligaciones.objects.filter(campaña=campaña)

            for obligacion in obligaciones:
                pagos = Pagos.objects.filter(obligacion=obligacion)

                serializer = PagosSerializer(pagos, many=True)
                pagos_data.append(serializer.data)
                
            return Response(pagos_data, status=status.HTTP_200_OK)
        
        except Obligaciones.DoesNotExist:
            return Response({"error": "No se encontrararon pagos para esta campaña"}, status=status.HTTP_404_NOT_FOUND)

class GestionesView(APIView):
    def get(self, request, *args, **kwargs):
        campaña_id = request.query_params.get('campaña')
        try:
            relaciones = CampañasUsuarios.objects.filter(campañas_id=campaña_id)
            usuarios = [relacion.usuarios_id for relacion in relaciones]
            
            gestiones = Gestiones.objects.filter(usuario__in=usuarios)
            
            print(f"Se encontraron {gestiones.count()} gestiones.")
            
            gestiones_serializer = GestionesSerializer(gestiones, many=True)
            
            return Response({
                "gestiones": gestiones_serializer.data
            }, status=status.HTTP_200_OK)
        
        except CampañasUsuarios.DoesNotExist:
            return Response({"error": "No se encontraron gestiones para esta campaña"}, status=status.HTTP_404_NOT_FOUND)


class ClientDataView(APIView):
    def get(self, request):
        obligaciones = Obligaciones.objects.select_related("cliente", "campaña").all()
        serializer = ClientDataSerializer(obligaciones, many=True)
        return Response(serializer.data)


class ClientesObligaciones(APIView):
    def get(self, request):
        cliente = request.query_params.get('cliente')
        
        if not cliente:
            return Response(
                {"error": "el parámetro cliente es obligatorio."},
                status=status.HTTP_400_BAD_REQUEST)
        
        cliente_data = Clientes.objects.filter(nit=cliente)
        serializer = ClienteObligacionesSerializer(cliente_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CollectionAndManagementView(APIView):
    def get(self, request, *args, **kwargs):
        campañas = Campañas.objects.all()
        serializer = CollectionAndManagement(campañas, many=True)
        return Response(serializer.data)

class InteraccionCampañasView(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener todas las campañas
        campañas = Campañas.objects.all()
        
        # Calcular los totales de SMS, WhatsApp y llamadas
        total_sms = 0
        total_whatsapp = 0
        total_llamadas = 0

        # Recorremos todas las campañas para calcular los totales
        for campaña in campañas:
            total_sms += Gestiones.objects.filter(resultado__campaña=campaña, tipo_gestion__nombre="SMS").count()
            total_whatsapp += Gestiones.objects.filter(resultado__campaña=campaña, tipo_gestion__nombre="WhatsApp").count()
            total_llamadas += Gestiones.objects.filter(resultado__campaña=campaña, tipo_gestion__nombre="Llamada").count()

        # Usar el serializer para las campañas
        serializer = InteraccionSerializer(campañas, many=True)

        # Crear los totales
        total_data = {
            "total_sms": total_sms,
            "total_whatsapp": total_whatsapp,
            "total_llamadas": total_llamadas
        }

        # Devolver las campañas junto con los totales
        response_data = {
            "campañas": serializer.data,
            "total": total_data
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
    
class ResultadosGestionView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        try:
            campaña = request.query_params.get('campaña')
            
            resultado_gestion = ResultadosGestion.objects.filter(campaña=campaña, estado=True)
            
            serializer = ResultadosGestionSerializer(resultado_gestion, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)