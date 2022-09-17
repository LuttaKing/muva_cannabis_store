from django.shortcuts import render

def handle_404n(request,exception):

    return render(request,'shop_app/error-404.html')

def handle_500(request):
    
    return render(request,'shop_app/error-404.html')