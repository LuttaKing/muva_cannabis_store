from django.shortcuts import render

def home(request):
    return render(request,'shop_app/index.html')

def about(request):
    return render(request,'shop_app/about.html')

def shop(request):
    return render(request,'shop_app/shop-left-sidebar.html')
    
def product_detail(request):
    return render(request,'shop_app/shop-details.html')

def cart(request):
    return render(request,'shop_app/cart.html')

def checkout(request):
    return render(request,'shop_app/checkout.html')

def terms_and_privacy(request):
    return render(request,'shop_app/terms-of-service.html')

def contact_us_and_store_location(request):
    return render(request,'shop_app/contact.html')
