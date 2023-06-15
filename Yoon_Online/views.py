from django.shortcuts import render
from food.models import Category

def index(request):
    context = {
        "categories" : Category.objects.all()
    }
    return render(request,"main.html",context)
