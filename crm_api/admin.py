from django.contrib import admin
from .models import *

admin.site.register([Gestiones, Obligaciones, ResultadosGestion, Pagos, Clientes, ClientesReferencias, Referencias, Codeudores, Campañas, CampañasUsuarios, Roles])
