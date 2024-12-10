from rest_framework import serializers
from ..models import *
from rest_framework import serializers

class CampañasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Campañas
        fields = ['id', 'nombre']
        
class CampañasUsuariosSerializer(serializers.ModelSerializer):
    usuarios_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())  # Relación de clave foránea
    campañas_id = serializers.PrimaryKeyRelatedField(queryset=Campañas.objects.all())  # Relación de clave foránea
    
    class Meta:
        model = CampañasUsuarios
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    role_id = serializers.IntegerField(required= True)
    role_name = serializers.CharField(source= "role", required= False)
    estado = serializers.SerializerMethodField(required= False)
    campaña = serializers.SerializerMethodField(required= False)

    def get_estado(self,obj):
        estado = obj.estado
        
        if estado == True:
            return 'Activo'
        else:
            return 'Inactivo'
                
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'role_id', 'role_name' , 'estado', 'campaña','is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        role_id = validated_data.pop('role_id', None)
        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(
            password=password,
            **validated_data
        )
        user.role_id = role_id

        user.save()

        return user
    
    def get_campaña(self, obj):
        id = obj.id
        campañas = CampañasUsuarios.objects.filter(usuarios_id=id).select_related('campañas_id')  # Optimiza las consultas
        if campañas.exists():
            return [{"id": c.campañas_id.id, "nombre": c.campañas_id.nombre} for c in campañas]
        return []


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id', 'nombre']


        
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
        fields = ['nit', 'tipo_id', 'nombres', 'apellidos',
                'email', 'canales_autorizados', 'campos_opcionales']


class CodeudoresSerializer(serializers.ModelSerializer):
    nit = serializers.CharField()
    nombre = serializers.CharField()
    cliente = serializers.SerializerMethodField()
    
    class Meta:
        model = Codeudores
        fields = '__all__'
        
    def get_cliente(self, obj):
        return f"{obj.cliente.nombres} {obj.cliente.apellidos}"
        
class ReferenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referencias
        fields = '__all__'


class ObligacionesSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField()
    campaña = serializers.CharField()
    cliente = serializers.CharField()
    class Meta:
        model = Obligaciones
        fields = '__all__'

    # def get_cliente(self, obj):
    #     return f"{obj.cliente.nombres} {obj.cliente.apellidos}"
    
    def create(self, validated_data):
        # Extrae los IDs de campaña y cliente directamente en lugar de datos anidados
        campaña_id = validated_data.pop('campaña', None)
        cliente_id = validated_data.pop('cliente', None)
        
        # Obtén la instancia de Clientes con el ID proporcionado o lanza un error si no se encuentra
        try:
            cliente = Clientes.objects.get(pk=cliente_id)
            validated_data['cliente'] = cliente
        except Clientes.DoesNotExist:
            raise serializers.ValidationError("El cliente con el ID proporcionado no existe.")
        
        # Obtén la instancia de Campañas con el ID proporcionado o lanza un error si no se encuentra
        try:
            campaña = Campañas.objects.get(pk=campaña_id)
            validated_data['campaña'] = campaña
        except Campañas.DoesNotExist:
            raise serializers.ValidationError("La campaña con el ID proporcionado no existe.")

        # Crea la instancia de Obligaciones usando los datos validados
        obligacion = Obligaciones.objects.create(**validated_data)
        return obligacion


class PagosSerializer(serializers.ModelSerializer):
    valor = serializers.FloatField()
    fecha = serializers.DateField()
    obligacion = serializers.CharField(source='obligacion.codigo')
    cliente = serializers.SerializerMethodField()
    
    class Meta:
        model = Pagos
        fields = '__all__'
        
    def get_cliente(self, obj):
        return f"{obj.obligacion.cliente.nombres} {obj.obligacion.cliente.apellidos}"

        
class ResultadosGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadosGestion
        fields = '__all__'


class GestionesSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    cliente = serializers.PrimaryKeyRelatedField(queryset=Clientes.objects.all())
    resultado = serializers.PrimaryKeyRelatedField(queryset=ResultadosGestion.objects.all())
    comentarios = serializers.CharField()

    class Meta:
        model = Gestiones
        fields =  '__all__'
        

    # Formatear la fecha sin segundos ni milisegundos
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.fecha:
            representation['fecha'] = instance.fecha.strftime('%d-%m-%y %H:%M')
        return representation


class ChatSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField()
    mensaje = serializers.CharField()
    fecha = serializers.DateTimeField()

    class Meta:
        model = Chat
        fields = '__all__'
        
    def get_usuario(self, obj):
        return f"{obj.usuario.nombres} {obj.usuario.apellidos}"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.fecha:
            representation['fecha'] = instance.fecha.strftime('%d-%m-%y %H:%M')
        return representation


class Tipo_identificacionSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    
    class Meta:
        model = Tipo_identificacion
        fields = '__all__'


class PaisSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    
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
        fields = '__all__'


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
    codeudor = serializers.CharField(source='codeudor.nombre')
    ciudad = serializers.CharField(source='ciudad.nombre')
    barrio = serializers.CharField()
    vereda = serializers.CharField()
    calle = serializers.CharField()
    carrera = serializers.CharField()
    complemento = serializers.CharField()

    class Meta:
        model = Direccion_codeudor
        fields = '__all__'


class Acuerdo_pagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acuerdo_pago
        fields = '__all__'
        
    def get_usuario(self, obj):
        return f"{obj.usuario.username}"
        
class Telefono_codeudorSerializer(serializers.Serializer):
    codeudor = serializers.CharField(source='codeudor.nombre')
    numero = serializers.CharField()
    tipo = serializers.CharField()
    tipo_celular = serializers.CharField()
    indicativo = serializers.CharField()
    extension = serializers.CharField()
    ciudad = serializers.CharField(source='ciudad.nombre')
    rating = serializers.CharField()
    departamento = serializers.CharField(source='departamento.nombre')

    class Meta:
        model = Telefono_codeudor
        fields = '__all__'
    

class GestionesFilterSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField()
    cliente = serializers.CharField(source='cliente.nombres')
    resultado = serializers.CharField(source='resultado.nombre', read_only=True)
    fecha = serializers.DateTimeField()
    comentarios = serializers.CharField(read_only=True)
    
    class Meta:
        model = Gestiones
        fields = ['usuario','cliente','resultado','fecha','comentarios',]
        
class TipoGestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_gestion
        fields = '__all__'
        
        