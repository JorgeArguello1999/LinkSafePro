from django.urls import path
from binary import views

urlpatterns = [
    path('', views.get, name='binary')
]