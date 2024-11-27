from rest_framework import serializers
from ..models import *


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
        return Obligaciones.objects.filter(cliente=obj.cliente).aggregate(total=models.Sum("valor_mora"))["total"]

    def get_totalCapital(self, obj):
        # Calcula la suma del valor del capital relacionado con el cliente
        return Obligaciones.objects.filter(cliente=obj.cliente).aggregate(total=models.Sum("valor_capital"))["total"]

    def get_tasaMora(self, obj):
        # Aquí puedes agregar la fórmula para calcular la tasa de mora si se requiere
        # Ejemplo: tasa de mora = total_mora / total_capital
        total_mora = self.get_totalCartera(obj)
        total_capital = self.get_totalCapital(obj)
        return total_mora / total_capital if total_capital else 0

    def get_diasMora(self, obj):
        # Calcula los días de mora entre la fecha de vencimiento de la cuota y la fecha de obligación
        return (obj.fecha_vencimiento_cuota - obj.fecha_obligacion).days

    def get_fechaUltPago(self, obj):
        # Obtiene la fecha del último pago realizado en la obligación
        pago = Pagos.objects.filter(obligacion=obj).order_by("-fecha").first()
        return pago.fecha if pago else None

    def get_montoGestAnt(self, obj):
        """
        Obtiene el monto gestionado (total de los pagos) de la gestión anterior asociada a un cliente específico.
        """
        # Buscar la última gestión asociada al cliente, ordenada por fecha en orden descendente
        ultima_gestion = Gestiones.objects.filter(cliente=obj.cliente).order_by('-fecha').first()

        if ultima_gestion:
            # Buscar la obligación asociada a la última gestión, ordenada por fecha de obligación
            obligacion = Obligaciones.objects.filter(cliente=ultima_gestion.cliente).order_by('-fecha_obligacion').first()

            if obligacion:
                # Obtener todos los pagos realizados para esta obligación
                pagos = Pagos.objects.filter(obligacion=obligacion)

                # Sumar todos los valores de los pagos realizados
                monto_gestionado = sum(pago.valor for pago in pagos)

                return monto_gestionado
            else:
                # Si no hay obligaciones relacionadas, retornar 0
                return 0
        else:
            # Si no hay gestiones previas, retornar 0
            return 0




    def get_ultimaGestion(self, obj):
        # Obtiene la fecha de la última gestión realizada para el cliente
        gestion = Gestiones.objects.filter(cliente=obj.cliente).order_by("-fecha").first()
        return gestion.fecha if gestion else None
