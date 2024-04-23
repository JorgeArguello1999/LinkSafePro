from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('textencrypt/', include('textencrypt.urls')),
    path('speed/', include('speed.urls')),
    path('binary/', include('binary.urls')),
    path('urlshortener/', include('urlshortener.urls')),
    path('', include('home.urls')),
]