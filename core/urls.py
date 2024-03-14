from django.urls import path
from core.views import index,contact,blog,blogdetails,elements,tracking,category,singleproduct,checkout,cart
from django.conf.urls.static import static
from django.conf import settings



urlpatterns=[
   path('',index,name='index'),
   path('contact/',contact,name='contact'),
   path('blog/',blog,name='blog'),
   path('blogdetails/<int:blog_id>/',blogdetails,name='blogdetails'),
   path('elements/',elements,name='elements'),
   path('tracking/',tracking,name='tracking'),
   path('category/',category,name='category'),
   path('singleproduct/',singleproduct,name='single-product'),
   path('checkout/',checkout,name='checkout'),
   path('cart/',cart,name='cart')
   

   
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)