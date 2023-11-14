from rest_framework import serializers

from .models import Wishlistitem


class WishlistitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlistitem
        fields = ["id", "user", "product", "added_timestamp"]
