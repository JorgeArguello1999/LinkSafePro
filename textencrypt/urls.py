from django.urls import path
from textencrypt import views

urlpatterns = [
    path('', views.front, name='front'),
]