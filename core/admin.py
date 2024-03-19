from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from core.models import (
    Category,Product,Color,Blog,Contact,Setting,ContactUs
)
# Register your models here.

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(ContactUs)
admin.site.register(Color)
# admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Setting)






class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','category','get_colors','size']
    search_fields=['name','price','category__name','color__name','size',]
    list_filter=['category','color','price','size']
    ordering=['price','category']
    # readonly_fields=['like']
    fieldsets=(
        ('Main Information', {
            'fields':('name','price','category','color','size','is_active') 
        }),
        ('Additional Information', {
            'fields':('like',)
        }),
    )
    def get_readonly_fields(self, request,obj=None):
        if request.user.is_superuser:
            return ()
        return('like','is_active')
    

    def get_queryset(self, request):
        qs=super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_active=True)
      
    def get_colors(self, obj):
        return ', '.join([color.name for color in obj.color.all()])
    get_colors.short_description = 'Colors'


    def delete_model(self, request,obj):
        if not request.user.is_superuser:
            obj.is_active=False
            obj.save()
        else:
            obj.delete()


    def has_delete_permission(self, request,obj=None):
        if request.user.is_superuser:
            return True
        return False
    
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','slug']
    fields=['title','description','image']


admin.site.register(Blog,BlogAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.site_header='MaleFashion administration'