from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer

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


# Registro


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        try:
            with transaction.atomic():
                user = serializer.save()  # Aquí se crea el usuario
                # Asegúrate de que el token se crea o se obtiene
                token, created = Token.objects.get_or_create(user=user)

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




# # Perfil
# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     return Response({"role": request.user.role.id}, status=status.HTTP_200_OK)
