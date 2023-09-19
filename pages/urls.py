from django.urls import path
from .views import HomePageVeiw, AboutPageView #new

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageVeiw.as_view(), name="home"),
]