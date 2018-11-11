from django.urls import path
from . import views

urlpatterns = [
    path('book/',views.CreateTable.as_view(),name='book_table'),
    path('userlist/',views.TableListView.as_view(),name='table_user_list'),
    path('book_lawn/',views.CreateLawn.as_view(),name='book_lawn'),
]
