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
        # Especifica que el modelo asociado es Gestiones
        model = Gestiones
        # Define los campos que se incluirán en la representación del serializer
        fields = ['id', 'usuario', 'cliente', 'resultado', 'fecha', 'comentarios']
    
    def to_representation(self, instance):
        # Obtiene la representación estándar del objeto usando la implementación base
        representation = super().to_representation(instance)
        # Formatea el campo 'fecha' si existe en la instancia
        if instance.fecha:
            representation['fecha'] = instance.fecha.strftime('%d-%m-%y %H:%M')
        # Devuelve la representación final del objeto
        return representation