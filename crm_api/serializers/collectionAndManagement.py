from rest_framework import serializers
from ..models import *
from collections import defaultdict

class CollectionAndManagement(serializers.Serializer):
    campaña = serializers.CharField(source='nombre')  # Nombre de la campaña
    recaudo = serializers.SerializerMethodField()  # Total de recaudo por fecha
    fecha = serializers.SerializerMethodField()  # Fecha de cada recaudo
    total_recaudo = serializers.SerializerMethodField()  # Total de recaudo de todos los pagos

    def get_camapaña(self, obj):
        return obj.nombre

    def get_recaudo(self, obj):
        # Filtrar los pagos relacionados con la campaña y agrupar por fecha
        pagos = Pagos.objects.filter(obligacion__campaña=obj).order_by('fecha')

        # Crear un diccionario para agrupar pagos por fecha
        recaudos = defaultdict(float)  # Usamos defaultdict para evitar errores de clave no existente

        # Agrupar los pagos por fecha
        for pago in pagos:
            recaudos[pago.fecha] += pago.valor  # Sumar el valor de los pagos por fecha

        # Convertir los datos agrupados en una lista para mostrarlo
        recaudos_por_fecha = [{"fecha": str(fecha), "recaudo": recaudo} for fecha, recaudo in recaudos.items()]
        return recaudos_por_fecha

    def get_fecha(self, obj):
        # Este campo es necesario para devolver la fecha de cada recaudo agrupado.
        pagos = Pagos.objects.filter(obligacion__campaña=obj).order_by('fecha')

        # Si hay pagos, devolvemos la fecha del primer recaudo
        if pagos:
            return pagos.first().fecha
        return None  # Retorna None si no hay pagos

    def get_total_recaudo(self, obj):
        # Filtrar los pagos relacionados con la campaña
        pagos = Pagos.objects.filter(obligacion__campaña=obj)
        
        # Calcular el total de recaudo sumando los valores de todos los pagos
        total_recaudo = sum(pago.valor for pago in pagos)

        # Retornar el total de recaudo
        return total_recaudo
