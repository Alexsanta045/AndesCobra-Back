from django.contrib import admin
from .models import *

admin.site.register([Gestiones, Obligaciones, ResultadosGestion, Pagos, Clientes, Telefono_cliente, ClientesReferencias,
Referencias, Codeudores, Telefono_codeudor, Campañas, CampañasUsuarios, Roles, Chat, Tipo_identificacion, Pais, Departamento,
Ciudad, Direccion_cliente, Direccion_codeudor, Canales, Acuerdo_pago , CustomUser, Tipo_gestion ])
