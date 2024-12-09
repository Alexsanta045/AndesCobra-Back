from crm_api.serializers.clientDataSerializer import ClientDataSerializer
from crm_api.serializers.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
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
        cliente = request.query_params.get('cliente')

        # Validación de parámetros
        if not campaña:
            return Response({"error": "El parámetro 'campaña' es requerido."}, status=status.HTTP_400_BAD_REQUEST)
        
        acuerdos = []  

        try:
            # Filtro de obligaciones basado en los parámetros
            if campaña and not cliente:
                obligaciones = Obligaciones.objects.filter(campaña=campaña)
            elif campaña and cliente:
                obligaciones = Obligaciones.objects.filter(campaña=campaña, cliente=cliente)
            else:
                return Response({"error": "Parámetros no válidos."}, status=status.HTTP_400_BAD_REQUEST)

            if not obligaciones:
                return Response({"error": "No se encontraron obligaciones para esta campaña o cliente."}, status=status.HTTP_404_NOT_FOUND)

            # Acumular acuerdos de pago
            for obligacion in obligaciones:
                acuerdos.extend(Acuerdo_pago.objects.filter(codigo_obligacion=obligacion).order_by('-fecha_pago'))

            # Serializar los acuerdos encontrados
            serializer = Acuerdo_pagoSerializer(acuerdos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        role_id = request.query_params.get('role')

        # Verificar si al menos uno de los parámetros está presente.
        if not campaña_id and not role_id:
            return Response(
                {"error": "Debe proporcionar al menos un parámetro: 'campaña' o 'role'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Usar select_related para optimizar la consulta y asegurar acceso al rol
            relaciones = CampañasUsuarios.objects.select_related('usuarios_id__role')

            # Aplicar filtros condicionales
            if campaña_id and role_id:
                # Filtrar por ambos parámetros: campaña y rol
                relaciones = relaciones.filter(
                    campañas_id=campaña_id, 
                    usuarios_id__role__id=role_id
                )
            elif campaña_id:
                # Solo filtrar por campaña
                relaciones = relaciones.filter(campañas_id=campaña_id)
            elif role_id:
                # Solo filtrar por rol
                relaciones = relaciones.filter(usuarios_id__role__id=role_id)

            # Eliminar duplicados para evitar usuarios repetidos
            relaciones = relaciones.distinct('usuarios_id')

            # Si no se encuentran relaciones, devolver 404.
            if not relaciones.exists():
                return Response(
                    {"error": "No se encontraron usuarios con los parámetros proporcionados."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Obtener los usuarios relacionados
            usuarios = [relacion.usuarios_id for relacion in relaciones]

            # Serializar los datos y devolverlos.
            serializer = UserSerializer(usuarios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # Si ocurre un error inesperado, devolver un error genérico.
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            
class PagosView(APIView):
    def get(self, request, *args, **kwargs):
        campaña = request.query_params.get('campaña')
        cliente = request.query_params.get('cliente')
        pagos_data = []

        if not campaña:
            return Response({"error": "El parámetro 'campaña' es requerido."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Filtrar las obligaciones basadas en los parámetros de campaña y cliente
            if cliente:
                obligaciones = Obligaciones.objects.filter(campaña=campaña, cliente=cliente)
            else:
                obligaciones = Obligaciones.objects.filter(campaña=campaña)

            # Verificar si se encontraron obligaciones
            if not obligaciones:
                return Response({"error": "No se encontraron obligaciones para esta campaña y cliente."}, status=status.HTTP_404_NOT_FOUND)

            # Acumular los pagos en la lista
            for obligacion in obligaciones:
                pagos = Pagos.objects.filter(obligacion=obligacion).order_by('-fecha')
                pagos_data.extend(PagosSerializer(pagos, many=True).data)

            # Responder con los pagos serializados
            return Response(pagos_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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

class CampañasPorUsuario(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener el id del usuario desde los parámetros de la consulta
        usuario_id = request.query_params.get('usuario_id')

        # Verificar si se proporcionó el id del usuario
        if not usuario_id:
            return Response(
                {"error": "Debe proporcionar el parámetro 'usuario_id'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Filtrar las campañas asociadas al usuario especificado
            relaciones = CampañasUsuarios.objects.filter(usuarios_id=usuario_id)

            # Si no se encuentran campañas, devolver un 404
            if not relaciones.exists():
                return Response(
                    {"error": "No se encontraron campañas asociadas a este usuario."},
                    status=status.HTTP_404_NOT_FOUND
                )

            # Obtener las campañas relacionadas
            campañas = [relacion.campañas_id for relacion in relaciones]

            # Serializar las campañas y devolverlas
            serializer = CampañasSerializer(campañas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # Si ocurre un error inesperado, devolver un error genérico
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CampañaUsuarioDeleteView(APIView):

    def delete(self, request, *args, **kwargs):
        campañas=request.query_params.get('id_campaña')
        usuarios=request.query_params.get('id_usuario')
        # Filtra los objetos basados en los parámetros de la solicitud
        campaña_usuario = CampañasUsuarios.objects.filter(usuarios_id=usuarios, campañas_id=campañas)
        
        # Verifica si existen resultados
        if campaña_usuario.exists():
            campaña_usuario.delete()  # Elimina los registros encontrados
            return Response({"detail": "Registro eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No se encontró el registro."}, status=status.HTTP_404_NOT_FOUND)
    
