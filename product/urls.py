from django.urls import path
from .views import *
from .views_create import *
urlpatterns = [
    path('shop/<str:name>/<int:page>', ShopPage),
    path('shop/<str:name>', ShopView),
    path('product/<int:pk>', ProductDetailView.as_view()),
    # path('shop/create/<str:path>', index),
    path('product/search', SearchView),
]