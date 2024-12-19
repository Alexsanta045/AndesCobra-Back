from django.contrib import admin
from .models import *

admin.site.register([Gestiones, Obligaciones, ResultadosGestion, Pagos, Clientes, Telefono_cliente, ClientesReferencias,
Referencias,Telefono_referencia, Codeudores, Telefono_codeudor, Campañas, CampañasUsuarios, Roles, Chat, Acuerdo_pago , CustomUser, Tipo_gestion ])
