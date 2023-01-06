from django.urls import resolve, reverse

from app.users.models import User


def test_user_detail(user: User):
    assert (
        reverse("app:user-detail", kwargs={"username": user.username})
        == f"/app/users/{user.username}/"
    )
    assert resolve(f"/app/users/{user.username}/").view_name == "app:user-detail"


def test_user_list():
    assert reverse("app:user-list") == "/app/users/"
    assert resolve("/app/users/").view_name == "app:user-list"


def test_user_me():
    assert reverse("app:user-me") == "/app/users/me/"
    assert resolve("/app/users/me/").view_name == "app:user-me"
