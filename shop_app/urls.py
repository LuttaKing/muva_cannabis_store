from django.urls import path
from . import views,shop_view,cart_view

urlpatterns=[
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('shop/',shop_view.shop, name='shop'),
    path('search/',shop_view.search, name='search'),
    path('product_detail/<id>/',views.product_detail, name='product_detail'),


    path('cart/',cart_view.cart, name='cart'),
    path('add-to-cart/<id>/', cart_view.add_to_cart, name="add_to_cart"),
    path('remove-cart/<int:cart_id>/', cart_view.delete_cart, name="remove-cart"),
    path('plus-cart/<int:cart_id>/', cart_view.plus_cart, name="plus-cart"),
    path('minus-cart/<int:cart_id>/', cart_view.minus_cart, name="minus-cart"),


    path('checkout/',views.checkout, name='checkout'),
    path('contact/',views.contact_us_and_store_location, name='contact'),
    path('terms/',views.terms_and_privacy, name='terms'),
]