from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by("-pk")
    context = {
        "posts" : posts,
    }
    return render(request, "blog/index.html",context)
