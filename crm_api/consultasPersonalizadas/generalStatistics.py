from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from ..models import Gestiones
import calendar

def gestiones_por_dia(request):
    # Obtenemos las gestiones de los asesores
    gestiones = Gestiones.objects.all()

    # Contamos las gestiones por día de la semana (lunes a sábado)
    gestiones_por_dia = gestiones.extra(
        select={'day_of_week': "EXTRACT(DOW FROM fecha)"}
    ).values('day_of_week').annotate(gestiones_count=Count('id'))

    # Creamos un diccionario para los días de la semana
    dias = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
    }

    # Filtramos y preparamos el formato para la respuesta
    bar_data = []
    for dia in range(7):  # Incluimos hasta Domingo para evitar datos faltantes
        # Buscamos el número de gestiones para el día de la semana
        gestiones_dia = next((item for item in gestiones_por_dia if item['day_of_week'] == dia), None)
        gestiones_count = gestiones_dia['gestiones_count'] if gestiones_dia else 0
        if dia < 6:  # Solo tomamos lunes a sábado
            bar_data.append({
                'name': dias[dia],
                'gestiones': gestiones_count,
            })

    return JsonResponse({'barData': bar_data})


def estadisticas_asesor(request):
    today = timezone.now()
    start_of_week = today - timedelta(days=today.weekday())  # Lunes de esta semana
    start_of_month = today.replace(day=1)  # Primer día del mes

    # Gestiones por día (solo hoy)
    gestiones_hoy = Gestiones.objects.filter(fecha__date=today.date()).count()

    # Gestiones por semana
    gestiones_semana = Gestiones.objects.filter(fecha__gte=start_of_week).count()

    # Gestiones por mes
    gestiones_mes = Gestiones.objects.filter(fecha__gte=start_of_month).count()

    pie_data = [
        {'name': 'Día', 'value': gestiones_hoy},
        {'name': 'Semana', 'value': gestiones_semana},
        {'name': 'Mes', 'value': gestiones_mes},
    ]

    return JsonResponse({'pieData': pie_data})
