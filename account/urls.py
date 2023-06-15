from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = "account"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("signup/", signup,name = "sign-up"),
    path("user/update/",user_update,name = "user_update"),
    path("user/delete/",user_delete,name = "user_delete"),
]
