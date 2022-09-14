
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop_app.urls')),
    path('auth/',include('auth_app.urls')),
]
