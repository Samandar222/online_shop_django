from django.contrib import admin
from django.contrib.auth.models import Group
from shop.models import Category,Product

admin.site.site_header ="Boshqaruv paneli"
admin.site.site_title="Online dokonga xush kelibsiz | admin panle"
admin.site.index_title="Online do'kon admin"



admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Product)
