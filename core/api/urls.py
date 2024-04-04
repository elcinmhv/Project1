from django.urls import path
from .views import (
    BlogListAPIView,BlogRetrieveAPIView,BlogCreateAPIView,BlogDestroyAPIView,BlogUpdateAPIView
    
    )













urlpatterns=[

    path('blogs/',BlogListAPIView.as_view(),name='blog-list'),
    path('blogs/<int:id>/',BlogRetrieveAPIView.as_view({'get': 'list'}),name='blog-detail'),
    path('blogs/create/',BlogCreateAPIView.as_view(),name='blog-create'),
    path('blogs/<int:id>/update/',BlogUpdateAPIView.as_view(),name='blog-update'),
    path('blogs/<int:nosun>/delete/',BlogDestroyAPIView.as_view(),name='blog-delete'),

]