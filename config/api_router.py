from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "app"
urlpatterns = router.urls

# Spreadsheet urls
urlpatterns += [
    path("spreadsheets/", include("app.spreadsheets.urls")),
]
