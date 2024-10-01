from rest_framework import serializers
from .models import *


class GestionesSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)
    cliente = serializers.PrimaryKeyRelatedField(read_only=True)
    resultado = serializers.CharField(source='resultado.nombre', read_only=True)
    comentarios = serializers.CharField(read_only=True)
    
    class Meta:
        model = Gestiones
        fields = '__all__'
        
    def get_usuario(self, obj):
        return obj.usuario.id
    
    def get_cliente(self, obj):
        return obj.cliente.id