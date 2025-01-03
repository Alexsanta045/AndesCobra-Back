import requests
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)