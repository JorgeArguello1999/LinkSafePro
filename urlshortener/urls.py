from django.urls import path
from urlshortener import views

urlpatterns = [
    path('', views.front, name="urlshortener"),
]