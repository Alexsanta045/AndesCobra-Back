from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from ..filters import ClientesFilter
from ..serializers.serializers import ClientesSerializer
from ..models import Clientes


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ClientesFilter

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def crear_cliente_si_no_existe(self, fila, campos_clientes_opcionales):
        try:
            cliente, creado = Clientes.objects.get_or_create(
                documento=fila['documento_cliente'],
                defaults={
                    # Aquí agregas los campos para nuevos clientes
                    'nit': fila.get('documento_cliente'),
                    'nombres': fila.get('Nombre', ''),
                    'email': fila.get('Apellido', ''),
                    # Agrega más campos según tu modelo
                }
            )
            return cliente
        except Exception as e:
            # Manejo de errores si falla la creación
            print(f"Error creando cliente: {e}")
            return None