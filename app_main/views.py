from django.shortcuts import render
from app_main.models import Product

def products(request):
    products=Product.objects.all()
    return render(request,"home_page.html",{"products":products})

# Create your views here.
