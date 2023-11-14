from rest_framework import serializers

from .models import Oderitem, Order


class OderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oderitem
        fields = ["id", "order", "product", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "user", "created_at", "updated_at", "total_amount"]
