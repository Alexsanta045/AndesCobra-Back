import pandas as pd

def validar_fila(fila):
    motivos = []

    if not fila['nit_cliente']:
        motivos.append ='el Nit del cliente es requerido'
    elif not isinstance(fila['nit_cliente'], (str, int)) or not str(fila['nit_cliente']).isdigit():
        motivos.append('el nitdel cliente no es un numero')
    
    if pd.notna(fila['tipo_id']):
        if not isinstance(fila['tipo_id'], str):
            motivos.append('tipo de id invalido')

    if not fila['nombres_cliente']:
        motivos.append('El nombre del clinte es requerido')
    elif not isinstance(fila['nombres_cliente'], str):
        motivos.append('Nombres del cliente invalidos')

    if pd.notna(fila['apellidos_cliente']):
        print('-------------------------------------------------')
        print(f'fecha vencimiento --->{fila['fecha_vencimiento']} ')
        if not isinstance(fila['apellidos_cliente'], str):
            motivos.append('apellidos del cliente invalidos')
    
    if not fila['telefono_cliente']:
        motivos.append('el telefono del cliente es requerido')
    elif not isinstance(fila['telefono_cliente'], (str, int)) or len(str(fila['telefono_cliente'])) > 10 or not str(fila['telefono_cliente']).isdigit():
        motivos.append('Telefono del cliente invalido')

    if pd.notna(fila['email_cliente']):
        if not isinstance(fila['email_cliente'], str) or "@" not in fila['email_cliente']:
            motivos.append('Email del cliente invalido')

    if pd.notna(fila['direccion_cliente']):
        if not isinstance(fila['direccion_cliente'], str):
            motivos.append("Dirección del cliente inválida")
    
    if pd.notna(fila['ciudad_cliente']):
        if not isinstance(fila['ciudad_cliente'], str):
            motivos.append('Ciudad del cliente invalida')
        
    if pd.notna(fila['genero_cliente']):
        if fila['genero_cliente'] not in ['M', 'F', 'm', 'f']:
            motivos.append('Genero del cliente invalido')

    if not fila['codigo_resultado_gestion']:
        motivos.append('El código del resultado de la gestion es requerido')
    elif not isinstance(fila['codigo_resultado_gestion'], (str, int)) or not str(fila['nit_cliente']).isdigit():
        motivos.append('Código delreultado de la gestión invalido')

    if pd.notna(fila['resultado_gestion']):
        motivos.append('El resultado de la getion es requerido')
    elif not isinstance(fila['resultado_gestion'], str):
        motivos.append('Resultado de la gestión invalido')

    # if pd.notna(fila['fecha_gestion']):
    #     if not isinstance(fila['fecha_gestion'], str):
    #         motivos.append('Fecha de gestion invalida')

    if pd.notna(fila['comentarios_gestion']):
        if not isinstance(fila['comentarios_gestion'], str):
            motivos.append('Comentarios gestión invalido')

    if pd.notna(fila['tipo_gestion']):
        if not isinstance(fila['tipo_gestion'], str):
            motivos.append('Tpo gestión invalido')

    





        

    
        
