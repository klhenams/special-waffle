from django.test import RequestFactory

from app.spreadsheets.models import Item
from app.spreadsheets.views import ItemListView
from app.users.models import User


class TestItemListView:
    def test_get_queryset(self, user: User, item: Item, rf: RequestFactory):
        view = ItemListView()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert item in view.get_queryset()
