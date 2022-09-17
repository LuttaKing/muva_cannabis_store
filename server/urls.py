
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop_app.urls')),
    path('auth/',include('auth_app.urls')),
]

handler404 = 'helpers.views.handle_404n'
handler500 = 'helpers.views.handle_500'
