from uuid import uuid4
from django.db import models

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
    description= models.TextField(verbose_name="Maxsulot tarifi" ,null=True,blank=True)
    in_stock=models.IntegerField(verbose_name="Ombordagi soni",default=1)
    

    def __str__(self):
        return self.name