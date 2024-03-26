from django.urls import path
from core.views import index,contact,blog,blogdetails,elements,tracking,category,singleproduct,checkout,cart,faq
from django.conf import settings
from core import views
from django.views.i18n import set_language




urlpatterns=[
   path('',index,name='index'),
   path('contact/',contact,name='contact'),
   path('blog/',blog,name='blog'),
   path('blogdetails/<slug:blog_slug>/',blogdetails,name='blogdetails'),
   path('elements/',elements,name='elements'),
   path('tracking/',tracking,name='tracking'),
   path('category/',category,name='category'),
   path('singleproduct/',singleproduct,name='single-product'),
   path('checkout/',checkout,name='checkout'),
   path('cart/',cart,name='cart'),
   path('faq/', faq, name='faq'),
   path('set_language',set_language,name='set_language')

   

   
]

