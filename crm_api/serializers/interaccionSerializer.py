from rest_framework import serializers
from ..models import Campañas, Gestiones, Tipo_gestion

class InteraccionSerializer(serializers.ModelSerializer):
    # Campos para contar el total de gestiones por cada tipo
    llamadas = serializers.SerializerMethodField()
    sms = serializers.SerializerMethodField()
    whatsapp = serializers.SerializerMethodField()

    class Meta:
        model = Campañas
        fields = ['id', 'nombre', 'llamadas', 'sms', 'whatsapp']

    def get_llamadas(self, obj):
        # Contar las gestiones de tipo "Llamada"
        return Gestiones.objects.filter(resultado__campaña=obj, tipo_gestion__nombre="Llamada").count()

    def get_sms(self, obj):
        # Contar las gestiones de tipo "SMS"
        return Gestiones.objects.filter(resultado__campaña=obj, tipo_gestion__nombre="SMS").count()

    def get_whatsapp(self, obj):
        # Contar las gestiones de tipo "WhatsApp"
        return Gestiones.objects.filter(resultado__campaña=obj, tipo_gestion__nombre="WhatsApp").count()


# Serializador para mostrar los totales de gestiones
class CampañasTotalSerializer(serializers.Serializer):
    total_sms = serializers.IntegerField()
    total_whatsapp = serializers.IntegerField()
    total_llamadas = serializers.IntegerField()

    class Meta:
        fields = ['total_sms', 'total_whatsapp', 'total_llamadas']


class CampañasGestionConTotalSerializer(serializers.Serializer):
    # Aquí contendremos tanto los datos de la campaña como los totales
    campañas = InteraccionSerializer(many=True)
    total = CampañasTotalSerializer()

    def to_representation(self, instance):
        # Primero, obtenemos los datos de todas las campañas
        campañas_data = InteraccionSerializer(instance, many=True).data

        # Calcular los totales
        total_sms = 0
        total_whatsapp = 0
        total_llamadas = 0

        for campaña in instance:
            total_sms += Gestiones.objects.filter(resultado__campaña=campaña, tipo_gestion__nombre="SMS").count()
            total_whatsapp += Gestiones.objects.filter(resultado__campaña=campaña, tipo_gestion__nombre="WhatsApp").count()
            total_llamadas += Gestiones.objects.filter(resultado__campaña=campaña, tipo_gestion__nombre="Llamada").count()

        # Crear el objeto de totales
        total_data = {
            "total_sms": total_sms,
            "total_whatsapp": total_whatsapp,
            "total_llamadas": total_llamadas
        }

        # Retornamos los datos de las campañas y los totales
        return {
            "campañas": campañas_data,
            "total": total_data
        }
