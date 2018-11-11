from django.urls import path
from . import views
from feedback import views as feedviews


urlpatterns = [
    path('',feedviews.DisplayRatings.as_view(),name='home-page'),
    path('about/',views.AboutPage.as_view(), name = "about-page"),
    path('contact/',views.CreateContact.as_view(),name='contact'),
]
