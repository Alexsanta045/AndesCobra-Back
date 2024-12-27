from rest_framework import serializers
from django.db.models import Sum
from datetime import datetime
from ..models import Clientes, Obligaciones, Telefono_cliente
from ..serializers.serializers import Telefono_clienteSerializer


class ClienteObligacionesSerializer(serializers.ModelSerializer):
    nit = serializers.CharField()
    nombres = serializers.CharField()
    email = serializers.CharField()
    celulares = serializers.SerializerMethodField()
    total_obligaciones = serializers.SerializerMethodField()
    total_valor_capital = serializers.SerializerMethodField()
    total_valor_mora = serializers.SerializerMethodField()
    dias_mora = serializers.SerializerMethodField()
    total_intereses = serializers.SerializerMethodField()
    total_a_pagar = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Clientes
        fields = '__all__'
        
    def get_celulares(self, obj):
        try:
            # Obtener todos los números de teléfono asociados al cliente
            telefonos = Telefono_cliente.objects.filter(cliente=obj).order_by('-rating')

            # Si existen números, devolver una lista de diccionarios con los valores deseados
            if telefonos.exists():
                result = []
                for telefono in telefonos:
                    # Agregar un objeto o diccionario con el número y otros valores
                    telefono_info = {
                        "numero": telefono.numero,
                        "rating": telefono.rating,
                    }
                    result.append(telefono_info)
                return result  # Lista de diccionarios con los valores

            # Si no hay números, retornar None
            return None
        
        except Telefono_cliente.DoesNotExist:
            return None

    def get_total_obligaciones(self, obj):
        obligaciones = Obligaciones.objects.filter(cliente=obj)
        return obligaciones.count()
    
    def get_total_valor_capital(self, obj):
        obligaciones = Obligaciones.objects.filter(cliente=obj)
        total_valor_capital = obligaciones.aggregate(total=Sum('saldo_capital'))['total']
        return total_valor_capital or 0 
    
    def get_total_valor_mora(self, obj):
        obligaciones = Obligaciones.objects.filter(cliente=obj)
        total_valor_mora = obligaciones.aggregate(total=Sum('intereses_mora'))['total']
        return total_valor_mora or 0
    
    def get_dias_mora(self, obj):
        obligaciones = Obligaciones.objects.filter(cliente=obj).order_by('fecha_vencimiento').first()
        if not obligaciones or not obligaciones.fecha_vencimiento:
            return 0  # Manejar casos donde no hay obligaciones o fecha es nula
        # Asegúrate de usar .date() para que ambos sean tipo date
        dias_mora = (datetime.now().date() - obligaciones.fecha_vencimiento).days
        return dias_mora
    
    def get_total_intereses(self,obj):
        obligaciones = Obligaciones.objects.filter(cliente=obj)
        total_intereses = obligaciones.aggregate(total=Sum('intereses_corriente'))['total']
        return total_intereses or 0
    
    def get_total_a_pagar(self, obj):
        obligaciones = Obligaciones.objects.filter(cliente=obj)
        total_a_pagar = obligaciones.aggregate(
            total=Sum('valor_vencido') + Sum('intereses_corriente') + Sum('intereses_mora') + Sum('valor_cuota')
        )['total']
        return total_a_pagar or 0