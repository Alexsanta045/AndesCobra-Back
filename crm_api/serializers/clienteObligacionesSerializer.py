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
    # Obtiene todas las obligaciones asociadas al cliente especificado en obj
    obligaciones = Obligaciones.objects.filter(cliente=obj)
    # Devuelve el conteo total de esas obligaciones
    return obligaciones.count()

def get_total_valor_capital(self, obj):
    # Filtra las obligaciones asociadas al cliente especificado en obj
    obligaciones = Obligaciones.objects.filter(cliente=obj)
    # Calcula el total del saldo de capital sumando el campo 'saldo_capital' de todas las obligaciones
    total_valor_capital = obligaciones.aggregate(total=Sum('saldo_capital'))['total']
    # Devuelve el total o 0 si no hay valores disponibles
    return total_valor_capital or 0 

def get_total_valor_mora(self, obj):
    # Filtra las obligaciones asociadas al cliente especificado en obj
    obligaciones = Obligaciones.objects.filter(cliente=obj)
    # Calcula el total de los intereses de mora sumando el campo 'intereses_mora' de todas las obligaciones
    total_valor_mora = obligaciones.aggregate(total=Sum('intereses_mora'))['total']
    # Devuelve el total o 0 si no hay valores disponibles
    return total_valor_mora or 0

def get_dias_mora(self, obj):
    # Filtra las obligaciones del cliente y ordena por la fecha de vencimiento (ascendente)
    obligaciones = Obligaciones.objects.filter(cliente=obj).order_by('fecha_vencimiento').first()
    # Verifica si no hay obligaciones o la fecha de vencimiento es nula
    if not obligaciones or not obligaciones.fecha_vencimiento:
        return 0  # Manejar casos donde no hay obligaciones o la fecha es nula
    # Calcula la diferencia en días entre la fecha actual y la fecha de vencimiento
    # Se usa .date() para asegurar que ambas fechas sean de tipo date
    dias_mora = (datetime.now().date() - obligaciones.fecha_vencimiento).days
    return dias_mora

def get_total_intereses(self, obj):
    # Filtra las obligaciones asociadas al cliente especificado en obj
    obligaciones = Obligaciones.objects.filter(cliente=obj)
    # Calcula el total de los intereses corrientes sumando el campo 'intereses_corriente' de todas las obligaciones
    total_intereses = obligaciones.aggregate(total=Sum('intereses_corriente'))['total']
    # Devuelve el total o 0 si no hay valores disponibles
    return total_intereses or 0

def get_total_a_pagar(self, obj):
    # Filtra las obligaciones asociadas al cliente especificado en obj
    obligaciones = Obligaciones.objects.filter(cliente=obj)
    # Calcula el total a pagar sumando los campos 'valor_vencido', 'intereses_corriente',
    # 'intereses_mora' y 'valor_cuota' de todas las obligaciones
    total_a_pagar = obligaciones.aggregate(
        total=Sum('valor_vencido') + Sum('intereses_corriente') + Sum('intereses_mora') + Sum('valor_cuota')
    )['total']
    # Devuelve el total o 0 si no hay valores disponibles
    return total_a_pagar or 0
