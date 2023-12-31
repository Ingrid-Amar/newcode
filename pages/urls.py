from django.urls import path
from .views import HomePageVeiw, AboutPageView, PotatoPageView #new

urlpatterns = [
    path("potato/", PotatoPageView.as_view(), name="potato"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageVeiw.as_view(), name="home"),
]