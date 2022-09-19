from .models import Category,Tag,Product
from django.core.paginator import Paginator
from django.shortcuts import render
from itertools import chain


def filter_products(request,products,all_categories,all_tags):

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 1)

    if request.GET.get('filter'):
        for item in list(chain(all_categories,all_tags)):
            if request.GET.get('filter')==item.name:
                if item in all_categories:
                    filtered_products = products.filter(category__id=item.pk).order_by("id")
                else:
                    filtered_products = products.filter(tags__id=item.pk).order_by("id")
                
                paginato = Paginator(filtered_products, 1)
                productx=paginato.get_page(page)

                return productx

    # # filter by category
    # if request.GET.get('filter_category'):
    #     for category in all_categories:
    #         if request.GET.get('filter_category')==category.name:
    #             filtered_products = products.filter(category__id=category.pk)
    #             paginato = Paginator(filtered_products, 1)
    #             productx=paginato.get_page(page)

    #             return productx
    
    # # filter by tag
    # if request.GET.get('filter_tag'):
    #     for tag in all_tags:
    #         if request.GET.get('filter_tag')==tag.name:
    #             filtered_products = products.filter(tags__id=tag.pk)
    #             paginato = Paginator(filtered_products, 1)
    #             productx=paginato.get_page(page)

    #             return productx

    products=paginator.get_page(page)
    print(products.paginator.per_page)

    return products


def shop(request):
    all_categories = Category.objects.all()
    all_tags = Tag.objects.all()
    all_products = Product.objects.all().order_by("id")

    context = {  
    'all_tags':all_tags,
    'all_categories':all_categories,
    'all_products':filter_products(request,all_products,all_categories,all_tags),
    
    }
    return render(request,'shop_app/shop-left-sidebar.html',context)