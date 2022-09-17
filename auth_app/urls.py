from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register_user, name='register'),
    path('login/',views.login_user, name='login'),
    path('reset_pass/',views.change_password, name='reset_pass'),
    path('activate_user/<uidb64>/<token>',views.activate_user, name='activate')
]