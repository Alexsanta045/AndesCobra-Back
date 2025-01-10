from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.timezone import now
import random
from django.conf import settings  # Para usar CustomUser si está en settings.AUTH_USER_MODEL


class Roles(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'roles'  # Opcional: especifica el nombre de la tabla
        
class Campañas(models.Model):
    id = models.IntegerField(unique=True, editable=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now_add= True)
    img = models.URLField(blank=True, null=True, max_length=500)
    campos_opcionales = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generar_codigo_unico()
        super().save(*args, **kwargs)
    
    def generar_codigo_unico(self):
        codigo = str(random.randint(1000, 999999))
        while Campañas.objects.filter(id=codigo).exists():
            codigo = str(random.randint(1000, 999999))
        return codigo

class CustomUser(AbstractUser):
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'custom_user'  

    def __str__(self):
        return self.username
    
class CampañasUsuarios(models.Model):
    usuarios_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    campañas_id = models.ForeignKey(Campañas, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"usuario: {self.usuarios_id} -  campaña: {self.campañas_id}"

                                
class Chat(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mensaje = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario}: '{self.mensaje}'"
    

class Clientes(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=70)
    tipo_id = models.CharField(max_length=10, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=80, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    actividad_economica = models.CharField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=15, blank=True, null=True)
    empresa = models.CharField(max_length=60, blank=True, null=True)
    cantidad_hijos = models.IntegerField(blank=True, null=True)
    estrato = models.IntegerField(blank=True, null=True)
    calificacion_cliente = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    tipo_persona = models.CharField(max_length=60, blank=True, null=True)
    profesion = models.CharField(max_length=60, blank=True, null=True)
    estado_fraude = models.CharField(max_length=70, blank=True, null=True)
    calificacion_buro = models.CharField(max_length=60, blank=True, null=True)
    codigo_dane = models.CharField(max_length=10, blank=True, null=True)
    campos_opcionales = models.JSONField(default=dict, blank=True, null=True)
    
    def __str__(self):
        return self.nit
    

class Telefono_cliente(models.Model):
    numero = models.CharField(max_length=15, primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.numero


class Codeudores(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=70)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=80, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    codigo_dane = models.CharField(max_length=10, blank=True, null=True)
    campos_opcionales = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres}"

class Obligaciones(models.Model):
    codigo = models.CharField(max_length=25, unique=True, editable=False, primary_key=True)
    codigo_obligacion = models.CharField(max_length=20, null=True, blank=True)
    campaña = models.ForeignKey(Campañas, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    codeudor = models.ForeignKey(Codeudores, on_delete=models.SET_NULL, null=True, blank=True, related_name='obligaciones')
    valor_vencido = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_obligacion = models.DateField(null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    valor_obligacion = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    valor_cuota = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    saldo_capital = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    saldo_total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    tipo_producto = models.CharField(max_length=50, null=True, blank=True)
    dias_mora = models.IntegerField(null=True, blank=True)
    valor_ultimo_pago = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    intereses_corriente = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    intereses_mora = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    plazo = models.DateField(null=True, blank=True)
    calificacion_obligacion = models.CharField(max_length=50, null=True, blank=True)
    ciclo = models.CharField(max_length=50, null=True, blank=True)
    etapa_actual_obligacion = models.CharField(max_length=60, null=True, blank=True)
    fecha_inactivacion = models.DateField(null=True, blank=True)
    estado_operacional = models.CharField(max_length=60, null=True, blank=True)
    dias_mora_inicial = models.IntegerField(null=True, blank=True)
    rango_mora_inicial = models.CharField(max_length=70, null=True, blank=True)
    rango_mora_actual = models.CharField(max_length=70, null=True, blank=True)
    fecha_inicio_mora = models.DateField(null=True, blank=True)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    porc_gastos_cobranza = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    valor_gastos_cobranza = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    valor_iva_gastos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valor_otros_conceptos = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    fecha_castigo = models.DateField(null=True, blank=True)
    cuotas_vencidas = models.IntegerField(null=True, blank=True)
    cuotas_pendientes = models.IntegerField(null=True, blank=True)
    cuotas_pagadas = models.IntegerField(null=True, blank=True)
    libranza = models.CharField(max_length=70, null=True, blank=True)
    nit_empresa = models.CharField(max_length=15, null=True, blank=True)
    sucursal =  models.CharField(max_length=70, null=True, blank=True)
    regional = models.CharField(max_length=70, null=True, blank=True)
    puntaje_credito = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    puntaje_comportamiento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    marca_especial = models.CharField(max_length=65, null=True, blank=True)
    fecha_corte_obligacion = models.DateField(null=True, blank=True)
    fecha_facturacion_obligacion = models.DateField(null=True, blank=True)
    campos_opcionales = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return f"{self.codigo} - {self.cliente}"
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = self.generar_codigo_unico()
        super().save(*args, **kwargs)

    def generar_codigo_unico(self):
        codigo = str(random.randint(1000, 9223372036854775807))
        while Obligaciones.objects.filter(codigo=codigo).exists():
            codigo = str(random.randint(1000, 9223372036854775807))
        return codigo
    
class Telefono_codeudor(models.Model):
    numero = models.CharField(max_length=15, primary_key=True)
    codeudor = models.ForeignKey(Codeudores, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0 )

    def __str__(self):
        return self.numero
    
class Referencias(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=80, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    codigo_dane = models.CharField(max_length=10, blank=True, null=True)
    campos_opcionales = models.JSONField(default=dict, blank=True, null=True)
     
    def __str__(self):
        return f"{self.nit} - {self.nombres}"

class ClientesReferencias(models.Model):
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    referencia_id = models.ForeignKey(Referencias, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"cliente: {self.cliente_id} - referencia: {self.referencia_id}"

class Telefono_referencia(models.Model):
    numero = models.CharField(max_length=15, primary_key=True)
    referencia = models.ForeignKey(Referencias, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0 )

    def __str__(self):
        return self.numero

class Acuerdo_pago(models.Model):
    valor_cuota = models.FloatField()  # Monto de la cuota
    fecha_pago = models.DateField()  # Fecha de pago
    fecha_gestion = models.DateField()  # Fecha de gestión
    codigo_resultado_gestion = models.CharField(max_length=100, null=True, blank=True)  # Resultado de la gestión
    resultado_gestion = models.CharField(max_length=100, null=True, blank=True)  # Descripción del resultado de la gestión
    codigo_obligacion = models.CharField(max_length=50)  # Código de obligación como un campo de texto
    codigo_asesor = models.CharField(max_length=50, null=True, blank=True)  # Campo opcional
    descripcion = models.CharField(max_length=60, default='sin descripcion', blank=True)  # Descripción opcional

    def __str__(self):
        return f"Acuerdo de pago {self.codigo_obligacion} - {self.codigo_asesor}"

class Subir_pagos(models.Model):
    valor_pago = models.FloatField()
    fecha_pago = models.DateField()
    codigo = models.CharField(max_length=30)

class ArchivoProcesado(models.Model):
    hash = models.CharField(max_length=32, unique=True)
    fecha_procesado = models.DateTimeField(auto_now_add=True)

class Pagos(models.Model):
    obligacion = models.ForeignKey(Obligaciones, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)
    fecha = models.DateField()
    plan_pago_id = models.IntegerField(blank=True, null=True)
    campos_opcionales = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return f"{self.obligacion} - {self.valor} - {self.fecha}"

class ResultadosGestion(models.Model):
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=60)
    efectividad = models.BooleanField(default=False, blank=True)
    estado = models.BooleanField(default=False)
    campaña = models.ForeignKey(Campañas, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} - campaña: {self.campaña}"

class Tipo_gestion(models.Model):
    nombre = models.CharField(max_length=60)
    def __str__(self):
        return self.nombre  

class Gestiones(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    resultado = models.ForeignKey(ResultadosGestion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=now)
    comentarios = models.TextField(max_length=200, null=True, blank=True)
    tipo_gestion = models.ForeignKey(Tipo_gestion, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Usuario: {self.usuario}, Cliente: {self.cliente}, Resultado: {self.resultado}, Fecha: {self.fecha}"
    

class PasswordChangeRequest(models.Model):
    email_or_username = models.CharField(max_length=255)  # Puede ser un correo o un nombre de usuario
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación de la solicitud
    is_changed = models.BooleanField(default=False)  # Indicador de si la contraseña fue cambiada
    changed_at = models.DateTimeField(null=True, blank=True)  # Fecha en que la contraseña fue cambiada
    is_rejected = models.BooleanField(default=False)  # Nuevo campo para marcar si la solicitud fue rechazada


    def __str__(self):
        return f'Solicitud de {self.email_or_username} - {self.created_at} - {"Cambiada" if self.is_changed else "Pendiente"}'
    

class CodigosEstado(models.Model):
    codigo = models.CharField()
    nombre = models.CharField(max_length=100)
    campaña = models.ForeignKey(Campañas, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.codigo