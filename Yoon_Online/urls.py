from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path("",index,name = "index"),
    path("cart/",cart,name = "cart"),
    path("cartDetail/", cartDetail, name="cartDetail")
]
