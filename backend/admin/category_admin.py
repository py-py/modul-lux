from django.contrib import admin

from backend.models import Furniture, CategoryImage

__all__ = ('CategoryAdmin', 'CategoryImageAdmin',)


class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'image', 'is_default', )


class FurnitureInline(admin.TabularInline):
    model = Furniture


class CategoryImageTabularInLine(admin.TabularInline):
    model = CategoryImage


class CategoryAdmin(admin.ModelAdmin):
    # inlines = (FurnitureInline, CategoryImageTabularInLine, )
    inlines = (FurnitureInline, )
    pass
