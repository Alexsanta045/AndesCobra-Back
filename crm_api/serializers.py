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
    direccion = serializers.CharField()
    rol = serializers.SerializerMethodField()
    
    class Meta:
        model = Usuarios
        fields = ['nit', 'nombres', 'apellidos', 'email', 'telefono', 'direccion', 'rol']
        
    def get_rol(self, obj):
        return obj.rol.nombre
        
class CampañasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campañas
        fields = '__all__'
        
class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        
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
    campaña = serializers.SerializerMethodField()
    cliente = serializers.SerializerMethodField()
    class Meta:
        model = Obligaciones
        fields = ['codigo', 'campaña', 'cliente', 'campos_opcionales']
        
    def get_campaña(self, obj):
        return obj.campaña.nombre
    
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
    usuario = serializers.SerializerMethodField()
    cliente = serializers.SerializerMethodField()
    resultado = serializers.CharField(source='resultado.nombre', read_only=True)
    fecha = serializers.DateTimeField()
    comentarios = serializers.CharField(read_only=True)
    
    class Meta:
        model = Gestiones
        fields = ['usuario', 'cliente', 'resultado', 'fecha', 'comentarios']
        
    def get_usuario(self, obj):
        return f"{obj.usuario.nombres} {obj.usuario.apellidos}"
    
    def get_cliente(self, obj):
        return f"{obj.cliente.nombres} {obj.cliente.apellidos}"
    
    # Formatear la fecha sin segundos ni milisegundos
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.fecha:
            representation['fecha'] = instance.fecha.strftime('%d-%m-%y %H:%M')
        return representation
    
class ChatSerializer(serializers.ModelSerializer):
    usuario = serializers.SerializerMethodField()
    mensaje = serializers.CharField()
    fecha = serializers.DateTimeField()
    
    class Meta:
        model = Chat
        fields = ['usuario' , 'mensaje' , 'fecha']
        
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
    pais = serializers.SerializerMethodField()
    
    class Meta:
        model = Departamento
        fields = ['nombre', 'pais']
        
    def get_pais(self, obj):
        return obj.pais.nombre
    
class CiudadSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    departamento = serializers.SerializerMethodField()
    
    class Meta: 
        model = Ciudad
        fields = ['nombre', 'departamento']
        
    def get_departamento(self, obj):
        return obj.departamento.nombre
    
class Telefono_clienteSerializer(serializers.Serializer):
    numero = serializers.CharField()
    tipo = serializers.CharField()
    tipo_celular = serializers.CharField()
    indicativo = serializers.CharField()
    extension = serializers.CharField()
    ciudad = serializers.SerializerMethodField()
    rating = serializers.CharField()
    departamento = serializers.SerializerMethodField()
    cliente = serializers.SerializerMethodField()
    
    class Meta:
        model = Telefono_cliente
        fields = ['ciudad', '__all__']
        
    def get_ciudad(self, obj):
        return obj.ciudad.nombre
    
    def get_departamento(self, obj):
        return obj.ciudad.departamento.nombre
    
    def get_cliente(self, obj):
        return obj.telefono.cliente.nombres
    
class Direccion_clienteSerializer(serializers.Serializer):
    ciudad = serializers.SerializerMethodField()
    
    class Meta:
        model = Direccion_cliente
        fields = ['ciudad', '__all__']
        
class Direccion_codeudorSerializer(serializers.Serializer):
    ciudad = serializers.SerializerMethodField()
    
    class Meta:
        model = Direccion_codeudor
        fields = ['ciudad', '__all__']
        
class CanalesSerializer(serializers.Serializer):
    class Meta:
        model = Canales
        fields = '__all__'
        
class Acuerdo_pagoSerializer(serializers.Serializer):
    class Meta:
        model = Acuerdo_pago
        fields = '__all__'
        
class Telefono_codeudorSerializer(serializers.Serializer):
    numero = serializers.CharField()
    tipo = serializers.CharField()
    tipo_celular = serializers.CharField()
    indicativo = serializers.CharField()
    extension = serializers.CharField()
    ciudad = serializers.SerializerMethodField()
    rating = serializers.CharField()
    departamento = serializers.SerializerMethodField()
    codeudor = serializers.SerializerMethodField()
    
    class Meta:
        model = Telefono_cliente
        fields = ['ciudad', '__all__']
        
    def get_ciudad(self, obj):
        return obj.ciudad.nombre
    
    def get_departamento(self, obj):
        return obj.ciudad.departamento.nombre
    
    def get_cliente(self, obj):
        return obj.telefono.cliente.nombres