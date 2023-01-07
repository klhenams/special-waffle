import pytest

from app.spreadsheets.models import Item

from .factories import ItemFactory


@pytest.fixture
def item(db) -> Item:
    return ItemFactory()
