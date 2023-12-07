from rest_framework import serializers

from .models import Category, ProductModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category"]


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock",
            "images",
            "created_at",
            "updated_at",
        ]
