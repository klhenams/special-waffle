from rest_framework import generics

from .models import Item
from .serializers.spreadsheet import ItemListSerializer


class ItemListView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
