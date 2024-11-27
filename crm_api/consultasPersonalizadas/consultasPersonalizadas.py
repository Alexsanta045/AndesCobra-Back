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
from crm_api.serializers.interacciónStatsSerializer import CampañaStatsSerializer
from datetime import datetime



class ObligacionesView(APIView):
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

class InteraccionesPorFechaAPIView(APIView):
    def get(self, request, *args, **kwargs):
        fecha_param = request.query_params.get('fecha', None)
        
        # Filtro por fecha si se proporciona
        if fecha_param:
            try:
                fecha = datetime.strptime(fecha_param, '%Y-%m-%d').date()
                gestiones = Gestiones.objects.filter(fecha__date=fecha)
            except ValueError:
                return Response({'error': 'Fecha inválida, debe ser en formato YYYY-MM-DD'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            gestiones = Gestiones.objects.all()

        result = []
        totales = {
            'total_sms': 0,
            'total_wpp': 0,
            'total_llamadas': 0
        }

        for campaña in Campañas.objects.all():
            gestiones_campaña = gestiones.filter(resultado__campaña=campaña)
            
            # Contar interacciones por canal
            sms_count = gestiones_campaña.filter(cliente__canales_autorizados__sms=True).count()
            whatsapp_count = gestiones_campaña.filter(cliente__canales_autorizados__whatsapp=True).count()
            llamadas_count = gestiones_campaña.filter(cliente__canales_autorizados__telefonico=True).count()
            
            # Actualizar totales
            totales['total_sms'] += sms_count
            totales['total_wpp'] += whatsapp_count
            totales['total_llamadas'] += llamadas_count
            
            result.append({
                'campaña': campaña.nombre,
                'sms': sms_count,
                'wpp': whatsapp_count,
                'llamadas': llamadas_count,
            })

        # Devolver tanto las interacciones por campaña como los totales
        return Response({
            'interacciones_por_campaña': result,
            'totales': totales
        }, status=status.HTTP_200_OK)
