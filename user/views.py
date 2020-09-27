from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, decorators, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer
from bill.serializers import BillSerializer
from bill.models import Bill
from .models import User
import jwt
from django.conf import settings
# Create your views here.
from rest_framework_social_oauth2.views import ConvertTokenView

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
    id = jwt.decode(
        request.POST['refresh'],
        settings.SECRET_KEY,
        algorithms= "HS256"
    ).get('user_id')
    user = User.objects.get(pk = id);
    refresh_token = RefreshToken.for_user(user)
    return Response({'access': str(refresh_token.access_token)}, status=status.HTTP_200_OK)


class SocialView(ConvertTokenView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        response = super(SocialView, self).post(request, args, kwargs)
        response.data['email'] = request.POST['email']
        response.data['username'] = "{0} {1}".format(request.POST['first_name'], request.POST['last_name'])

        try:
            user = User.objects.get(email = request.POST['email'])
        except User.DoesNotExist:
            user = User(email = request.POST['email'], username = response.data['username'])
            password = User.objects.make_random_password()
            user.set_password(password)
        
        refresh_token = RefreshToken.for_user(user)
        response.data['access_token']=  str(refresh_token.access_token)
        response.data['refresh_token']=  str(refresh_token)
        return response

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.AllowAny])
def obtainUserInfo(request):
    user_id = jwt.decode(
        request.GET.get('access'),
        settings.SECRET_KEY,
        algorithms= "HS256"
    ).get('user_id')
    try:
        user = User.objects.get(pk = user_id)
        bills = Bill.objects.filter(owner__id = user_id)
        bills_serializers = BillSerializer(bills, many = True)
        return Response(data={
                'username': user.username,
                'email': user.email,
                'bills': bills_serializers.data
            }, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
