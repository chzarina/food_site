from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.book_table, name='book_table'),
]
