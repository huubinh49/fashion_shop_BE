from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import decorators
from .serializers import *
from .models import *
# Create your views here.

# 
# def obtainRefreshForUser(request):
#     #TODO : Authenticate user
#     user = User(email = request.POST['email'], password = request.POST['password'], username = request.POST['username'])
#     refresh_token = RefreshToken.for_user(user)
#     return Response({'refresh': str(refresh_token)}, status=status.HTTP_200_OK)
@decorators.api_view(('GET', ))
@decorators.permission_classes([permissions.AllowAny])
def ShopView(request, name):
    shop = Shop.objects.get(name = name)
    serializer = ShopSerializer(instance=shop)
    return Response(serializer.data)

@decorators.api_view(('GET', ))
@decorators.permission_classes([permissions.AllowAny])
def ShopPage(request, name, page):
    
    shop = Shop.objects.get(name = name)
    products = Product.objects.filter(shop = shop.id)
    serializer = ProductSerializer(products[(page-1)*10:(page)*10], many = True)
    res = {
        'name':shop.name,
        'id':shop.id,
        'products': serializer.data
    }
    return Response(res)

class ProductDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        serializer = ProductSerializer(instance = product)
        return Response(serializer.data)
    
    def get_object(self, pk):
        try:
            return Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    # def post(self, request, pk, *arg, **kwargs):
    #     product = self.get_object(pk)
    #     serializer = ProductSerializer(product, data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format = None):
    #     product = self.get_object(pk)
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

@decorators.api_view(('GET', ))
@decorators.permission_classes([permissions.AllowAny])
def SearchView(request):
    
    query = request.GET.get('name')
    res = Product.objects.filter(name__contains = query)
    serializer = ProductSerializer(res, many= True)
    # for product in serializer.data:
        # product['shop'] = Shop.objects.get(int(product['shop'])).name
    return Response(serializer.data, status=status.HTTP_200_OK)