from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import * 

class ObligacionesView(APIView):
    def get(self, request, *args, **kwargs):
        campaña = request.query_params.get('campaña')
        nit_cliente = request.query_params.get('cliente')

        # Si ambos parámetros son nulos, devolvemos un error.
        if not campaña and not nit_cliente:
            return Response(
                {"error": "Debe proporcionar al menos un parámetro: 'campaña' o 'cliente'."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Filtrar por campaña y cliente solo si ambos parámetros existen.
            if campaña and nit_cliente:
                # Filtrar por ambos parámetros: campaña y cliente (NIT)
                obligaciones = Obligaciones.objects.filter(campaña__id=campaña, cliente__nit=nit_cliente)
            elif campaña:
                # Solo filtrar por campaña
                obligaciones = Obligaciones.objects.filter(campaña__id=campaña)
            elif nit_cliente:
                # Solo filtrar por cliente
                obligaciones = Obligaciones.objects.filter(cliente__nit=nit_cliente)

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
        campaña_id = request.query_params.get('campaña')
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
