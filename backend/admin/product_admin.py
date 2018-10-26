from django.contrib import admin

__all__ = ('ProductAdmin', 'ProductImageAdmin',)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'image', 'is_default')


class ProductAdmin(admin.ModelAdmin):
    pass

