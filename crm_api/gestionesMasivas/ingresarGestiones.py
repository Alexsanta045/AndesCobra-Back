from ..models import Gestiones, Clientes, Tipo_gestion, ResultadosGestion, CustomUser, Roles, Telefono_cliente, Campañas
import pandas as pd


def asigna_o_none(valor):
    return valor if not pd.isna(valor) else None

def obtener_asesor_externo(rol_instancia):
    return CustomUser.objects.get_or_create(
        username='Asesor externo',
        defaults={
            'email': 'asesorExterno@gmail.com',
            'password': 'asesorExterno',
            'role_id': rol_instancia.id
        }
    )

def ingresar_gestiones(id_campaña, df):

    rol_instancia = Roles.objects.get(nombre='advisor')

    for _, fila in df.iterrows():
        asesor_externo_instancia = None

        if pd.isna(fila['codigo_asesor']):
            asesor_externo_instancia, usuario_creado = obtener_asesor_externo(rol_instancia)
            # asesor_externo_instancia, usuario_creado = CustomUser.objects.get_or_create(
            #     username = 'Asesor externo',
            #     defaults={
            #         'email': 'asesorExterno@gmail.com',
            #         'password': 'asesorExterno',
            #         'role_id': rol_instancia
            #     }
            # )
        else:
            try:
                asesor_instancia = CustomUser.objects.get(id=fila['codigo_asesor'])
            except:
                asesor_externo_instancia, usuario_creado = obtener_asesor_externo(rol_instancia)

        
        cliente_intancia, cliente_creado = Clientes.objects.get_or_create(
            nit = fila['nit_cliente'],
            defaults={
                'nombres': fila['nombres_cliente'],
                'tipo_id': asigna_o_none(fila['tipo_id']),
                'apellidos': asigna_o_none(fila['apellidos_cliente']),
                'email': asigna_o_none(fila['email_cliente']),
                'direccion': asigna_o_none(fila['direccion_cliente']),
                'ciudad': asigna_o_none(fila['ciudad_cliente']),
                'genero': asigna_o_none(fila['genero_cliente'])
            }
        )

        telefono_intancia, telefono_creado = Telefono_cliente.objects.get_or_create(
            numero = fila['telefono_cliente'],
            defaults = {    
                'cliente':  cliente_intancia     
            } 
        )

        if fila['resultado_gestion'].lower() == 'compromiso de pago':
            efectividad = True
        else:
            efectividad = False

        campaña_instancia = Campañas.objects.get(id=id_campaña)

        resultado_gestion_instancia, resultado_gestion_creado = ResultadosGestion.objects.get_or_create(
            codigo = fila['codigo_resultado_gestion'], campaña = campaña_instancia,
            defaults = {
                'nombre': fila['resultado_gestion'],
                'efectividad': efectividad,
                'campaña': campaña_instancia
            }
        )

        if pd.isna(fila['tipo_gestion']):
            tipo_gestion = 'llamada'
        else:
            tipo_gestion = fila['tipo_gestion']


        tipo_gestion_instancia, tipo_gestion_credo = Tipo_gestion.objects.get_or_create(nombre = tipo_gestion)

        Gestiones.objects.create(
            usuario = asesor_externo_instancia if asesor_externo_instancia else asesor_instancia,
            cliente = cliente_intancia,
            resultado = resultado_gestion_instancia,
            comentarios = asigna_o_none(fila['comentarios_gestion']),
            tipo_gestion = tipo_gestion_instancia
        )
