from django.contrib import admin

from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    model = ProductReview
    search_fields = ["product", "user", "rating", "review_text", "review_timestamp"]
    list_select_related = True


admin.site.register(ProductReview, ProductReviewAdmin)
