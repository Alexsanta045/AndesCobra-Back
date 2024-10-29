from django.db import models


class Roles(models.Model):
    nombre = models.CharField(max_length=25)
    
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nit} - {self.nombres} {self.apellidos}"
    
class Chat(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    mensaje = models.TextField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario}: '{self.mensaje}'"
    

class Campañas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    campos_opcionales = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return self.nombre

class CampañasUsuarios(models.Model):
    usuarios_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    campañas_id = models.ForeignKey(Campañas, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    
    def __str__(self):
        return f"usuario: {self.usuarios_id} -  campaña: {self.campañas_id}"
    
class Tipo_identificacion(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    

class Canales(models.Model):
    telefonico = models.BooleanField(default=True)
    visita = models.BooleanField(default=False)
    whatsapp = models.BooleanField(default=False)
    email = models.BooleanField(default=False)
    sms = models.BooleanField(default=False)
    
    def __str__(self):
        return f"telefonico: {self.telefonicon} email: {self.email} visita: {self.visita} whatsapp: {self.whatsapp} sms: {self.sms}"

class Clientes(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    tipo_id = models.ForeignKey(Tipo_identificacion, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    campos_opcionales = models.JSONField(default=dict, blank=True)
    canales_autorizados = models.ForeignKey(Canales, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nit} - {self.telefono} - {self.nombres}"
    
class Direccion_cliente(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    barrio = models.CharField(max_length=50)
    vereda = models.CharField(max_length=20, blank=True)
    calle = models.CharField(max_length=15, blank=True)
    carrera = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=70, blank=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.calle} - {self.carrera} - {self.complemento} "

class Codeudores(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=30)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} - cliente: {self.cliente}"
    
class Direccion_codeudor(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    barrio = models.CharField(max_length=50)
    vereda = models.CharField(max_length=20, blank=True)
    calle = models.CharField(max_length=15, blank=True)
    carrera = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=70, blank=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.calle} - {self.carrera} - {self.complemento} "

class Telefono_cliente(models.Model):
    numero = models.CharField(max_length=10, primary_key=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30)
    tipo_celular = models.CharField(max_length=30)
    indicativo = models.CharField(max_length=5)
    extension = models.CharField(max_length=5)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.numero
    
class Telefono_codeudor(models.Model):
    numero = models.CharField(max_length=10, primary_key=True)
    cliente = models.ForeignKey(Codeudores, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30)
    tipo_celular = models.CharField(max_length=30)
    indicativo = models.CharField(max_length=5)
    extension = models.CharField(max_length=5)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.numero
    
class Referencias(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.nit} - {self.nombre}"

class ClientesReferencias(models.Model):
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    referencia_id = models.ForeignKey(Referencias, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"cliente: {self.cliente_id} - referencia: {self.referencia_id}"

class Obligaciones(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    campaña = models.ForeignKey(Campañas, on_delete=models.CASCADE) 
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha_obligacion = models.DateField()
    fecha_vencimiento_cuota = models.DateField()
    valor_capital = models.FloatField()
    valor_mora = models.FloatField()
    campos_opcionales = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return f"{self.campaña} - {self.cliente}"
    
class Acuerdo_pago(models.Model):
    valor_cuota = models.FloatField()
    fecha_pago = models.DateField()
    codigo_obligacion = models.ForeignKey(Obligaciones, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"obligacion: {self.codigo_obligacion} - valor: {self.valor_cuota} - fecha: {self.fecha_pago}"

class Pagos(models.Model):
    obligacion = models.ForeignKey(Obligaciones, on_delete=models.CASCADE)
    valor = models.IntegerField(default=0)
    fecha = models.DateField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    campos_opcionales = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return f"{self.cliente} - {self.valor} - {self.fecha}"

class ResultadosGestion(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=200, blank=True)
    efectividad = models.BooleanField(default=False, blank=True)
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.nombre} - estado: {self.estado}"

class Gestiones(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    resultado = models.ForeignKey(ResultadosGestion, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    comentarios = models.TextField(max_length=200)
    
    def __str__(self):
        return f"Usuario: {self.usuario}, Cliente: {self.cliente}, Resultado: {self.resultado}, Fecha: {self.fecha}"
