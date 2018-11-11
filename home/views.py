from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contact
from .forms import ContactForm
# Create your views here.
app_name = 'home'
class AboutPage(TemplateView):
    template_name = 'home/about.html'

class HomePage(TemplateView):
    template_name = 'home/index.html'

class CreateContact(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact.html'
