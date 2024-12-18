from ..models import Clientes, Telefono_cliente, Codeudores, Telefono_codeudor, Referencias, Telefono_referencia, ClientesReferencias, Obligaciones, Campañas
import pandas as pd

def asignar_o_none(valor):
    return valor if not pd.isna(valor) else None


def ingresar_datos(df, campaña):
    cantObligacionesRepetidas = 0
    for _, fila in df.iterrows():
        cliente_instancia, _ = Clientes.objects.get_or_create(
            nit=fila['nit'],
            defaults={
                'nombres' : fila['nombre'],
                'tipo_id' : asignar_o_none(fila['tipo_identificacion']),
                'apellidos' : asignar_o_none(fila['apellidos']),
                'email' : asignar_o_none(fila['email']),
                'direccion' : asignar_o_none(fila['direccion']),
                'ciudad' : asignar_o_none(fila['ciudad']),
                'fecha_nacimiento' : asignar_o_none(fila['fecha_nacimiento']),
                'fecha_ingreso' : asignar_o_none(fila['fecha_ingreso']),
                'actividad_economica' : asignar_o_none(fila['actividad_economica']),
                'genero' : asignar_o_none(fila['genero']),
                'empresa' : asignar_o_none(fila['empresa']),
                'cantidad_hijos' : asignar_o_none(fila['cantidad_hijos']),
                'estrato' : asignar_o_none(fila['estrato']),
                'calificacion_cliente' : asignar_o_none(fila['calificacion_cliente']),
                'tipo_persona' : asignar_o_none(fila['tipo_persona']),
                'profesion' : asignar_o_none(fila['profesion']),
                'estado_fraude' : asignar_o_none(fila['estado_fraude']),
                'calificacion_buro' : asignar_o_none(fila['calificacion_buro']),
                'codigo_dane' : asignar_o_none(fila['codigo_dane_cliente']),
                # campos_opcionales = asignar_o_none()
            }
        )
        for i in range(10):
            telefono = fila.get(f'telefono_{ i + 1}')
            if telefono and not Telefono_cliente.objects.filter(numero=telefono).exists():
                Telefono_cliente.objects.create(numero=telefono, cliente=cliente_instancia)
        

        if pd.isna(fila['nit_codeudor']) or pd.isna(fila['nombre_codeudor']) or pd.isna(fila['telefono_codeudor']): 
            codeudor_instancia = None
        else:
            codeudor_instancia, creado = Codeudores.objects.get_or_create(
                nit=fila['nit_codeudor'],
                defaults={
                    'nombres' : fila['nombre_codeudor'],
                    'email' : asignar_o_none(fila['email_codeudor']),
                    'direccion' : asignar_o_none(fila['direccion_codeudor']),
                    'ciudad' : asignar_o_none(fila['ciudad_codeudor']),
                    'codigo_dane' : asignar_o_none(fila['codigo_dane_codeudor']),
                    # campos_opcionales = asignar_o_none(fila['']),
                }
            )
            if creado:
                Telefono_codeudor.objects.get_or_create(numero=fila['telefono_codeudor'], codeudor=codeudor_instancia)

        campaña_instancia = Campañas.objects.get(id=campaña)
        if Obligaciones.objects.filter(codigo_obligacion=fila['numero_obligacion']).exists():
            cantObligacionesRepetidas += 1
        else: Obligaciones.objects.create(
            codigo_obligacion = asignar_o_none(fila['numero_obligacion']),
            campaña = campaña_instancia,
            cliente = cliente_instancia,
            codeudor = codeudor_instancia,
            valor_vencido  = fila['valor_vencido'],
            fecha_obligacion = asignar_o_none(fila['fecha_obligacion']),
            fecha_vencimiento = asignar_o_none(fila['fecha_vencimiento']),
            valor_obligacion = asignar_o_none(fila['valor_obligacion']),
            valor_cuota = asignar_o_none(fila['valor_cuota']),
            saldo_capital = asignar_o_none(fila['saldo_capital']),
            saldo_total = asignar_o_none(fila['saldo_total']),
            tipo_producto = asignar_o_none(fila['tipo_de_producto']),
            dias_mora = asignar_o_none(fila['dias_de_mora']),
            valor_ultimo_pago = asignar_o_none(fila['valor_ultimo_pago']),
            intereses_corriente = asignar_o_none(fila['intereses_corrientes']),
            intereses_mora = asignar_o_none(fila['intereses_mora']),
            plazo = asignar_o_none(fila['plazo']),
            calificacion_obligacion = asignar_o_none(fila['calificacion_obligacion']),
            ciclo = asignar_o_none(fila['ciclo']),
            etapa_actual_obligacion = asignar_o_none(fila['etapa_actual_obligacion']),
            fecha_inactivacion = asignar_o_none(fila['fecha_inactivacion']),
            estado_operacional = asignar_o_none(fila['estado_operacional']),
            dias_mora_inicial = asignar_o_none(fila['dias_mora_inicial']),
            rango_mora_inicial = asignar_o_none(fila['rango_mora_inicial']),
            rango_mora_actual = asignar_o_none(fila['rango_mora_actual']),
            fecha_inicio_mora = asignar_o_none(fila['fecha_inicio_mora']),
            tasa_interes = asignar_o_none(fila['tasa_interes']),
            porc_gastos_cobranza = asignar_o_none(fila['porc_gastos_cobranza']),
            valor_gastos_cobranza = asignar_o_none(fila['valor_gastos_cobranza']),
            valor_iva_gastos = asignar_o_none(fila['valor_iva_gastos']),
            valor_otros_conceptos = asignar_o_none(fila['valor_otros_conceptos']),
            fecha_castigo = asignar_o_none(fila['fecha_castigo']),
            cuotas_vencidas = asignar_o_none(fila['cuotas_vencidas']),
            cuotas_pendientes = asignar_o_none(fila['coutas_pendientes']),
            cuotas_pagadas = asignar_o_none(fila['cuotas_pagadas']),
            libranza = asignar_o_none(fila['libranza']),
            nit_empresa = asignar_o_none(fila['nit_empresa']),
            sucursal = asignar_o_none(fila['sucursal']),
            regional = asignar_o_none(fila['regional']),
            puntaje_credito = asignar_o_none(fila['puntaje_credito']),
            puntaje_comportamiento = asignar_o_none(fila['puntaje_comportamiento']),
            marca_especial = asignar_o_none(fila['marca_especial']),
            fecha_corte_obligacion = asignar_o_none(fila['fecha_corte_obligacion']),
            fecha_facturacion_obligacion = asignar_o_none(fila['fecha_facturacion_obligacion']),
                # campos_opcionales = asignar_o_none(),
        )
        referencia_instancia = None
        if not pd.isna(fila['nit_referencia']) or not pd.isna(fila['nombre_referencia']) or not pd.isna(fila['telefono_referencia']):
            referencia_instancia, _ = Referencias.objects.get_or_create(
                nit=fila['nit_referencia'],
                defaults={
                'nombres' : fila['nombre_referencia'],
                'email' : asignar_o_none(fila['email_referencia']),
                'direccion' : asignar_o_none(fila['direccion_referencia']),
                'ciudad' : asignar_o_none(fila['ciudad_referencia']),
                'codigo_dane' : asignar_o_none(fila['codigo_dane_referencia']),
                # campos_opcionales = asignar_o_none(fila['']),
                }
            )
            if not Telefono_referencia.objects.filter(telefono=fila['telefono_referencia']).exists():
                Telefono_referencia.objects.create(numero=fila['telefono_referencia'], referencia=referencia_instancia)

        if referencia_instancia and not ClientesReferencias.objects.filter(cliente_id=cliente_instancia, referencia_id=referencia_instancia).exists():
            ClientesReferencias.objects.create(cliente_id=cliente_instancia,referencia_id=referencia_instancia)


        
    print(f'Cantidad de obligaciones repetidas ---> {cantObligacionesRepetidas}')

























