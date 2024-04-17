from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['POST', 'GET'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = UserSerializer()  # Aquí creas una instancia del serializer
        return render(request, 'register.html', {'serializer': serializer})

@api_view(['POST'])
def login(request):
    # Lógica de tu vista de inicio de sesión
    return render(request, 'login.html')


@api_view(['POST'])
def profile(request):
    # Lógica de tu vista de perfil de usuario
    return render(request, 'profile.html')
