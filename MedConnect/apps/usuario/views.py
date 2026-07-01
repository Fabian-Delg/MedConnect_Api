from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({
            "success": True,
            "username": user.username
        })

    return Response(
        {
            "success": False,
            "mensaje": "Usuario o contraseña incorrectos"
        },
        status=status.HTTP_401_UNAUTHORIZED
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def registro_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response(
            {
                "success": False,
                "mensaje": "El usuario ya existe"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    User.objects.create_user(
        username=username,
        password=password
    )

    return Response({
        "success": True,
        "mensaje": "Usuario registrado correctamente"
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def logout_api(request):
    return Response({
        "success": True
    })