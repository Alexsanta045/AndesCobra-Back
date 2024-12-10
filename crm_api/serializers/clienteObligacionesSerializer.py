from rest_framework import serializers
from django.db.models import Sum
from datetime import datetime
from ..models import Clientes, Obligaciones, Telefono_cliente
# from .serializers import CanalesSerializer

class ClienteObligacionesSerializer(serializers.ModelSerializer):
    nit = serializers.CharField()
    nombres = serializers.CharField()
    email = serializers.CharField()
    numero_celular = serializers.SerializerMethodField()
    total_obligaciones = serializers.SerializerMethodField()
    # total_valor_capital = serializers.SerializerMethodField()
    # total_valor_mora = serializers.SerializerMethodField()
    # dias_mora = serializers.SerializerMethodField()
    # canales_autorizados = CanalesSerializer()
    
    class Meta:
        model = Clientes
        fields = '__all__'
        
    def get_numero_celular(self, obj):
        try:
            telefono = Telefono_cliente.objects.filter(cliente=obj).first()
            return telefono.numero
        except Telefono_cliente.DoesNotExist:
            return None
        
    def get_total_obligaciones(self, obj):
        obligaciones = Obligaciones.objects.filter(cliente=obj)
        return obligaciones.count()
    
    # def get_total_valor_capital(self, obj):
    #     obligaciones = Obligaciones.objects.filter(cliente=obj)
    #     total_valor_capital = obligaciones.aggregate(total=Sum('valor_capital'))['total']
    #     return total_valor_capital or 0 
    
    # def get_total_valor_mora(self, obj):
    #     obligaciones = Obligaciones.objects.filter(cliente=obj)
    #     total_valor_mora = obligaciones.aggregate(total=Sum('valor_mora'))['total']
    #     return total_valor_mora or 0
    
    # def get_dias_mora(self, obj):
    #     obligaciones = Obligaciones.objects.filter(cliente=obj).order_by('fecha_vencimiento_cuota').first()
    #     if not obligaciones or not obligaciones.fecha_vencimiento_cuota:
    #         return 0  # Manejar casos donde no hay obligaciones o fecha es nula
    #     # Asegúrate de usar .date() para que ambos sean tipo date
    #     dias_mora = (datetime.now().date() - obligaciones.fecha_vencimiento_cuota).days
    #     return dias_mora
            