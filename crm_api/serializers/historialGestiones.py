from rest_framework import serializers
from ..models import Gestiones


class HistorialGestionesSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    usuario = serializers.CharField(source='usuario.username')
    cliente = serializers.CharField(source='cliente.nombres')
    resultado = serializers.CharField(source='resultado.nombre')
    fecha = serializers.DateTimeField()
    comentarios = serializers.CharField()
    
    class Meta:
        model = Gestiones
        fields = ['id', 'usuario', 'cliente', 'resultado', 'fecha', 'comentarios']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.fecha:
            representation['fecha'] = instance.fecha.strftime('%d-%m-%y %H:%M')
        return representation