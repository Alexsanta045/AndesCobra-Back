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



class ClientesSerializer(serializers.ModelSerializer):
    nit = serializers.CharField()
    nombres = serializers.CharField()
    campos_opcionales = serializers.JSONField()

    class Meta:
        model = Clientes
        fields = ['nit', 'tipo_id', 'nombres', 'campos_opcionales']


class CodeudoresSerializer(serializers.ModelSerializer):
    nit = serializers.CharField()
    nombre = serializers.CharField()
    cliente = serializers.SerializerMethodField()
    campos_opcionales =serializers.JSONField()
    
    class Meta:
        model = Codeudores
        fields = '__all__'
        
    def get_cliente(self, obj):
        return f"{obj.cliente.nombres}"
        
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
    usuario = serializers.CharField()
    cliente = serializers.CharField(source='cliente.nombres')
    resultado = serializers.CharField(source='resultado.nombre', read_only=True)
    fecha = serializers.DateTimeField()
    comentarios = serializers.CharField(read_only=True)

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


class Telefono_clienteSerializer(serializers.Serializer):
    cliente = serializers.CharField(source='cliente.nombres')
    numero = serializers.CharField()
    rating = serializers.CharField()

    class Meta:
        model = Telefono_cliente
        fields = '__all__'


class Acuerdo_pagoSerializer(serializers.Serializer):
    valor_cuota = serializers.CharField()
    fecha_pago = serializers.CharField()
    codigo_obligacion = serializers.CharField(source='codigo_obligacion.codigo')
    usuario = serializers.SerializerMethodField()
    descripcion = serializers.CharField()
    estado=serializers.CharField() 
    
    class Meta:
        model = Acuerdo_pago
        fields = '__all__'
        
    def get_usuario(self, obj):
        return f"{obj.usuario.username}"
        
class Telefono_codeudorSerializer(serializers.Serializer):
    codeudor = serializers.CharField(source='codeudor.nombre')
    numero = serializers.CharField()
    rating = serializers.CharField()

    class Meta:
        model = Telefono_codeudor
        fields = '__all__'
    
class Telefono_referenciaSerializer(serializers.Serializer):
    referenia = serializers.CharField(source='referencia.nombre')
    numero = serializers.CharField()
    rating = serializers.CharField()

    class Meta:
        model = Telefono_referencia
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

