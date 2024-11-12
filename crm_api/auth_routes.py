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

# Login
@api_view(['POST'])
def login(request):
    print("Login endpoint reached")  # Añade esta línea

    username = request.data.get('username')
    password = request.data.get('password')

    user = get_object_or_404(CustomUser, username=username)

    if not user.check_password(password):
        return Response({"error": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)

    token, _ = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

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
