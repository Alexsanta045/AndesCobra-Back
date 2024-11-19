from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import * 

class ObligacionesView(APIView):
    def get(self, request, *args, **kwargs):
        campaña = request.query_params.get('campaña')
        try:
            obligaciones = Obligaciones.objects.filter(campaña=campaña)
            
            serializer = ObligacionesSerializer(obligaciones, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Obligaciones.DoesNotExist:
            return Response({"error": "No se encontraron obligaciones para esta campaña"}, status=status.HTTP_404_NOT_FOUND)
        
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

            for obligacion in obligaciones:
                cliente = obligacion.cliente
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
            
            gestiones_serializer = GestionesSerializer(gestiones, many=True)
            
            return Response({
                "gestiones": gestiones_serializer.data
            }, status=status.HTTP_200_OK)
        
        except CampañasUsuarios.DoesNotExist:
            return Response({"error": "No se encontraron gestiones para esta campaña"}, status=status.HTTP_404_NOT_FOUND)
        