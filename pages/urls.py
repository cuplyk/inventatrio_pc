from django.urls import path

from .views import HomePageView, AboutPageView, InventoryPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("inventory/", InventoryPageView.as_view(), name="inventory"),
]
