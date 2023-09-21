from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageVeiw(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): #new
    template_name = 'about.html'

class PotatoPageView(TemplateView): #new
    template_name = 'potato.html'