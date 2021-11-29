from django.contrib import admin
from .models import OrderDetail, ShoppingCart, OrderGoods
# Register your models here.

admin.site.register(OrderDetail)
admin.site.register(ShoppingCart)
admin.site.register(OrderGoods)
