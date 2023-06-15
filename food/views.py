from django.shortcuts import render, redirect
import json
from django.http import JsonResponse

from .models import Order, Menu, Menu_Order

def OrderCreate(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            order = Order(user = request.user)
            order.save()

            for item in data:
                menu = Menu.objects.get(name = item['name'])
                new = Menu_Order(menu = menu, order = order, quantity = item['quantity'])
                new.save()

            return JsonResponse({'success' : True},status = 200)
        else:
            return JsonResponse({'success':False,"error" : "로그인 후 이용해주세요."}, status=400)

    # POST 요청이 아니거나 AJAX 요청이 아닌 경우
    return JsonResponse({}, status=404)

def OrderList(request):
    order_list = Order.objects.filter(user = request.user)
    return render(request,"cart.html",{"order_list":order_list})

def OrderDetail(request,id):
    order = Order.objects.get(id = id)
    return render(request,"cartDetail.html",{"order":order})

def OrderDelete(request,id):
    order = Order.objects.get(id = id)
    order.delete()
    return redirect('food:order_list')
