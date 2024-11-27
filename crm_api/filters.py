import django_filters
from .models import *
from django_filters import rest_framework as filters
from django.db.models import JSONField


class CampañasFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Campañas
        fields = ['nombre', 'id']
        
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


class ResultadosGestionFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ResultadosGestion
        fields = ['nombre']


class GestionesFilter(django_filters.FilterSet):
    cliente_nombres = django_filters.CharFilter(field_name='cliente__nombres', lookup_expr='icontains')
    resultado_nombre = django_filters.CharFilter(field_name='resultado__nombre', lookup_expr='icontains')


    class Meta:
        model = Gestiones
        fields = ['cliente_nombres','resultado_nombre']


class CodeudoresFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Codeudores
        fields = ['nombre']


class AcuerdoPagoFilter(django_filters.FilterSet):
    codigo_obligacion = django_filters.CharFilter(field_name='codigo_obligacion__codigo', lookup_expr='icontains')
    usuario_nombres = django_filters.CharFilter(field_name='usuario__nombres', lookup_expr='icontains')
    estado = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Acuerdo_pago
        fields = ['codigo_obligacion','usuario_nombres', 'estado']
