from django.shortcuts import render
from food.models import Category

def index(request):
    context = {
        "categories" : Category.objects.all()
    }
    return render(request,"main.html",context)

def cart(request):
    return render(request,"cart.html")

def cartDetail(request):
    return render(request,"cartDetail.html")
