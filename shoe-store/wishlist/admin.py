from django.contrib import admin

from .models import Wishlistitem


class WishlistitemAdmin(admin.ModelAdmin):
    model = Wishlistitem
    search_fields = ["user", "product", "added_timestamp"]
    list_select_related = True


admin.site.register(Wishlistitem, WishlistitemAdmin)
