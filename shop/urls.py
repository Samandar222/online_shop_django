from django.urls import path
from .views import products, register, login_view, logout_view, product_detail

urlpatterns = [
    path('products/', products, name='products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('', products, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]