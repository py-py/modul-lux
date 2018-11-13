from django.contrib import admin

from backend.models import Product, CategoryImage

__all__ = ('CategoryAdmin', 'CategoryImageAdmin',)


class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'image', 'is_default', )


class CategoryImageInlineAdmin(admin.TabularInline):
    model = CategoryImage
    extra = 1


class ProductInlineAdmin(admin.TabularInline):
    model = Product
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryImageInlineAdmin, ProductInlineAdmin, )
