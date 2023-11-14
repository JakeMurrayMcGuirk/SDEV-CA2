from django.contrib import admin

from .models import ProductSearch


class ProductSearchAdmin(admin.ModelAdmin):
    model = ProductSearch
    search_fields = ["product", "search_query", "search_filters", "search_timestamp"]
    list_select_related = True


admin.site.register(ProductSearch, ProductSearchAdmin)
