from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Pagos, Acuerdo_pago
from datetime import datetime, timedelta

class ActualizarAcuerdosPagoView(APIView):
    def get(self, request, *args, **kwargs):

        ayer = datetime.today().date() - timedelta(days=1)
        fecha_vencida = ayer - timedelta(days=6)
        
        pagos = Pagos.objects.filter(fecha=ayer)
        acuerdos = Acuerdo_pago.objects.filter(fecha_pago=fecha_vencida)

        for pago in pagos:
            acuerdo_pago = Acuerdo_pago.objects.filter(codigo_obligacion=pago.obligacion).first()

            if acuerdo_pago:
                if pago.fecha <= acuerdo_pago.fecha_pago + timedelta(days=5) and pago.valor == acuerdo_pago.valor_cuota:
                    acuerdo_pago.estado = "Cumplido"  
                    acuerdo_pago.save()
                elif pago.fecha <= acuerdo_pago.fecha_pago + timedelta(days=5) and pago.valor < acuerdo_pago.valor_cuota:
                    acuerdo_pago.estado = "Cumplido Parcialmente"  
                    acuerdo_pago.save()
                elif pago.fecha > acuerdo_pago.fecha_pago + timedelta(days=5) and pago.valor == acuerdo_pago.valor_cuota:
                    acuerdo_pago.estado = "Incumplido pero pagado"   
                    acuerdo_pago.save()
                elif pago.fecha > acuerdo_pago.fecha_pago + timedelta(days=5) and pago.valor < acuerdo_pago.valor_cuota:
                    acuerdo_pago.estado = "Incumplido y pagado parcialmente"   
                    acuerdo_pago.save()

        for acuerdo in acuerdos:
            pago = Pagos.objects.filter(obligacion=acuerdo.codigo_obligacion).first()
            
            if not pago:
                acuerdo.estado = "Incumplido"
                acuerdo.save()

        # Retornar respuesta
        return Response({"mensaje": "Acuerdos de pago actualizados"}, status=status.HTTP_200_OK)
