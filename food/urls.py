from django.urls import path
from .views import *

app_name = 'food'
urlpatterns = [
    path("order/create/",OrderCreate,name = "order_create"),
    path("order/list/",OrderList,name = "order_list"),
    path("order/detail/<int:id>",OrderDetail,name = "order_detail"),
    path("order/delete/<int:id>",OrderDelete,name = "order_delete"),

]
