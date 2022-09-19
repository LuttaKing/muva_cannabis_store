
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product

def home(request):
    return render(request,'shop_app/index.html')

def about(request):
    return render(request,'shop_app/about.html')

    
def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)
    # for i in product.category.all():
    #     print(i.name)
    context = {'product':product}
    return render(request,'shop_app/shop-details.html',context)

def cart(request):
    return render(request,'shop_app/cart.html')

def checkout(request):
    return render(request,'shop_app/checkout.html')

def terms_and_privacy(request):
    return render(request,'shop_app/terms-of-service.html')

def contact_us_and_store_location(request):
    return render(request,'shop_app/contact.html')
