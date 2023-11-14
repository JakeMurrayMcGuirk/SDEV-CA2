from django.contrib import admin

from .models import Category, ProductModel


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ["category"]
    list_select_related = True


class ProductModelAdmin(admin.ModelAdmin):
    model = ProductModel
    search_fields = [
        "name",
        "description",
        "price",
        "stock",
        "images",
        "created_at",
        "updated_at",
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductModel, ProductModelAdmin)
