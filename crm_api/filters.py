import django_filters
from .models import *
from django_filters import rest_framework as filters
from django.db.models import JSONField


class CampañasFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Campañas
        fields = ['nombre']