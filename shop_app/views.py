
from django.contrib import messages 
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product,Order,Cart
from django.contrib.auth.decorators import login_required


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


@login_required
def checkout(request,shipping_amount,subtotal_amount):

    user = request.user
    cart_objects = Cart.objects.filter(owner=user)
    context = {"cart_objects":cart_objects,'shipping_amount':shipping_amount,
    'subtotal_amount': subtotal_amount,'total_amount':int(subtotal_amount)+int(shipping_amount)}


    return render(request,'shop_app/checkout.html',context)

def terms_and_privacy(request):
    return render(request,'shop_app/terms-of-service.html')

def contact_us_and_store_location(request):
    return render(request,'shop_app/contact.html')

@login_required
def order(request):
    if request.POST:
        user = request.user
        address = request.POST.get("address")

        order = Order(user=user,address=address)
        order.save()
        messages.add_message(request,messages.ERROR, "Order added successfully")
        return render(request,'shop_app/order.html')

    messages.add_message(request,messages.ERROR, "No oder placed")
    return render(request,'shop_app/order.html')
