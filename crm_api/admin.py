from django.contrib import admin
from .models import *

admin.site.register([Gestiones, Usuarios, Obligaciones, ResultadosGestion, Pagos, Clientes, ClientesReferencias, Referencias, Codeudores, Campañas, CampañasUsuarios, Roles])
