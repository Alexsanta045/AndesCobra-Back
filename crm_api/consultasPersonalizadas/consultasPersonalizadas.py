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
            
            serializer = ObligacionesSerializer(obligaciones, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Obligaciones.DoesNotExist:
            return Response({"error": "No se encontraron obligaciones para esta campaña"}, status=status.HTTP_404_NOT_FOUND)
        
