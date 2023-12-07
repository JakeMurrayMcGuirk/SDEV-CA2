from rest_framework import serializers

from .models import ProductSearch


class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSearch
        fields = ["id", "product", "search_query", "search_filters", "search_timestamp"]
