from django.contrib import admin

from .models import Oderitem, Order


class OderitemAdmin(admin.ModelAdmin):
    model = Oderitem
    search_fields = ["order", "product", "quantity", "price"]
    list_select_related = True


class OrderAdmin(admin.ModelAdmin):
    model = Order
    search_fields = ["user", "created_at", "updated_at", "total_amount"]
    list_select_related = True


admin.site.register(Oderitem, OderitemAdmin)
admin.site.register(Order, OrderAdmin)
