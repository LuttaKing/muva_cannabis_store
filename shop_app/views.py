from unicodedata import category
from django.shortcuts import render
from .models import Category,Tag,Product
from django.core.paginator import Paginator

def filter_products(request,products,all_categories,all_tags):

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 1)


    # filter by category
    if request.GET.get('filter_category'):
        for category in all_categories:
            if request.GET.get('filter_category')==category.name:
                filtered_products = products.filter(category__id=category.pk)
                paginato = Paginator(filtered_products, 1)
                productx=paginato.get_page(page)

                return productx
    
    # filter by tag
    if request.GET.get('filter_tag'):
        for tag in all_tags:
            if request.GET.get('filter_tag')==tag.name:
                filtered_products = products.filter(tags__id=tag.pk)
                paginato = Paginator(filtered_products, 1)
                productx=paginato.get_page(page)

                return productx

    products=paginator.get_page(page)
    # print(products.paginator.count)

    return products


def shop(request):
    all_categories = Category.objects.all()
    all_tags = Tag.objects.all()
    all_products = Product.objects.all()

    context = {  
    'all_tags':all_tags,
    'all_categories':all_categories,
    'all_products':filter_products(request,all_products,all_categories,all_tags),
    
    }
    return render(request,'shop_app/shop-left-sidebar.html',context)

def home(request):
    return render(request,'shop_app/index.html')

def about(request):
    return render(request,'shop_app/about.html')

    
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
