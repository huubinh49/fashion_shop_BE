from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, decorators, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer
from .models import User
# Create your views here.

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh_token = RefreshToken.for_user(user)
    respone = {
        'refresh': str(refresh_token),
        'access' : str(refresh_token.access_token)
    }
    return Response(respone, status=status.HTTP_201_CREATED)

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def obtainTokenForUser(request):
    #TODO : Authenticate user
    print(request.POST)
    user = User(email = request.POST['email'], password = request.POST['password'], username = request.POST['username'])
    refresh_token = RefreshToken.for_user(user)
    return Response({'access': str(refresh_token.access_token)}, status=status.HTTP_200_OK)
