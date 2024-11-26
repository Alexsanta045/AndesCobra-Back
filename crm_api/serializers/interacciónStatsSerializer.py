from rest_framework import serializers
from ..models import *
from django.db.models import Count

class InteracciónStatsSerializer(serializers.Serializer):
    SMS = serializers.IntegerField()
    WhatsApp = serializers.IntegerField()
    Llamadas = serializers.IntegerField()

class CampañaStatsSerializer(serializers.ModelSerializer):
    # Se usa el serializer de InteracciónStats
    interacciones = InteracciónStatsSerializer()

    class Meta:
        model = Campañas
        fields = ['nombre', 'interacciones']
