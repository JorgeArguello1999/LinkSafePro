from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('text/', include('textencrypt.urls')),
    path('speed/', include('speed.urls')),
    path('binary/', include('binary.urls')),
    path('', include('home.urls')),
]