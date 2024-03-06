from django.contrib import admin
from core.models import Category,Product,Color
# Register your models here.

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Color)



class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','category','get_colors','size']
    search_fields=['name','price','category__name','color__name','size',]
    list_filter=['category','color','price','size']
    ordering=['price','category']
    readonly_fields=['like']
    fieldsets=(
        ('Main Information', {
            'fields':('name','price','category','color','size') 
        }),
        ('Additional Information', {
            'fields':('like',)
        }),
    )
      
    def get_colors(self, obj):
        return ', '.join([color.name for color in obj.color.all()])
    get_colors.short_description = 'Colors'
    



admin.site.register(Product,ProductAdmin)