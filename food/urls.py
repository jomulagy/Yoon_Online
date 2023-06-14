from django.urls import path
from .views import *

urlpatterns = [
    path("order/create/",OrderCreate,name = "order_create")
]
