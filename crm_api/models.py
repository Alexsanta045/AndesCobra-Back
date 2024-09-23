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
    direccion = models.TextField(max_length=150)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nit} - {self.nombres} {self.apellidos}"

class Campañas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    
    def __str__(self):
        return self.nombre

class CampañasUsuarios(models.Model):
    usuarios_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    campañas_id = models.ForeignKey(Campañas, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    
    def __str__(self):
        return f"usuario: {self.usuarios_id} -  campaña: {self.campañas_id}"

class Clientes(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    telefono = models.CharField(max_length=10)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nit} - {self.telefono} - {self.nombres}"

class Codeudores(models.Model):
    nit = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=30)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nombre} - cliente: {self.cliente}"

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
    
    def __str__(self):
        return f"{self.campaña} - {self.cliente}"

class Pagos(models.Model):
    valor = models.IntegerField(default=0)
    fecha = models.DateField()
    obligacion = models.ForeignKey(Obligaciones, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.cliente} - {self.valor} - {self.fecha}"

class ResultadosGestion(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=200)
    efectividad = models.BooleanField(default=False)
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
        return f"{self.usuario} - {self.cliente} - {self.resultado} - {self.fecha}"