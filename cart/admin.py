from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user',)}

@admin.register(CartItem)
class CartItemAdmin( admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cart',)}
    list_display = ('product', 'quantity')

