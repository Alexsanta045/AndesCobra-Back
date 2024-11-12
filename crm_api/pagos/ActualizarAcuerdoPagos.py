from rest_framework.response import Response
from datetime import datetime, timedelta
from ..models import Acuerdo_pago
from rest_framework import status

def actualizarAcuerdoPago(self, obligacion, fecha):
    try:
        fecha_pago = datetime.strptime(fecha, '%Y-%m-%d').date()  # Convierte la fecha de cadena a datetime.date
    except ValueError:
        return Response({"error": "El formato de la fecha es inválido, debe ser YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

    # Define el rango de fechas: desde hace 30 días hasta la fecha de pago
    fecha_inicio_rango = fecha_pago - timedelta(days=5)
    fecha_fin_rango = fecha_pago + timedelta(days=14)

    # Filtra el acuerdo de pago en el rango de fechas
    acuerdo_pago = Acuerdo_pago.objects.filter(
        codigo_obligacion=obligacion,
        fecha_pago__range=(fecha_inicio_rango, fecha_fin_rango)
    ).first()

    print(acuerdo_pago)

    if acuerdo_pago:
        if fecha_pago <= acuerdo_pago.fecha_pago:
            acuerdo_pago.cumplimiento = True
            acuerdo_pago.save()
            return Response({"message": "Acuerdo de pago actualizado"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "No se encontró el acuerdo de pago"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "No se requirió actualización"}, status=status.HTTP_200_OK)