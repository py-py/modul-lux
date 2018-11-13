from django.contrib import admin
from backend.models import ProductImage

__all__ = ('ProductAdmin', 'ProductImageAdmin',)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'image', 'is_default')


class ProductImageInlineAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageInlineAdmin, )
    list_display = ('__str__', 'category', 'default_image')
