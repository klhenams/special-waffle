from rest_framework import serializers

from app.spreadsheets.models import Item


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            "title",
            "description",
            "image",
        ]
