from django.urls import path

from .views import *
app_name = "blog"

urlpatterns = [
    path("",PostLV.as_view()),
    path("<int:pk>/",PostDV.as_view()),
    #path('',index,name = "index"),
    #path("<int:pk>/",single_post_page),
]
