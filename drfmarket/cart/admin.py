from django.contrib import admin
from .models import Cart,Cartitems,CartOrder
# Register your models here.

admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(CartOrder)