from rest_framework import serializers
from .models import Product,Swatch,Shop


class SwatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swatch
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.SerializerMethodField()
    swatches = SwatchesSerializer(many=True, read_only = True)
    class Meta:
        model = Product
        fields = '__all__'
    def get_shop(self, obj):
        return obj.shop.name

class ShopSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many = True)
    class Meta:
        model = Shop
        fields= "__all__"