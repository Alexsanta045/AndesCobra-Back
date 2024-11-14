import django_filters
from .models import *
from django_filters import rest_framework as filters
from django.db.models import JSONField


class CampañasFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Campañas
        fields = ['nombre']
        
class ClientesFilter(django_filters.FilterSet):
    nombres = django_filters.CharFilter(lookup_expr='icontains')
    apellidos = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Clientes
        fields = ['nit', 'nombres', 'apellidos', 'email']
        
class ReferenciasFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    nit = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Referencias
        fields = ['nit', 'nombre']
        
class ObligacionesFilter(django_filters.FilterSet):
    campaña = django_filters.CharFilter(field_name='campaña__nombre', lookup_expr='icontains')
    cliente = django_filters.CharFilter()

    class Meta:
        model = Obligaciones
        fields = ['codigo', 'campaña', 'cliente', 'fecha_obligacion', 'fecha_vencimiento_cuota', 'valor_capital', 'valor_mora']

class PagosFilter(django_filters.FilterSet):

    class Meta:
        model = Pagos
        fields = ['obligacion', 'valor', 'fecha']