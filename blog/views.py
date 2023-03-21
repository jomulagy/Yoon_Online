from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post
    
def index(request):
    posts = Post.objects.all().order_by("-pk")
    context = {
        "posts" : posts,
    }
    return render(request, "blog/index.html",context)

def single_post_page(request,pk):
    post = Post.objects.get(id = pk)
    context = {
        'post' : post,
    }
    return render(request,"blog/single_post_page.html",context)