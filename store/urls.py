from django.urls import path, include
from .views import *

app_name = "store"
urlpatterns = [
    path('table/',table_list,name = "table_list"),
]
