from django.core.cache import cache
from rest_framework import filters, generics

from .serializers.spreadsheet import ItemListSerializer


class ItemListView(generics.ListAPIView):
    serializer_class = ItemListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
    ]

    def get_queryset(self):
        if "items" in cache:
            # get results from cache
            return cache.get("items")
