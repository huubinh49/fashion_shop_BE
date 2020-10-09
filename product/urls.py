from django.urls import path
from .views import *
urlpatterns = [
    path('shop/<str:name>/<int:page>', ShopPage),
    path('shop/<str:name>', ShopView),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('product/search', SearchView),
]