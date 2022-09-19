from .models import Category,Tag,Product
from django.core.paginator import Paginator
from django.shortcuts import render
from itertools import chain

all_categories = Category.objects.all()
all_tags = Tag.objects.all()
all_products = Product.objects.all().order_by("id")

def filter_products(request):
    page = request.GET.get('page', 1)

    # if request.method == 'POST':
    #     search_term = request.POST.get("search_term")
        
    #     searched_products=all_products.filter(name__contains=search_term,)
    #     print(searched_products)
    #     paginato = Paginator(searched_products, 1)
    #     productx=paginato.get_page(page)
    #     return productx
    

    if request.GET.get('filter'):
        for item in list(chain(all_categories,all_tags)):
            if request.GET.get('filter')==item.name:
                if item in all_categories:
                    filtered_products = all_products.filter(category__id=item.pk).order_by("id")
                else:
                    filtered_products = all_products.filter(tags__id=item.pk).order_by("id")
                
                paginato = Paginator(filtered_products, 1)
                productx=paginato.get_page(page)

                return productx

    paginator = Paginator(all_products, 1)
    products=paginator.get_page(page)
    print(products.paginator.per_page)

    return products


def shop(request):
    

    context = {  
    'all_tags':all_tags,
    'all_categories':all_categories,
    'all_products':filter_products(request),
    
    }
    return render(request,'shop_app/shop.html',context)

def search(request):
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        search_term = request.POST.get("search_term")
        
        searched_products=all_products.filter(name__contains=search_term,)
        paginato = Paginator(searched_products, 1)
        productx=paginato.get_page(page)
        context = {  
            'all_tags':all_tags,
            'all_categories':all_categories,
            'all_products':productx,
            
            }
        return render(request,'shop_app/search_shop.html',context)

    if request.GET.get("search_term"):
        search_term = request.GET.get("search_term")
        searched_products=all_products.filter(name__contains=search_term,)
        paginato = Paginator(searched_products, 1)
        productx=paginato.get_page(page)
        context = {  
                'all_tags':all_tags,
                'all_categories':all_categories,
                'all_products':productx,
                
                }
        return render(request,'shop_app/shop.html',context)
    else:

        context = {  
            'all_tags':all_tags,
            'all_categories':all_categories,
            'all_products':filter_products(request),
            
            }
        return render(request,'shop_app/shop.html',context)