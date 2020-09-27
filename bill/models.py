from django.db import models
from product.models import Product, Swatch
from user.models import User
# Create your models here.
class Bill(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(to = User, blank=True, null=True, on_delete=models.CASCADE, related_name= 'user', related_query_name= 'user')
    orderDate = models.DateTimeField(auto_now_add=True)
    #The options auto_now_add, auto_now, and default are mutually exclusive. Any combination of these options will result in an error.
    address = models.CharField(max_length = 200)
    price = models.FloatField()
class Order(models.Model):
    id = models.AutoField(primary_key = True)
    bill = models.ForeignKey(to = Bill, on_delete=models.CASCADE, null=True, related_name='orders', related_query_name='orders')
    product = models.ForeignKey(to = Product, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(to = Swatch,  on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    size = models.CharField(max_length = 10)
    price = models.FloatField()


    