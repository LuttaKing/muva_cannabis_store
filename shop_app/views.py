
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product

def home(request):
    return render(request,'shop_app/index.html')

def about(request):
    return render(request,'shop_app/about.html')

    
def product_detail(request,id):

    product = get_object_or_404(Product,pk=id)
    category_ID = None
    for category in product.category.all():
        category_ID=category.id
    related_products = Product.objects.exclude(id=product.id).filter(category__id=category_ID)[:3]
    print(related_products)
    context = {'product':product, 'related_products': related_products,}
    return render(request,'shop_app/shop-details.html',context)



def checkout(request):
    return render(request,'shop_app/checkout.html')

def terms_and_privacy(request):
    return render(request,'shop_app/terms-of-service.html')

def contact_us_and_store_location(request):
    return render(request,'shop_app/contact.html')
