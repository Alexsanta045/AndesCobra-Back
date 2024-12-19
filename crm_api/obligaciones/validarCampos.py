import pandas as pd

def validar_fila(fila):
    # Lista de motivos para una fila específica
    motivos = []

    # Validar columna nit 
    if not fila['nit']:
        motivos.append("El NIT es requerido")
    elif not isinstance(fila['nit'], (int, str)) or not str(fila['nit']).isdigit():
        motivos.append("NIT inválido")

    # Validar columna fecha_obligacion 
    if pd.notna(fila['fecha_obligacion']):  
        if not isinstance(fila['fecha_obligacion'], str):  
            motivos.append("Fecha de obligación inválida")

    # Validar columna fecha_vencimiento
    if pd.notna(fila['fecha_vencimiento']):
        if not isinstance(fila['fecha_vencimiento'], str):
            motivos.append("Fecha de vencimiento inválida")

    # Validar columna valor_obligacion 
    if pd.notna(fila['valor_obligacion']):
        try:
            valor_obligacion = float(fila['valor_obligacion'])
        except:
            try:
                valor_obligacion = int(fila['valor_obligacion'])
            except:
                print("Error valor obligacion no es un numero")
                valor_obligacion = fila['valor_obligacion']

        if not isinstance(valor_obligacion, (int, float)) or valor_obligacion < 0:
            motivos.append("Valor obligación inválido")
    
    # Validar columna valor_vencido 
    if not fila['valor_vencido']:
        motivos.append("Valor vencido es requerido")
    elif not isinstance(fila['valor_vencido'], (int, float)) or fila['valor_vencido'] < 0:
        motivos.append("Valor vencido inválido")
    
    # Validar columna valor_cuota 
    if pd.notna(fila['valor_cuota']):
        try:
            valor_cuota = float(fila['valor_cuota'])
        except:
            try:
                valor_cuota = int(fila['valor_cuota'])
            except:
                print('Error: valor de cuota no es un numero ')
                valor_cuota = fila['valor_cuota']

        if not isinstance(valor_cuota, (int, float)) or valor_cuota < 0:
            motivos.append("Valor cuota inválido")

    # Validar columna saldo_capital 
    if pd.notna(fila['saldo_capital']):
        try:
            saldo_capital = float(fila['saldo_capital'])
        except:
            try:
                saldo_capital = int(fila['saldo_capital'])
            except:
                print('Error: saldo capital no es un numero')
                saldo_capital = fila['saldo_capital']

        if not isinstance(saldo_capital, (int, float)) or saldo_capital < 0:
            motivos.append("Saldo capital inválido")

    # Validar columna saldo_total 
    if pd.notna(fila['saldo_total']):
        try:
            saldo_total = float(fila['saldo_total'])
        except:
            try: 
                saldo_total = int(fila['saldo_total'])
            except:
                print('Error: el saldo total no es un numero')
                saldo_total = fila['saldo_total']
        
        if not isinstance(saldo_total, (int, float)) or saldo_total < 0:
            motivos.append("Saldo total inválido")

    # Validar columna tipo_de_producto 
    if pd.notna(fila['tipo_de_producto']):
        if not isinstance(fila['tipo_de_producto'], str):
            motivos.append("Tipo de producto inválido")

    # Validar columna dias_de_mora 
    if pd.notna(fila['dias_de_mora']):
        try:
            dias_de_mora = int(fila['dias_de_mora'])
        except:
            try:
                dias_de_mora = float(fila['dias_de_mora'].replace(',', '.'))
            except:
                print('error los dias de mora no es un numero')
                dias_de_mora= fila['dias_de_mora']

        if not isinstance(dias_de_mora, int) or dias_de_mora < 0:
            motivos.append("Días de mora inválidos")

    # Validar columna valor_ultimo_pago 
    if pd.notna(fila['valor_ultimo_pago']):
        try:
            valor_ultimo_pago = float(fila['valor_ultimo_pago'])
        except:
            try:
                valor_ultimo_pago = int(fila['valor_ultimo_pago'])
            except:
                print('Error el valor del ultimo pago no es un numero')
                valor_ultimo_pago = fila['valor_ultimo_pago']

        if not isinstance(valor_ultimo_pago, (int, float)) or valor_ultimo_pago < 0:
            motivos.append("Valor último pago inválido")

    # Validar columna intereses_corrientes 
    if pd.notna(fila['intereses_corrientes']):

        try:
            intereses_corrientes = float(fila['intereses_corrientes'])
        except:
            try:
                intereses_corrientes = int(fila['intereses_corrientes'])
            except:
                print('Error intereses corrientes no es un numero')
                intereses_corrientes = fila['intereses_corrientes']

        if not isinstance(intereses_corrientes, (int, float)) or intereses_corrientes < 0:
            motivos.append("Intereses corrientes inválidos")

    # Validar columna intereses_mora 
    if pd.notna(fila['intereses_mora']):
        try:
            intereses_mora = float(fila['intereses_mora'])
        except:
            try:
                intereses_mora = int(fila['intereses_mora'])
            except:
                intereses_mora = fila['intereses_mora']
                print('Error: intereses de mora no es un numero')

        if not isinstance(intereses_mora, (int, float)) or intereses_mora < 0:
            motivos.append("Intereses de mora inválidos")

    # Validar columna 'plazo' (debe ser un número entero positivo, o puede estar vacía)
    if pd.notna(fila['plazo']):
        if not isinstance(fila['plazo'], str):
            motivos.append("Plazo inválido")

    # Validar columna calificacion_obligacion 
    if pd.notna(fila['calificacion_obligacion']):
        if not isinstance(fila['calificacion_obligacion'], str):
            motivos.append("Calificación de obligación inválida")

    # Validar columna ciclo 
    if pd.notna(fila['ciclo']):
        if not isinstance(fila['ciclo'], str):
            motivos.append("Ciclo inválido")

    # Validar columna etapa_actual_obligacion 
    if pd.notna(fila['etapa_actual_obligacion']):
        if not isinstance(fila['etapa_actual_obligacion'], str):
            motivos.append("Etapa actual de obligación inválida")

    # Validar columna fecha_inactivacion 
    if pd.notna(fila['fecha_inactivacion']):
        if not isinstance(fila['fecha_inactivacion'], str):
            motivos.append("Fecha de inactivación inválida")

    # Validar columna estado_operacional 
    if pd.notna(fila['estado_operacional']):
        if not isinstance(fila['estado_operacional'], str):
            motivos.append("Estado operacional inválido")

    # Validar columna dias_mora_inicial 
    if pd.notna(fila['dias_mora_inicial']):
        if not isinstance(fila['dias_mora_inicial'], int) or fila['dias_mora_inicial'] < 0:
            motivos.append("Días de mora inicial inválidos")

    # Validar columna rango_mora_inicial 
    if pd.notna(fila['rango_mora_inicial']):
        if not isinstance(fila['rango_mora_inicial'], str):
            motivos.append("Rango de mora inicial inválido")

    # Validar columna rango_mora_actual 
    if pd.notna(fila['rango_mora_actual']):
        if not isinstance(fila['rango_mora_actual'], str):
            motivos.append("Rango de mora actual inválido")

    # Validar columna fecha_inicio_mora 
    if pd.notna(fila['fecha_inicio_mora']):
        if not isinstance(fila['fecha_inicio_mora'], str):
            motivos.append("Fecha de inicio de mora inválida")

    # Validar columna tasa_interes 
    if pd.notna(fila['tasa_interes']):
        if not isinstance(fila['tasa_interes'], (int, float)) or fila['tasa_interes'] < 0:
            motivos.append("Tasa de interés inválida")

    # Validar columna porc_gastos_cobranza 
    if pd.notna(fila['porc_gastos_cobranza']):
        if not isinstance(fila['porc_gastos_cobranza'], (int, float)) or fila['porc_gastos_cobranza'] < 0:
            motivos.append("Porcentaje de gastos cobranza inválido")

    # Validar columna 'valor_gastos_cobranza' (debe ser número positivo o cero, o puede estar vacía)
    if pd.notna(fila['valor_gastos_cobranza']):
        try:
            valor_gastos_cobranza = float(fila['valor_gastos_cobranza'])
        except:
            try:
                valor_gastos_cobranza = int(fila['valor_gastos_cobranza'])
            except:
                print('Error valor gastos cobranza no es un numero')
                valor_gastos_cobranza = fila['valor_gastos_cobranza']

        if not isinstance(valor_gastos_cobranza, (int, float)) or valor_gastos_cobranza < 0:
            motivos.append("Valor de gastos de cobranza inválido")

    # Validar columna valor_iva_gastos 
    if pd.notna(fila['valor_iva_gastos']):
        if not isinstance(fila['valor_iva_gastos'], (int, float)) or fila['valor_iva_gastos'] < 0:
            motivos.append("Valor IVA de gastos inválido")

    # Validar columna valor_otros_conceptos 
    if pd.notna(fila['valor_otros_conceptos']):
        if not isinstance(fila['valor_otros_conceptos'], (int, float)) or fila['valor_otros_conceptos'] < 0:
            motivos.append("Valor de otros conceptos inválido")

    # Validar columna fecha_castigo
    if pd.notna(fila['fecha_castigo']):
        if not isinstance(fila['fecha_castigo'], str):
            motivos.append("Fecha de castigo inválida")

    # Validar columna cuotas_vencidas
    if pd.notna(fila['cuotas_vencidas']):
        if not isinstance(fila['cuotas_vencidas'], int) or fila['cuotas_vencidas'] < 0:
            motivos.append("Cuotas vencidas inválidas")

    # Validar columna coutas_pendientes 
    if pd.notna(fila['coutas_pendientes']):
        if not isinstance(fila['coutas_pendientes'], int) or fila['coutas_pendientes'] < 0:
            motivos.append("Cuotas pendientes inválidas")

    # Validar columna cuotas_pagadas
    if pd.notna(fila['cuotas_pagadas']):
        if not isinstance(fila['cuotas_pagadas'], int) or fila['cuotas_pagadas'] < 0:
            motivos.append("Cuotas pagadas inválidas")

    # Validar columna libranza
    if pd.notna(fila['libranza']):
        if not isinstance(fila['libranza'], str):
            motivos.append("Libranza inválida")

    # Validar columna nit_empresa
    if pd.notna(fila['nit_empresa']):
        if not isinstance(fila['nit_empresa'], str) or len(fila['nit_empresa']) > 13:
            motivos.append("NIT de la empresa inválido")

    # Validar columna sucursal
    if pd.notna(fila['sucursal']):
        if not isinstance(fila['sucursal'], str):
            motivos.append("Sucursal inválida")

    # Validar columna regional
    if pd.notna(fila['regional']):
        if not isinstance(fila['regional'], str):
            motivos.append("Regional inválida")

    # Validar columna puntaje_credito
    if pd.notna(fila['puntaje_credito']):
        if not isinstance(fila['puntaje_credito'], (int, float)) or fila['puntaje_credito'] < 0:
            motivos.append("Puntaje de crédito inválido")

    # Validar columna puntaje_comportamiento
    if pd.notna(fila['puntaje_comportamiento']):
        if not isinstance(fila['puntaje_comportamiento'], (int, float)) or fila['puntaje_comportamiento'] < 0:
            motivos.append("Puntaje de comportamiento inválido")

    # Validar columna marca_especial
    if pd.notna(fila['marca_especial']):
        if not isinstance(fila['marca_especial'], str):
            motivos.append("Marca especial inválida")

    # Validar columna fecha_corte_obligacion
    if pd.notna(fila['fecha_corte_obligacion']):
        if not isinstance(fila['fecha_corte_obligacion'], str):
            motivos.append("Fecha de corte de obligación inválida")

    # Validar columna fecha_facturacion_obligacion
    if pd.notna(fila['fecha_facturacion_obligacion']):
        if not isinstance(fila['fecha_facturacion_obligacion'], str): 
            motivos.append("Fecha de facturación de obligación inválida")
       
    # Validar columna nombre
    if not fila['nombre']:
        motivos.append("El nombre del cliente es requerido")
    elif not isinstance(fila['nombre'], str):
        motivos.append("Nombre  del cliente inválido")

    # Validar columna tipo_identificacion
    if pd.notna(fila['tipo_identificacion']):
        if not isinstance(fila['tipo_identificacion'], str):
            motivos.append("Tipo de identificación inválido")

    # Validar columna apellidos
    if pd.notna(fila['apellidos']):
        if not isinstance(fila['apellidos'], str):
            motivos.append("Apellidos del cliente inválidos")

    # Validar columna fecha_nacimiento
    if pd.notna(fila['fecha_nacimiento']):
        if not isinstance(fila['fecha_nacimiento'], str):  
            motivos.append("Fecha de nacimiento inválida")

    # Validar columna fecha_ingreso
    if pd.notna(fila['fecha_ingreso']):
        if not isinstance(fila['fecha_ingreso'], str):
            motivos.append("Fecha de ingreso inválida")
        

    # Validar columna actividad_economica
    if pd.notna(fila['actividad_economica']):
        if not isinstance(fila['actividad_economica'], str):
            motivos.append("Actividad económica inválida")

    # Validar columna genero
    if pd.notna(fila['genero']):
        if fila['genero'] not in ['M', 'F', 'm', 'f'] :  
            motivos.append("Género inválido")

    # Validar columna empresa
    if pd.notna(fila['empresa']):
        if not isinstance(fila['empresa'], str):
            motivos.append("Empresa inválida")

    # Validar columna cantidad_hijos
    if pd.notna(fila['cantidad_hijos']):
        if not isinstance(fila['cantidad_hijos'], int) or fila['cantidad_hijos'] < 0:
            motivos.append("Cantidad de hijos inválida")

    # Validar columna estrato
    if pd.notna(fila['estrato']):
        if not isinstance(fila['estrato'], int) or fila['estrato'] < 1 or fila['estrato'] > 6:
            motivos.append("Estrato inválido")

    # Validar columna calificacion_cliente
    if pd.notna(fila['calificacion_cliente']):
        if not isinstance(fila['calificacion_cliente'], (int, float)):
            motivos.append("Calificación de cliente inválida")

    # Validar columna tipo_persona
    if pd.notna(fila['tipo_persona']):
        if not isinstance(fila['tipo_persona'], str):
            motivos.append("Tipo de persona inválido")

    # Validar columna profesion
    if pd.notna(fila['profesion']):
        if not isinstance(fila['profesion'], str):
            motivos.append("Profesión inválida")

    # Validar columna estado_fraude
    if pd.notna(fila['estado_fraude']):
        if not isinstance(fila['estado_fraude'], str):
            motivos.append("Estado de fraude inválido")

    # Validar columna calificacion_buro
    if pd.notna(fila['calificacion_buro']):
        if not isinstance(fila['calificacion_buro'], str):
            motivos.append("Calificación de buró inválida")

    # Validar columnas de teléfonos (telefono_1 a telefono_10)
    if not fila['telefono_1']:
        motivos.append("El telefono 1 del cliente es requerido")
    elif not isinstance(fila['telefono_1'], (int, str)) or len(str(fila['telefono_1'])) > 10 or not str(fila['telefono_1']).isdigit():
        motivos.append("telefono 1 invalido")

    for i in range(2, 11):
        telefono = fila.get(f'telefono_{i}')
        
        if pd.notna(telefono) and telefono:  
            if not isinstance(telefono, (int, str)):
                motivos.append(f"Teléfono {i} inválido")
            elif len(str(telefono)) > 10 or not str(telefono).isdigit():
                motivos.append(f"Teléfono {i} inválido")

    # Validar columna direccion
    if pd.notna(fila['direccion']):
        if not isinstance(fila['direccion'], str):
            motivos.append("Dirección inválida")

    # Validar columna email
    if pd.notna(fila['email']):
        if not isinstance(fila['email'], str) or "@" not in fila['email']:
            motivos.append("Email inválido")

    # Validar columna ciudad
    if pd.notna(fila['ciudad']):
        if not isinstance(fila['ciudad'], str) or len(fila['ciudad']) == 0:
            motivos.append("Ciudad inválida")

    # Validar columna codigo_dane_cliente
    if pd.notna(fila['codigo_dane_cliente']):
        if not isinstance(fila['codigo_dane_cliente'], str) or len(fila['codigo_dane_cliente']) != 5:
            motivos.append("Código DANE de cliente inválido")

    # Validar columna nit_codeudor
    if pd.notna(fila['nit_codeudor']):
        if not isinstance(fila['nit_codeudor'], str) or len(fila['nit_codeudor']) != 9:
            motivos.append("NIT de codeudor inválido")

    # Validar columna nombre_codeudor
    if pd.notna(fila['nombre_codeudor']):
        if not isinstance(fila['nombre_codeudor'], str):
            motivos.append("Nombre de codeudor inválido")

    # Validar columna telefono_codeudor
    if pd.notna(fila['telefono_codeudor']):
        if not isinstance(fila['telefono_codeudor'], str) or len(str(fila['telefono_codeudor'])) > 10 or not str(fila['telefono_codeudor']).isdigit():
            motivos.append("Teléfono de codeudor inválido")

    # Validar columna direccion_codeudor
    if pd.notna(fila['direccion_codeudor']):
        if not isinstance(fila['direccion_codeudor'], str):
            motivos.append("Dirección de codeudor inválida")

    # Validar columna email_codeudor
    if pd.notna(fila['email_codeudor']):
        if not isinstance(fila['email_codeudor'], str) or "@" not in fila['email_codeudor']:
            motivos.append("Email de codeudor inválido")

    # Validar columna ciudad_codeudor
    if pd.notna(fila['ciudad_codeudor']):
        if not isinstance(fila['ciudad_codeudor'], str):
            motivos.append("Ciudad de codeudor inválida")

    # Validar columna codigo_dane_codeudor
    if pd.notna(fila['codigo_dane_codeudor']):
        if not isinstance(fila['codigo_dane_codeudor'], str) or len(fila['codigo_dane_codeudor']) != 5:
            motivos.append("Código DANE de codeudor inválido")

    # Validar columna nit_referencia
    if pd.notna(fila['nit_referencia']):
        if not isinstance(fila['nit_referencia'], (str, int)):
            motivos.append("NIT de referencia inválido")

    # Validar columna nombre_referencia
    if pd.notna(fila['nombre_referencia']):
        if not isinstance(fila['nombre_referencia'], str) or len(fila['nombre_referencia']) == 0:
            motivos.append("Nombre de referencia inválido")

    # Validar columna telefono_referencia
    if pd.notna(fila['telefono_referencia']):
        if not isinstance(fila['telefono_referencia'], str) or  len(str(fila['telefono_referencia'])) > 10 or not str(fila['telefono_referencia']).isdigit():
            motivos.append("Teléfono de referencia inválido")

    # Validar columna direccion_referencia
    if pd.notna(fila['direccion_referencia']):
        if not isinstance(fila['direccion_referencia'], str) or len(fila['direccion_referencia']) == 0:
            motivos.append("Dirección de referencia inválida")

    # Validar columna email_referencia
    if pd.notna(fila['email_referencia']):
        if not isinstance(fila['email_referencia'], str) or "@" not in fila['email_referencia']:
            motivos.append("Email de referencia inválido")

    # Validar columna ciudad_referencia
    if pd.notna(fila['ciudad_referencia']):
        if not isinstance(fila['ciudad_referencia'], str) or len(fila['ciudad_referencia']) == 0:
            motivos.append("Ciudad de referencia inválida")

    # Validar columna codigo_dane_referencia
    if pd.notna(fila['codigo_dane_referencia']):
        if not isinstance(fila['codigo_dane_referencia'], str) or len(fila['codigo_dane_referencia']) != 5:
            motivos.append("Código DANE de referencia inválido")



    return motivos
