from django.contrib import admin
from .models import Category, Menu, Order, Menu_Order
# Register your models here.
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Menu_Order)
