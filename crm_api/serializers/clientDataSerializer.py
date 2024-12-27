from rest_framework import serializers
from ..models import *
from collections import defaultdict
from datetime import datetime


class ClientDataSerializer(serializers.Serializer):
    obligacion = serializers.CharField(source="codigo")
    nroCliente = serializers.CharField(source="cliente.nit")
    nombreCliente = serializers.SerializerMethodField()
    telefonos = serializers.SerializerMethodField()
    cartera = serializers.CharField(source="campaña.nombre")
    totalCartera = serializers.SerializerMethodField()
    totalCapital = serializers.SerializerMethodField()
    tasaMora = serializers.SerializerMethodField()
    diasMora = serializers.SerializerMethodField()
    fechaUltPago = serializers.SerializerMethodField()
    montoGestAnt = serializers.SerializerMethodField()
    ultimaGestion = serializers.SerializerMethodField()

    def get_nombreCliente(self, obj):
        # Retorna el nombre completo del cliente
        return f"{obj.cliente.nombres} {obj.cliente.apellidos}"

    def get_telefonos(self, obj):
        # Obtiene los números de teléfono asociados al cliente
        telefonos = Telefono_cliente.objects.filter(cliente=obj.cliente).values_list("numero", flat=True)
        return list(telefonos)

    def get_totalCartera(self, obj):
        # Calcula la suma del valor de la mora relacionada con el cliente
        total_mora = Obligaciones.objects.filter(cliente=obj.cliente).aggregate(total=models.Sum("intereses_mora"))["total"] or 0
        # Obtiene el monto total de pagos gestionados que han sido aplicados a esta cartera
        total_pagos = self.get_montoGestAnt(obj)
        # Asegurarse de que el valor no sea negativo
        total_cartera = total_mora - total_pagos
        return max(total_cartera, 0)  # Si el valor es negativo, se ajusta a 0

    def get_totalCapital(self, obj):
        # Calcula el capital total después de descontar los pagos realizados
        total_capital = Obligaciones.objects.filter(cliente=obj.cliente).aggregate(total=models.Sum("saldo_capital"))["total"] or 0
        total_pagos = self.get_montoGestAnt(obj)
        # Asegurarse de que el valor no sea negativo
        total_capital_final = total_capital - total_pagos
        return max(total_capital_final, 0)  # Si el valor es negativo, se ajusta a 0

    def get_tasaMora(self, obj):
        # Calcula la tasa de mora considerando los pagos realizados
        total_mora = self.get_totalCartera(obj)
        total_capital = self.get_totalCapital(obj)
        return total_mora / total_capital if total_capital else 0

    def get_diasMora(self, obj):
        # Calcula los días de mora entre la fecha de vencimiento de la cuota y la fecha de obligación
        # Asumir que 'fecha_vencimiento' es la correcta en 'Obligaciones'
        if obj.fecha_vencimiento:
            return (datetime.now().date() - obj.fecha_vencimiento).days
        return 0

    def get_fechaUltPago(self, obj):
        # Obtiene la fecha del último pago realizado en la obligación
        pago = Pagos.objects.filter(obligacion=obj).order_by("-fecha").first()
        return pago.fecha if pago else None

    def get_montoGestAnt(self, obj):
        """
        Obtiene el monto total gestionado (total de los pagos) de la última gestión asociada a un cliente específico.
        Si no hay gestión, se calcula el monto de los pagos directamente de la obligación.
        """
        # Buscar la última gestión asociada al cliente, ordenada por fecha en orden descendente
        ultima_gestion = Gestiones.objects.filter(cliente=obj.cliente).order_by('-fecha').first()

        if ultima_gestion:
            # Buscar la obligación asociada a la última gestión
            obligacion = Obligaciones.objects.filter(cliente=ultima_gestion.cliente).order_by('-fecha_obligacion').first()
        else:
            # Si no hay gestión, simplemente buscar la obligación más reciente
            obligacion = Obligaciones.objects.filter(cliente=obj.cliente).order_by('-fecha_obligacion').first()

        if obligacion:
            # Filtrar los pagos relacionados con esta obligación
            pagos = Pagos.objects.filter(obligacion=obligacion).order_by('fecha')

            # Sumar todos los valores de los pagos realizados en esta obligación
            monto_gestionado = sum(pago.valor for pago in pagos)

            # Devolver el monto total de los pagos gestionados
            return monto_gestionado
        else:
            return 0

    def get_ultimaGestion(self, obj):
        # Obtiene la fecha de la última gestión realizada para el cliente
        gestion = Gestiones.objects.filter(cliente=obj.cliente).order_by("-fecha").first()
        return gestion.fecha if gestion else None
