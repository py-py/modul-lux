from django.db import models
from django.utils.translation import gettext as _

from backend.models.base import *

__all__ = ('Product', 'ProductImage',)


class ProductImage(BaseImageModel):
    product = models.ForeignKey('backend.Product', on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Изображение товара')
        verbose_name_plural = _('Изображения товаров')

    def __str__(self):
        return _('Изображение товара {}'.format(self.product.name))

    def save(self, *args, **kwargs):
        if self.is_default:
            try:
                default_category_image = self.product.images.get(is_default=True)
            except Product.DoesNotExist:
                pass
            else:
                default_category_image.is_default = False
                default_category_image.save()
        else:
            if not self.product.images.count():
                self.is_default = True
        super().save(*args, **kwargs)


class Product(BaseItemModel):
    size = models.CharField(verbose_name=_('Размеры'), max_length=255, null=True, blank=True)
    category = models.ForeignKey('backend.Category', verbose_name=_('Категория'), on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return '{}'.format(self.name)
