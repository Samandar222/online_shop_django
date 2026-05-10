from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from shop.models import Product, User, Cart, Transaction


# ---------------- PRODUCTS ----------------
def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


# ---------------- SIGN IN ----------------
def signin(request):

    if request.user.is_authenticated:
        return redirect("products")

    if request.method == "POST":

        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")

        user = authenticate(
            request,
            phone_number=phone_number,
            password=password
        )

        print(user)

        if user is not None:
            login(request, user)
            return redirect("products")

        messages.error(request, "Telefon yoki parol xato")
        return redirect("signin")

    return render(request, "auth.html")
# ---------------- SIGN OUT ----------------
def signout(request):
    logout(request)
    return redirect("products")


# ---------------- SIGN UP ----------------
def signup(request):

    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm_password")

        if not first_name or not last_name or not phone_number or not password1 or not password2:
            messages.error(request, "Barcha maydonlarni to'ldiring")
            return redirect("signup")

        if password1 != password2:
            messages.error(request, "Parollar mos emas")
            return redirect("signup")

        if User.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Bu telefon raqam mavjud")
            return redirect("signup")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password1
        )

        messages.success(request, "Muvaffaqiyatli ro'yxatdan o'tdingiz")
        return redirect("signin")

    return render(request, "auth.html")


# ---------------- PRODUCT DETAIL ----------------
def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("signin")

        quantity = int(request.POST.get("quantity"))

        cart_object = Cart.objects.filter(
            user=request.user,
            product=product
        ).first()

        if cart_object is None:

            Cart.objects.create(
                user=request.user,
                product=product,
                count=quantity
            )

            messages.success(request, "Savatchaga qo'shildi")

        else:

            cart_object.count += quantity
            cart_object.save()

            messages.success(request, "Savatcha yangilandi")

    return render(request, "product_detail.html", {
        "product": product
    })


# ---------------- PROFILE ----------------
@login_required
def profile(request):
    return render(request, "profile.html")


# ---------------- CART ----------------
@login_required
def cart(request):

    cart_objects = request.user.cart_set.all()

    return render(request, "cart.html", {
        "cart_objects": cart_objects
    })


# ---------------- TRANSACTIONS ----------------
@login_required
def transactions(request):

    transactions = Transaction.objects.filter(
        user=request.user
    )

    return render(request, "transactions.html", {
        "transactions": transactions
    })


# ---------------- DELETE CART PRODUCT ----------------
@login_required
def delete_cart_product(request, id):

    cart_object = request.user.cart_set.filter(id=id).first()

    if cart_object:
        cart_object.delete()

    return redirect("cart")


# ---------------- BUY ----------------
@login_required
def buy(request):

    cart_objects = request.user.cart_set.all()

    for cart_object in cart_objects:

        Transaction.objects.create(
            user=request.user,
            amount=cart_object.product.price * cart_object.count,
            product_name=f"{cart_object.product.name} x{cart_object.count}"
        )

    cart_objects.delete()

    messages.success(request, "Sotib olindi")

    return redirect("transactions")