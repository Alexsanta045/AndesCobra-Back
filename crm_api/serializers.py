from rest_framework import serializers
from .models import *

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
        
class UsuariosSerializer(serializers.ModelSerializer):
    nit = serializers.CharField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    email = serializers.EmailField()
    telefono = serializers.CharField()
    rol = serializers.CharField(source='rol.nombre')
    
    class Meta:
        model = Usuarios
        fields = '__all__'
        
class CampañasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campañas
        fields = '__all__'
        
class CanalesSerializer(serializers.Serializer):
    telefonico = serializers.BooleanField()
    visita = serializers.BooleanField()
    whatsapp = serializers.BooleanField()
    email = serializers.BooleanField()
    sms = serializers.BooleanField()
    
    class Meta:
        model = Canales
        fields = '__all__'
        
class ClientesSerializer(serializers.ModelSerializer):
    nit = serializers.CharField()
    tipo_id = serializers.CharField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()
    email = serializers.CharField()
    canales_autorizados = CanalesSerializer(read_only=True)
    
    class Meta:
        model = Clientes
        fields = [ 'nit', 'tipo_id', 'nombres', 'apellidos', 'email', 'canales_autorizados', 'campos_opcionales']
        
        
class CodeudoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codeudores
        fields = '__all__'
        
class ReferenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referencias
        fields = '__all__'
        
class ObligacionesSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField()
    campaña = serializers.CharField(source='campaña.nombre')
    cliente = serializers.SerializerMethodField()
    class Meta:
        model = Obligaciones
        fields = '__all__'
        
    def get_cliente(self, obj):
        return f"{obj.cliente.nombres} {obj.cliente.apellidos}"
        
class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'
        
class ResultadosGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadosGestion
        fields = '__all__'
        
class GestionesSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.nombres')
    cliente = serializers.CharField(source='cliente.nombres')
    resultado = serializers.CharField(source='resultado.nombre', read_only=True)
    fecha = serializers.DateTimeField()
    comentarios = serializers.CharField(read_only=True)
    
    class Meta:
        model = Gestiones
        fields = ['fecha', '__all__']
        
    # Formatear la fecha sin segundos ni milisegundos
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.fecha:
            representation['fecha'] = instance.fecha.strftime('%d-%m-%y %H:%M')
        return representation
    
class ChatSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='usuario.nombres')
    mensaje = serializers.CharField()
    fecha = serializers.DateTimeField()
    
    class Meta:
        model = Chat
        fields = ['fecha', '__all__']
        
    def get_usuario(self, obj):
        return f"{obj.usuario.nombres} {obj.usuario.apellidos}"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.fecha:
            representation['fecha'] = instance.fecha.strftime('%d-%m-%y %H:%M')
        return representation
    
class Tipo_identificacionSerializer(serializers.Serializer):
    class Meta:
        model = Tipo_identificacion
        fields = '__all__'
        
class PaisSerializer(serializers.Serializer):
    class Meta:
        model = Pais
        fields = '__all__'
        
class DepartamentoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    pais = serializers.CharField(source='pais.nombre',)
    
    class Meta:
        model = Departamento
        fields = '__all__'
    
class CiudadSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    departamento = serializers.CharField(source='departamento.nombre')
    
    class Meta: 
        model = Ciudad
        fields = '__all__'
    
class Telefono_clienteSerializer(serializers.Serializer):
    cliente = serializers.CharField(source='cliente.nombres')
    numero = serializers.CharField()
    tipo = serializers.CharField()
    tipo_celular = serializers.CharField()
    indicativo = serializers.CharField()
    extension = serializers.CharField()
    ciudad = serializers.CharField(source='ciudad.nombre')
    rating = serializers.CharField()
    departamento = serializers.CharField(source='departamento.nombre')
    
    class Meta:
        model = Telefono_cliente
        fields =  '__all__'
    
class Direccion_clienteSerializer(serializers.Serializer):
    cliente = serializers.CharField(source='cliente.nombres')
    ciudad = serializers.CharField(source='ciudad.nombre')
    barrio = serializers.CharField()
    vereda = serializers.CharField()
    calle = serializers.CharField()
    carrera = serializers.CharField()
    complemento = serializers.CharField()
    
    class Meta:
        model = Direccion_cliente
        fields = '__all__'
        
class Direccion_codeudorSerializer(serializers.Serializer):
    codeudor = serializers.CharField(source='codeudor.nombres')
    ciudad = serializers.CharField(source='ciudad.nombre')
    barrio = serializers.CharField()
    vereda = serializers.CharField()
    calle = serializers.CharField()
    carrera = serializers.CharField()
    complemento = serializers.CharField()
    
    class Meta:
        model = Direccion_cliente
        fields = '__all__'

        
        
class Acuerdo_pagoSerializer(serializers.Serializer):
    valor_cuota = serializers.CharField()
    fecha_pago = serializers.CharField()
    codigo_obligacion = serializers.CharField()
    
    class Meta:
        model = Acuerdo_pago
        fields = '__all__'
        
class Telefono_codeudorSerializer(serializers.Serializer):
    codeudor = serializers.CharField(source='codeudor.nombres')
    numero = serializers.CharField()
    tipo = serializers.CharField()
    tipo_celular = serializers.CharField()
    indicativo = serializers.CharField()
    extension = serializers.CharField()
    ciudad = serializers.CharField(source='ciudad.nombre')
    rating = serializers.CharField()
    departamento = serializers.CharField(source='departamento.nombre')
    
    class Meta:
        model = Telefono_cliente
        fields = '__all__'
    
