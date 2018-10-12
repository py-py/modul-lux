from django.contrib import admin

__all__ = ('FurnitureAdmin', 'FurnitureImageAdmin',)


class FurnitureImageAdmin(admin.ModelAdmin):
    pass


class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'images')

