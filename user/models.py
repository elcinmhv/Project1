from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



user_type=(
    ('admin','Admin'),
    ('customer','Customer'),
    ('user','User'),
    ('menejer','Menejer')
    
    )








class MyUser(AbstractUser):
    phone=models.CharField(max_length=15,blank=True,null=True)
    address=models.CharField(max_length=255,blank=True,null=True)
    country=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    date_of_birth=models.DateField(blank=True,null=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True,null=True)
    user_role=models.CharField(max_length=100,choices=user_type,default='customer',blank=True,null=True)
