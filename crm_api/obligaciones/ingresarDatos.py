from ..models import Clientes, Telefono_cliente, Codeudores, Telefono_codeudor, Referencias, Telefono_referencia, ClientesReferencias, Obligaciones, Campañas
import pandas as pd



def asignar_o_none(valor):
    return valor if not pd.isna(valor) else None

def ingresar_datos(df, campaña):
    for index, fila in df.iterrows():
        #ingresa el cliente
        if Clientes.objects.filter(nit=fila['nit']).exists():
            print(f"El cliente con NIT {fila['nit']} ya existe.")
            
        else:
            clientes_data = Clientes(
                nit = fila['nit'],
                nombres = fila['nombre'],
                tipo_id = asignar_o_none(fila['tipo_identificacion']),
                apellidos = asignar_o_none(fila['apellidos']),
                email = asignar_o_none(fila['email']),
                direccion = asignar_o_none(fila['direccion']),
                ciudad = asignar_o_none(fila['ciudad']),
                fecha_nacimiento = asignar_o_none(fila['fecha_nacimiento']),
                fecha_ingreso = asignar_o_none(fila['fecha_ingreso']),
                actividad_economica = asignar_o_none(fila['actividad_economica']),
                genero = asignar_o_none(fila['genero']),
                empresa = asignar_o_none(fila['empresa']),
                cantidad_hijos = asignar_o_none(fila['cantidad_hijos']),
                estrato = asignar_o_none(fila['estrato']),
                calificacion_cliente = asignar_o_none(fila['calificacion_cliente']),
                tipo_persona = asignar_o_none(fila['tipo_persona']),
                profesion = asignar_o_none(fila['profesion']),
                estado_fraude = asignar_o_none(fila['estado_fraude']),
                calificacion_buro = asignar_o_none(fila['calificacion_buro']),
                codigo_dane = asignar_o_none(fila['codigo_dane_cliente']),
                # campos_opcionales = asignar_o_none()     
            )
            clientes_data.save() 

            #ingresa el telefono del cliente
       
            cliente_instancia = Clientes.objects.get(nit=fila['nit'])
            telefonos_clientes_data = Telefono_cliente(
                numero = fila['telefono'],
                cliente = cliente_instancia
            )
            telefonos_clientes_data.save()
           

        #se ingresa el codeudor
        if pd.isna(fila['nit_codeudor']) or pd.isna(fila['nombre_codeudor']) or pd.isna(fila['telefono_codeudor']):
            print('faltan datos del codeudor')
            ingresar_codeudor = False

        else:
            ingresar_codeudor = True
            codeudores_data = Codeudores(
                nit = fila['nit_codeudor'],
                nombres = fila['nombre_codeudor'],
                email = asignar_o_none(fila['email_codeudor']),
                direccion = asignar_o_none(fila['direccion_codeudor']),
                ciudad = asignar_o_none(fila['ciudad_codeudor']),
                codigo_dane = asignar_o_none(fila['codigo_dane_codeudor']),
                # campos_opcionales = asignar_o_none(fila['']),
            )
            codeudores_data.save()

            #se agrega el telefono del codeudor
            codeudor_instancia = Codeudores.objects.get(nit=fila['nit_codeudor'])
            telefonos_codeudores_data = Telefono_codeudor(
                numero = fila['telefono_codeudor'],
                codeudor = codeudor_instancia,  
            )
            telefonos_codeudores_data.save()

        #ingresar obligacion
        try:
            campaña_instancia = Campañas.objects.get(id=campaña)
            obligaciones_data = Obligaciones(
                codigo_obligacion = asignar_o_none(fila['numero_obligacion']),
                campaña = campaña_instancia,
                cliente = cliente_instancia,
                codeudor = codeudor_instancia if ingresar_codeudor else None,
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
            obligaciones_data.save()
        except Exception as e:
            print(f'error {e}')

        #ingresar referencia
        if pd.isna(fila['nit_referencia']) or pd.isna(fila['nombre_referencia']) or pd.isna(fila['telefono_referencia']):
            print("no estan todos los datos de la referencia")

        else:
            referencias_data = Referencias(
                nit = fila['nit_referencia'],
                nombres = fila['nombre_referencia'],
                email = asignar_o_none(fila['email_referencia']),
                direccion = asignar_o_none(fila['direccion_referencia']),
                ciudad = asignar_o_none(fila['ciudad_referencia']),
                codigo_dane = asignar_o_none(fila['codigo_dane_referencia']),
                # campos_opcionales = asignar_o_none(fila['']),
            )
            referencias_data.save()

            # ingresar telefono referencia
            referencia_instancia = Referencias.objects.get(nit=fila['nit_referencia'])
            telefonos_referencias_data = Telefono_referencia(
                numero = fila['telefono_referencia'],
                referencia = referencia_instancia,
            )
            telefonos_referencias_data.save()

            # ingresar referencia cliente
            clientes_referencias_data = ClientesReferencias(
                cliente_id = cliente_instancia,
                referencia_id = referencia_instancia,
            )
            clientes_referencias_data.save()






















# from ..models import Clientes, Telefono_cliente, Codeudores, Telefono_codeudor, Referencias, Telefono_referencia, ClientesReferencias, Obligaciones
# import pandas as pd



# def asignar_o_none(valor):
#     return valor if not pd.isna(valor) else None

# def ingresar_clientes(df):
#     for index, fila in df.iterrows():

#         if Clientes.objects.filter(nit=fila['nit']).exists():
#             print(f"El cliente con NIT {fila['nit']} ya existe.")
#             continue

#         clientes_data = Clientes(
#             nit = fila['nit'],
#             nombres = fila['nombre'],
#             tipo_id = asignar_o_none(fila['tipo_identificacion']),
#             apellidos = asignar_o_none(fila['apellidos']),
#             email = asignar_o_none(fila['email']),
#             direccion = asignar_o_none(fila['direccion']),
#             ciudad = asignar_o_none(fila['ciudad']),
#             fecha_nacimiento = asignar_o_none(fila['fecha_nacimiento']),
#             fecha_ingreso = asignar_o_none(fila['fecha_ingreso']),
#             actividad_economica = asignar_o_none(fila['actividad_economica']),
#             genero = asignar_o_none(fila['genero']),
#             empresa = asignar_o_none(fila['empresa']),
#             cantidad_hijos = asignar_o_none(fila['cantidad_hijos']),
#             estrato = asignar_o_none(fila['estrato']),
#             califiacion_cliente = asignar_o_none(fila['calificacion_cliente']),
#             tipo_persona = asignar_o_none(fila['tipo_persona']),
#             profesion = asignar_o_none(fila['profesion']),
#             estado_fraude = asignar_o_none(fila['estado_fraude']),
#             calificacion_buro = asignar_o_none(fila['calificacion_buro']),
#             codigo_dane = asignar_o_none(fila['codigo_dane_cliente']),
#             # campos_opcionales = asignar_o_none()     
#         )

#         clientes_data.save() 


# def ingresar_telefono_cliente(df):
#     for index, fila in df.iterrows():
#         telefonos_clientes_data = Telefono_cliente(
#             numero = fila['telefono'],
#             cliente = fila['nit'],
#         )

#         telefonos_clientes_data.save()


# def ingresar_obligacion(df, campaña):
#     for index, fila in df.iterrows():
#         obligaciones_data = Obligaciones(
#             codigo_obligacion = asignar_o_none('numero_obligacion'),
#             campaña = campaña,
#             cliente = fila['nit'],
#             valor_vencido  = fila['valor_vencido '],
#             fecha_obligacion = asignar_o_none(fila['fecha_obligacion']),
#             fecha_vencimiento = asignar_o_none(fila['fecha_vencimiento']),
#             valor_obligacion = asignar_o_none(fila['valor_obligacion']),
#             valor_cuota = asignar_o_none(fila['valor_cuota']),
#             saldo_capital = asignar_o_none(fila['saldo_capital']),
#             saldo_total = asignar_o_none(fila['saldo_total']),
#             tipo_producto = asignar_o_none(fila['tipo_de_producto']),
#             dias_mora = asignar_o_none(fila['dias_de_mora']),
#             valor_ultimo_pago = asignar_o_none(fila['valor_ultimo_pago']),
#             intereses_corriente = asignar_o_none(fila['intereses_corrientes']),
#             intereses_mora = asignar_o_none(fila['intereses_mora']),
#             plazo = asignar_o_none(fila['plazo']),
#             calificacion_obligacion = asignar_o_none(fila['calificacion_obligacion']),
#             ciclo = asignar_o_none(fila['ciclo']),
#             etapa_actual_obligacion = asignar_o_none(fila['etapa_actual_obligacion']),
#             fecha_inactivacion = asignar_o_none(fila['fecha_inactivacion']),
#             estado_operacional = asignar_o_none(fila['estado_operacional']),
#             dias_mora_inicial = asignar_o_none(fila['dias_mora_inicial']),
#             rango_mora_inicial = asignar_o_none(fila['rango_mora_inicial']),
#             rango_mora_actual = asignar_o_none(fila['rango_mora_actual']),
#             fecha_inicio_mora = asignar_o_none(fila['fecha_inicio_mora']),
#             tasa_interes = asignar_o_none(fila['tasa_interes']),
#             porc_gastos_cobranza = asignar_o_none(fila['porc_gastos_cobranza']),
#             valor_gastos_cobranza = asignar_o_none(fila['valor_gastos_cobranza']),
#             valor_iva_gastos = asignar_o_none(fila['valor_iva_gastos']),
#             valor_otros_conceptos = asignar_o_none(fila['valor_otros_conceptos']),
#             fecha_castigo = asignar_o_none(fila['fecha_castigo']),
#             cuotas_vencidas = asignar_o_none(fila['cuotas_vencidas']),
#             cuotas_pendientes = asignar_o_none(fila['coutas_pendientes']),
#             cuotas_pagadas = asignar_o_none(fila['cuotas_pagadas']),
#             libranza = asignar_o_none(fila['libranza']),
#             nit_empresa = asignar_o_none(fila['nit_empresa']),
#             sucursal = asignar_o_none(fila['sucursal']),
#             regional = asignar_o_none(fila['regional']),
#             puntaje_credito = asignar_o_none(fila['puntaje_credito']),
#             puntaje_comportamiento = asignar_o_none(fila['puntaje_comportamiento']),
#             marca_especial = asignar_o_none(fila['marca_especial']),
#             fecha_corte_obligacion = asignar_o_none(fila['fecha_corte_obligacion']),
#             fecha_facturacion_obligacion = asignar_o_none(fila['fecha_facturacion_obligacion']),
#             # campos_opcionales = asignar_o_none(),
#         )

#         obligaciones_data.save()

# def ingresar_codeudores(df):
#     for index, fila in df.iterrows():

#         if pd.isna(fila['nit_codeudor']) or pd.isna(fila['nombre_codeudor']) or pd.isna(fila['telefono_codeudor']):

#             # Si falta alguno de los campos obligatorios, omitir la fila
#             print(f"faltan datos obligatorios (nit_codeudor o nombre_codeudor)en la fila: {index}")
#             continue  
    
#         if pd.isna(fila['numero_obligacion']):
#                 obligacion = Obligaciones.objects.get(codigo_obligacion=fila['numero_obligacion'])
#         else:
#                 obligacion = Obligaciones.objects.get(cliente=fila['nit'], valor_vencido=fila['valor_vencido'])

#         codeudores_data = Codeudores(
#             nit = fila['nit_codeudor'],
#             nombres = fila['nombre_codeudor'],
#             obligacion = obligacion,
#             email = asignar_o_none(fila['email_codeudor']),
#             direccion = asignar_o_none(fila['direccion_codeudor']),
#             ciudad = asignar_o_none(fila['ciudad_codeudor']),
#             codigo_dane = asignar_o_none(fila['codigo_dane_codeudor']),
#                 # campos_opcionales = asignar_o_none(fila['']),
#         )

#         codeudores_data.save()


# def ingresar_telefonos_codeudores(df):

#     for index, fila in df.iterrows():

#         if pd.isna(fila['nit_codeudor']) or pd.isna(fila['nombre_codeudor']) or pd.isna(fila['telefono_codeudor']):
#             continue

#         telefonos_codeudores_data = Telefono_codeudor(
#             numero = fila['telefono_codeudor'],
#             codeudor = fila['nit_codeudor'],  
#         )

#         telefonos_codeudores_data.save()


# def ingresar_referencias(df):
#     for index, fila in df.iterrows():

#         if pd.isna(fila['nit_referencia']) or pd.isna(fila['nombre_referencia']) or pd.isna(fila['telefono_referencia']):
#             continue

#         referencias_data = Referencias(
#             nit = fila['nit_referencia'],
#             nombres = fila['nombre_referencia'],
#             email = asignar_o_none(fila['email_referencia']),
#             direccion = asignar_o_none(fila['direccion_referencia']),
#             ciudad = asignar_o_none(fila['ciudad_referencia']),
#             codigo_dane = asignar_o_none(fila['codigo_dane_referencia']),
#             # campos_opcionales = asignar_o_none(fila['']),
#         )

#     referencias_data.save()


# def ingresar_telefonos_referencias(df):
#     for index, fila in df.iterrows():

#         if pd.isna(fila['nit_referencia']) or pd.isna(fila['nombre_referencia']) or pd.isna(fila['telefono_referencia']):
#             continue
        
#         telefonos_referencias_data = Telefono_referencia(
#             numero = fila['telefono_referencia'],
#             referencia = fila['nit_referencia'],
#         )

#     telefonos_referencias_data.save()


# def ingresar_clientes_referencias(df):
#     for index, fila in df.iterrows():
#         if pd.isna(fila['nit_referencia']) or pd.isna(fila['nombre_referencia']) or pd.isna(fila['telefono_referencia']):
#             continue
#         clientes_referencias_data = ClientesReferencias(
#             cliente_id = fila['nit'],
#             referencia_id = fila['nit_referencia'],
#         )

#     clientes_referencias_data.save()