from django.contrib import admin

# Register your models here.
from .models import Cart, CartItemDetails

"""
class CartItemInline(admin.TabularInline):
    model = CartItem

class CartAdmin(admin.ModelAdmin):
    inlines = [
        CartItemInline
    ]
    class Meta:
        model = Cart
"""


admin.site.register(Cart)
admin.site.register(CartItemDetails)
