from django.urls import path

from .views import ItemListView

urlpatterns = [
    path("", ItemListView.as_view(), name="item_list"),
]
