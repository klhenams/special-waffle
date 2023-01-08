from django.urls import resolve, reverse


def test_item_list():
    assert reverse("app:item_list") == "/app/spreadsheets/"
    assert resolve("/app/spreadsheets/").view_name == "app:item_list"
