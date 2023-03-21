from django.urls import path

from .views import *
app_name = "single_page"

urlpatterns = [
    path('about_me/',about_me, name = "about_me"),
    path("",landing, name = "landing"),
]
