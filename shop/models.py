from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from phonenumber_field.modelfields import PhoneNumberField
from shop.managers import UserManager
class CustomUser(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(verbose_name="Ism",max_length=100)
    last_name =models.CharField(verbose_name="Familya",max_length=100)
    phone_number =PhoneNumberField(verbose_name="Telefon raqam",null=True,blank = True,unique=True)
    profile_image = models.ImageField(verbose_name="Profil rasmi",upload_to="profiles/",null=True,blank=True)
    adress=models.CharField(verbose_name="Yashash manzili",max_length=255)
    is_staff = models.BooleanField(verbose_name="Xodimlik statusi",default=False)
    is_superuser=models.BooleanField(verbose_name="Superadminlik statusi",default=False)
    is_active=models.BooleanField(verbose_name="Profil aktivlik holati",default=True)
    objects=UserManager()



    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
class Catagory(models.Model):
    name=models.CharField(verbose_name="Katagoriya nomi",max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id=models.UUIDField(verbose_name="ID",primary_key=True,unique=True,editable=False,default=uuid4)
    name=models.CharField(verbose_name="Maxsulot nomi",max_length=100)
    catagory = models.ForeignKey(to=Catagory,on_delete=models.PROTECT)
    price=models.DecimalField(verbose_name="Maxsulot narxi",max_digits=12,decimal_places=2)
    image=models.ImageField(verbose_name="Maxsulot rasmi",upload_to="products/")
    description = models.TextField(verbose_name="Tarif",blank=True, null=True)
    is_available = models.BooleanField(verbose_name="bormi_yo'q",default=True)
    in_stock=models.IntegerField(verbose_name="Ombordagi soni",default=1)
    

    def __str__(self):
        return self.name