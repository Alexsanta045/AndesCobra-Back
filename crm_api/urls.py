from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .serializers import *


# router = DefaultRouter()
# router.register(r'Gestiones', GestionesSerializer, basename='Gestiones') 


# utlpatterns = [
#     path('', include(router.urls)),
# ]