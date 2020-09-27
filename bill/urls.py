from django.urls import path
from .views import *
urlpatterns = [
    path('bill', BillView.as_view()),
]