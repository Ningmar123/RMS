from django.contrib import admin
from .models import Table, Menu, Category, Waiter, Reception, Order

# Register your models here.
admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Waiter)
admin.site.register(Reception)
admin.site.register(Order)
