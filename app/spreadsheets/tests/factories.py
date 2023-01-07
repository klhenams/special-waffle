from factory import Sequence, fuzzy
from factory.django import DjangoModelFactory

from app.spreadsheets.models import Item


class ItemFactory(DjangoModelFactory):

    title = Sequence(lambda n: "Item %d" % n)
    description = fuzzy.FuzzyText(length=150)
    image = Sequence(lambda n: "http://example.com/item-image%d.jpg" % n)

    class Meta:
        model = Item
        django_get_or_create = ["title"]
