from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer
from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

# Login
@api_view(['POST'])
def login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    try:
        # Intenta obtener el usuario con el nombre de usuario proporcionado
        user = CustomUser.objects.get(username=username)
    except ObjectDoesNotExist:
        # Si no se encuentra el usuario, retorna un mensaje personalizado de error
        return Response({"error": "Usuario Invalido"}, status=status.HTTP_400_BAD_REQUEST)


    # Verifica si la contraseña es correcta
    if not user.check_password(password):
        return Response({"error": "Contraseña Incorrecta"}, status=status.HTTP_400_BAD_REQUEST)

    # Genera o recupera el token de autenticación
    if user.is_active:
        token, _ = Token.objects.get_or_create(user=user)
    else:
            return Response({"error": "Usuario desactivado"}, status=status.HTTP_401_UNAUTHORIZED)

    # Serializa el usuario
    serializer = UserSerializer(instance=user)

    # Retorna la respuesta con el token y los datos del usuario
    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

# Register
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            with transaction.atomic():
                user = serializer.save()  # Aquí se crea el usuario
                token, created = Token.objects.get_or_create(user=user)  # Asegúrate de que el token se crea o se obtiene
                
                return Response({
                    'token': token.key,
                    'user': UserSerializer(user).data
                }, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response({
                'error': 'Error creating user',
                'detail': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Rol requerido
def role_required(roles):
    def decorator(func):
        @wraps(func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

            user_role = request.user.role.nombre if request.user.role else None
            # Verifica si el rol del usuario es uno de los roles permitidos
            if user_role not in roles:
                return HttpResponseForbidden("You do not have permission to access this resource.")
            
            return func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


@api_view(['GET'])
@role_required(['admin'])  # Solo los usuarios con rol 'admin' pueden acceder
def admin_dashboard(request):
    return Response({"message": "Bienvenido, Admin!"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@role_required(['advisor', 'leader'])  # Solo los usuarios con rol 'advisor' o 'leader' pueden acceder
def advisor_leader_dashboard(request):
    return Response({"message": "Bienvenido, Advisor o Leader!"}, status=status.HTTP_200_OK)


User = get_user_model() #Para obtener el modelo del usuario actualmente

@api_view(['POST'])
def logout(request):
    # Verificar si el token está en el encabezado de autorización
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Token '):
        token_key = auth_header.split(' ')[1]  # Obtener el token
        try:
            token = Token.objects.get(key=token_key)  # Buscar el token en la base de datos
            token.delete()  # Eliminar el token para cerrar la sesión
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Token not provided"}, status=status.HTTP_401_UNAUTHORIZED)