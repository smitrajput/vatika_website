from django.shortcuts import render
from django.views.generic import CreateView
from .models import Feedback
# Create your views here.

class CreateFeedback(CreateView):
    model = Feedback
    template_name = 'feedback/feedback.html'
