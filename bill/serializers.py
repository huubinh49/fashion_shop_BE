from rest_framework import serializers
from .models import Bill, Order
from product.serializers import ProductSerializer, SwatchesSerializer
from user.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    color = SwatchesSerializer()
    class Meta:
        model = Order
        fields = "__all__"

class BillSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many = True)
    owner = UserSerializer()
    orderDate = serializers.DateTimeField(format = "%d-%m-%Y %H:%M:%S")
    class Meta: 
        model = Bill
        fields = "__all__"