from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Cart
from django.contrib import messages 
import decimal

@login_required
def cart(request):
    owner = request.user
    cart_products = Cart.objects.filter(owner=owner)
        # Display Total on Cart Page
    amount = decimal.Decimal(0)
    if cart_products.count() > 0:
        shipping_amount = decimal.Decimal(20)
    else:
         shipping_amount = decimal.Decimal(0)
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all() if p.owner==owner]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.product.price)
            amount += temp_amount

    context = {"cart_products":cart_products,'shipping_amount':shipping_amount,'sub_total_amount': amount,'total_amount': amount+shipping_amount}
    return render(request,'shop_app/cart.html',context)


@login_required
def add_to_cart(request,id):
    owner = request.user
    product = get_object_or_404(Product, id=id)

    # Check whether the Product is alread in Cart or Not
    item_already_in_cart = Cart.objects.filter(product=id, owner=owner)
    if item_already_in_cart:
        messages.add_message(request,messages.ERROR, "Item already in cart")
        print('item already in cart')

    else:
        Cart(owner=owner, product=product).save()
        messages.add_message(request,messages.ERROR, "Item added to your cart")
    
    return redirect('cart')

@login_required
def plus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        cp.quantity += 1
        cp.save()
    return redirect('cart')


@login_required
def minus_cart(request, cart_id):
    if request.method == 'GET':
        cp = get_object_or_404(Cart, id=cart_id)
        # Remove the Product if the quantity is already 1
        if cp.quantity == 1:
            cp.delete()
        else:
            cp.quantity -= 1
            cp.save()
    return redirect('cart')

@login_required
def delete_cart(request, cart_id):
    if request.method == 'GET':
        c = get_object_or_404(Cart, id=cart_id)
        c.delete()
        messages.add_message(request,messages.ERROR, "Item removed cart")
    return redirect('cart')

