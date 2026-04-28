from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from shop.models import Product


@login_required
def products(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
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