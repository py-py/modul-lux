from django.contrib import admin

from backend.models import Product, CategoryImage

__all__ = ('CategoryAdmin', 'CategoryImageAdmin',)


class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'image', 'is_default', )


class CategoryImageTabularInLine(admin.TabularInline):
    model = CategoryImage


class ProductInline(admin.TabularInline):
    model = Product
    max_num = 1


class CategoryAdmin(admin.ModelAdmin):
    # inlines = (FurnitureInline, CategoryImageTabularInLine, )
    # inlines = (FurnitureInline, )
    pass
