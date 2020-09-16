from .models import *
import json
import os
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render, HttpResponse
# request.GET.get('shop', '')
# request.GET.get('shop', '')
def index(request, path):
    shop = Shop.objects.create(name = path)
    shop.save()
    with open(staticfiles_storage.path('data/{0}.json'.format(path)), 'r') as f:
        data = json.loads(f.read())
        for sp in data:
            product = Product.objects.create(
                shop = shop,
                name = sp['name'],
                price = float(sp['price'][1:])
            )
            product.save()

            for sw in sp['swatches']:
                swatch = Swatch.objects.create(
                    product = product,
                    name = sw['color_name'],
                    color_url = sw['color'],
                    product_img_url = sw['img']
                )
    
    return HttpResponse("successfully!")