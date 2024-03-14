from typing import Iterable
from django.db import models
from django.utils.translation import gettext as _
# from django.utils import timezone
from datetime import datetime
from django.db.models import F 


SIZE=(
    ('XS','Extra Small'),
    ('S','Small'),
    ('M','Medium'),
    ('L','Large'),
    ('XL','Extra Large')
)

# Create your models here.
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        abstract=True


class Category(BaseModel):
    name=models.CharField(max_length=50 )
    class Meta:
        verbose_name=_('Category')
        verbose_name_plural=_('Categories')
   
    

    def __str__(self):
        formatted_date = datetime.strftime(self.created_at, '%y,%m,%d-%H:%M:%S')
        return f'{self.name}-{formatted_date}'
        # return f"{self.name} - {timezone.localtime(self.created_at)}"
    
    
class Color(BaseModel):
    name=models.CharField(max_length=50)
    class Meta:
        verbose_name=_('Color')
        verbose_name_plural=_('Colors')

    def __str__(self):
        return self.name



class Product(BaseModel):
    name=models.CharField(max_length=50)
    price=models.FloatField(help_text='ancaq reqem yazilmalidir')
    color=models.ManyToManyField(Color,)
    size=models.CharField(max_length=50,choices=SIZE,default='M')
    like=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        verbose_name=_('Product')
        verbose_name_plural=_('Products')

    def __str__(self):
        return self.name
    
    def pricename(self):
        return f'{self.name}-{self.price} AZN'
    def save(self,*args,**kwargs):
        self.name=self.name.title()
        return super(Product,self).save(*args,**kwargs)
    @classmethod
    def increaseprice(cls):
        cls.objects.update(price=F('price')+5)
Product.increaseprice() 

class Blog(BaseModel):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='media/blog/')
    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'
        ordering=('created_at',)
    def __str__(self):
        return self.title
    def format_created_at1(self):
        return self.created_at.strftime('%d')
    def format_created_at2(self):
        return self.created_at.strftime('%b')
    
class Contact(BaseModel):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    working_time=models.CharField(max_length=50)
    email=models.EmailField()
    text=models.TextField()
    
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
    def __str__(self):
        return self.name


    
    

