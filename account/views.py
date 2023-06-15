from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .models import User


def signup(request):
    if request.method == 'POST':
        if User.objects.filter(username = request.POST.get("username")).exists():
            return render(request,"signup.html",{"message":"이미 존재하는 회원입니다."})
        else:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                first_name=request.POST['name'][0],
                last_name=request.POST['name'][1:],
                phone_number=request.POST.get("phonenum")
            )
            auth.login(request, user)
            return redirect('main:index')

    else:
        return render(request, 'signup.html')

def user_update(request):
    if request.method == "POST":
        user = request.user

        user.first_name = request.POST.get("name")[0]
        user.last_name = request.POST.get("name")[2:]
        if request.POST.get("password"):
            user.set_password(request.POST.get("password"))
        user.phone_number = request.POST.get("phone_number")
        user.save()
        auth.login(request,user)
        return redirect("main:index")
    else:
        return render(request,"editInfo.html")

def user_delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth.logout(request)
    return redirect("main:index")
