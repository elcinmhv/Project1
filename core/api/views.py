from .serialisers import BlogSerialiser
from rest_framework.generics import (
    ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    
    )
from core.models import Blog
from rest_framework.permissions import BasePermission,SAFE_METHODS
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return False

class BlogListAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerialiser
    permission_classes=[
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
        CustomPermission,
    ]

    # def get_queryset(self):
    #     queryset=Blog.objects.all()
    #     title=self.request.query_params.get("blog_search",None)
    #     if title is not None:
    #         queryset=queryset.filter(title__icontains=title)
    #     return queryset

class BlogRetrieveAPIView(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerialiser
    lookup_field='id'

class BlogCreateAPIView(CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerialiser

class BlogUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerialiser
    lookup_field='id'
    permission_classes=[
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
        # CustomPermission,
    ]

class BlogDestroyAPIView(RetrieveDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerialiser
    lookup_field='id'
    lookup_url_kwarg='nosun'  #sadece id olsun slug olsun adini burdan teyin ede bilirik,
                              #ama bunu qoymasaq avtamatik olaraq lookup_fieldinde ne yazmisiqsa onu qoyur ve urlye yaziriq
    



# class GENERALAPIView(APIView):
#     def get(self,request):
#         data = {"message": "GET isteği başarıyla işlendi"}
#         return Response(data, status=status.HTTP_200_OK)






