from django.conf import settings
from django.core.cache import cache
from rest_framework import generics

from .models import Item
from .serializers.spreadsheet import ItemListSerializer


class ItemListView(generics.ListAPIView):
    serializer_class = ItemListSerializer

    def get_queryset(self):
        if "items" in cache:
            # get results from cache
            return cache.get("items")
        else:
            results = Item.objects.all()
            # store data in cache
            cache.set("items", results, timeout=settings.CACHE_TTL)
            return results
