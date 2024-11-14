from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *

class ObligacionesView(APIView):
    def get(self, request, *args, **kwargs):
        usuario = request.query_params.get('usuario')

        if not usuario:
            return Response({"error": "Usuario no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

        cantidad_obligaciones = {}
        cantidad_campañas = {}

        campañas_usuarios = CampañasUsuarios.objects.filter(usuarios_id=usuario)

        for campaña_usuario in campañas_usuarios:
            campaña = campaña_usuario.campañas_id

            cantidad_campañas[campaña.nombre] = cantidad_campañas.get(campaña.nombre, 0) + 1

            obligaciones = Obligaciones.objects.filter(campaña=campaña)
            cantidad_obligaciones[campaña.nombre] = obligaciones.count()

        response_data = {
            "mensaje": "Datos de obligaciones y campañas obtenidos",
            "cantidad_obligaciones": cantidad_obligaciones,
            "cantidad_campañas": cantidad_campañas,
        }

        return Response(response_data, status=status.HTTP_200_OK)
