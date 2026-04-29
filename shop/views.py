from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from shop.models import Product


@login_required
def products(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password != confirm_password:
            messages.error(request, "Parollar mos emas!")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bunday username mavjud!")
            return redirect("register")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tildi!")
        return redirect("login")

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("products")
        else:
            messages.error(request, "Login yoki parol noto‘g‘ri!")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_detail.html", {"product": product})