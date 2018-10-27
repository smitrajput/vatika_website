from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AboutPage(TemplateView):
    template_name = 'home/about.html'

class HomePage(TemplateView):
    template_name = 'home/index.html'
