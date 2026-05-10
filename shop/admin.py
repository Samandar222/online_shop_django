from django.contrib import admin
from django.contrib.auth.models import Group

from shop.models import Category, Product, User, Cart, Transaction


# ADMIN PANEL TEXT
admin.site.site_header = "Boshqaruv paneli"
admin.site.site_title = "Admin panel"
admin.site.index_title = "Online do'konga xush kelibsiz"


# GROUPNI OLIB TASHLASH
admin.site.unregister(Group)


# MODELLARNI REGISTER QILISH
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Transaction)