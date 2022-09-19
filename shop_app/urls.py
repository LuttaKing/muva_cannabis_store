from django.urls import path
from . import views,shop_view

urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('shop/',shop_view.shop, name='shop'),
    path('search/',shop_view.search, name='search'),
    path('product_detail/<id>/',views.product_detail, name='product_detail'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('contact/',views.contact_us_and_store_location, name='contact'),
    path('terms/',views.terms_and_privacy, name='terms'),
]