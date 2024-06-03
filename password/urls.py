from django.urls import path
from password import views 

urlpatterns = [
    path('', views.get, name='password')
]