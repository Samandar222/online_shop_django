
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('',include('shop.urls')),
=======
    path('',include('app_main.urls')),
>>>>>>> b28dc618bbe0e93dc77b20463093319466e0a566
]
