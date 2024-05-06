from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from core.models import (
    Category,Product,Color,Blog,Contact,Setting,ContactUs,
    FAQ,Subscriber
)
from modeltranslation.admin import TranslationAdmin
from excel_response import ExcelResponse
# Register your models here.

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(ContactUs)
admin.site.register(Color)
# admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Setting)
# admin.site.register(FAQ)
admin.site.register(Subscriber)






class ProductAdmin(TranslationAdmin):
    list_display=['name','price','category','get_colors','size','slug']
    search_fields=['name','price','category__name','color__name','size',]
    list_filter=['category','color','price','size']
    ordering=['price','category']
    # readonly_fields=['like']
    fieldsets=(
        ('Main Information', {
            'fields':('name','price','description','category','color','size','image','is_active','slug') 
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
# @admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display=['title','slug','created_at']
    fields=['title','description','image','is_active','category']
    actions=['excel_export']

    def excel_export(self, request, queryset):
        data=[]
        for blog in queryset:
            data.append([blog.title, blog.slug, blog.created_at])
        return ExcelResponse(data,output_filename='blogs')
    # excel_export.short_description = "Melumatlari Excele chixartmaq"


class FAQAdmin(TranslationAdmin):
    list_display=['question']
    fields=['question','answer','is_active']


admin.site.register(Blog,BlogAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(FAQ,FAQAdmin)
admin.site.site_header='MaleFashion administration'
admin.site.site_title='MaleFashion administration'


permissions = [("can_deliver_pizzas", "Can deliver pizzas")]
