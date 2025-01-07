from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Pagos, Acuerdo_pago
from datetime import datetime, timedelta

class ActualizarAcuerdosPagoView(APIView):
    def get(self, request, *args, **kwargs):
        # Calcular la fecha de ayer y la fecha de seis días atrás
        ayer = datetime.today().date() - timedelta(days=1)
        fecha_vencida = ayer - timedelta(days=6)
        
        # Obtener los pagos realizados ayer
        pagos = Pagos.objects.filter(fecha=ayer)
        # Obtener los acuerdos de pago cuya fecha de pago venció hace seis días
        acuerdos = Acuerdo_pago.objects.filter(fecha_pago=fecha_vencida)

        # Iterar sobre los pagos realizados ayer
        for pago in pagos:
            # Buscar el acuerdo de pago relacionado con la obligación del pago
            acuerdo_pago = Acuerdo_pago.objects.filter(codigo_obligacion=pago.obligacion).first()

            if acuerdo_pago:
                # Verificar condiciones de cumplimiento de pago según fecha y valor
                if pago.fecha <= acuerdo_pago.fecha_pago + timedelta(days=5) and pago.valor == acuerdo_pago.valor_cuota:
                    acuerdo_pago.estado = "Cumplido"  # Pago completo dentro del rango permitido
                    acuerdo_pago.save()
                elif pago.fecha <= acuerdo_pago.fecha_pago + timedelta(days=5) and pago.valor < acuerdo_pago.valor_cuota:
                    acuerdo_pago.estado = "Cumplido Parcialmente"  # Pago parcial dentro del rango permitido
                    acuerdo_pago.save()
                elif pago.fecha > acuerdo_pago.fecha_pago + timedelta(days=5) and pago.valor == acuerdo_pago.valor_cuota:
                    acuerdo_pago.estado = "Incumplido pero pagado"  # Pago completo fuera del rango permitido
                    acuerdo_pago.save()
                elif pago.fecha > acuerdo_pago.fecha_pago + timedelta(days=5) and pago.valor < acuerdo_pago.valor_cuota:
                    acuerdo_pago.estado = "Incumplido y pagado parcialmente"  # Pago parcial fuera del rango permitido
                    acuerdo_pago.save()

        # Iterar sobre acuerdos de pago que vencieron hace seis días
        for acuerdo in acuerdos:
            # Verificar si no existe un pago relacionado con el acuerdo
            pago = Pagos.objects.filter(obligacion=acuerdo.codigo_obligacion).first()
            
            if not pago:
                acuerdo.estado = "Incumplido"  # Marcar acuerdo como incumplido si no hay pago registrado
                acuerdo.save()

        # Retornar respuesta indicando que los acuerdos de pago fueron actualizados
        return Response({"mensaje": "Acuerdos de pago actualizados"}, status=status.HTTP_200_OK)
