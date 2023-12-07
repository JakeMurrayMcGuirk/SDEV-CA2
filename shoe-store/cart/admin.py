from django.contrib import admin

from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    model = Cart
    search_fields = ["user", "created_at", "updated_at"]
    list_select_related = True


class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    search_fields = ["cart", "product", "quantity"]
    list_select_related = True


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
