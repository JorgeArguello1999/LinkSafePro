from django.urls import path
from speed import views

urlpatterns = [
    path('', views.get, name='speed')
]