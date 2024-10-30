from rest_framework import serializers
from .models import *


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'


class CampañasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campañas
        fields = ['id', 'nombre'] 


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'


class CodeudoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codeudores
        fields = '__all__'


class ReferenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referencias
        fields = '__all__'


class ObligacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obligaciones
        fields = '__all__'


class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'


class ResultadosGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadosGestion
        fields = '__all__'


class GestionesSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)
    cliente = serializers.PrimaryKeyRelatedField(read_only=True)
    resultado = serializers.CharField(
        source='resultado.nombre', read_only=True)
    comentarios = serializers.CharField(read_only=True)

    class Meta:
        model = Gestiones
        fields = '__all__'

    def get_usuario(self, obj):
        return obj.usuario.id

    def get_cliente(self, obj):
        return obj.cliente.id


class CampañasUsuariosSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.SerializerMethodField()
    nombre_campaña = serializers.SerializerMethodField()

    class Meta:
        model = CampañasUsuarios
        fields = '__all__'  

    def get_nombre_usuario(self, obj):
        # Obtén el nombre completo del usuario
        return f"{obj.usuarios_id.nombres} {obj.usuarios_id.apellidos}"

    def get_nombre_campaña(self, obj):
        # Obtén el nombre de la campaña
        return obj.campañas_id.nombre
