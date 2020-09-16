from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length = 20, unique =True)
    def __str__(self):
        return self.name
        
class Product(models.Model):
    shop = models.ForeignKey(Shop,on_delete= models.CASCADE, related_name="products", related_query_name="products")
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 60)
    price = models.FloatField()
    def __str__(self):
        return self.name

class Swatch(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="swatches", related_query_name="swatches")

    name = models.CharField(max_length = 20)
    color_url = models.CharField(max_length = 200)
    product_img_url = models.CharField(max_length = 200)
    def __str__(self):
        return "{0}_{1}".format(self.product.name, self.name)
