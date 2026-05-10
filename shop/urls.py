from django.urls import path
from shop.views import *

urlpatterns = [
    path('', products, name='products'),

    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),

    path('product/<uuid:id>/', product_detail, name='product_detail'),

    path('profile/', profile, name='profile'),
    path('cart/', cart, name='cart'),
    path('transactions/', transactions, name='transactions'),

    path('cart/delete/<int:id>/', delete_cart_product, name='delete_cart_product'),

    path('buy/', buy, name='buy'),
]