from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import BillSerializer
from .models import Bill, Order
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from user.models import User
from product.models import Product
from datetime import datetime
from django.conf import settings
import jwt
import json
# Create your views here.
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class BillView(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    def get(self, request, *args, **kwargs):
        user_id = jwt.decode(request.GET.get('access_token'), settings.SECRET_KEY, algorithms= ['HS256'])['user_id']
        bills = Bill.objects.filter(owner__id = user_id)
        serializer = BillSerializer(bills, many = True) 
        return Response(data= serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs): 
        user_id = jwt.decode(request.data['access_token'], settings.SECRET_KEY, algorithms= ['HS256'])['user_id']
        owner = User.objects.get(pk = user_id)
        address = request.data['address']
        bill = Bill(owner = owner, address = address)
        products = json.loads(request.data['products'])
        price = 0
        bill.price = price
        bill.save()
        if(len(products)):
         for product in products:
             try:
                 db_product = Product.objects.get(pk = product['id'])

                 swatches = [swatch for swatch in db_product.swatches.all() if swatch.name == product["color"]]
                 order = Order(product = db_product,color = swatches[0], quantity = product["quantity"], size = product["size"], price = db_product.price*int(product["quantity"]))
                 order.bill = bill
                 order.save()

                 price = price+order.price
             except Product.DoesNotExist:
                 return Response(status=status.HTTP_404_NOT_FOUND)

        bill.price = price
        bill.save()
        return Response(status=status.HTTP_201_CREATED)