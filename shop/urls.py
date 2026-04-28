from django.urls import path
from .views import products, register

urlpatterns = [
    path('', products, name='products'),
    path('register/', register, name='register'),

    # 🔥 YANGI QATOR
    path('product/<uuid:pk>/', products, name='product_detail'),
]