from django.db import models
from django.utils.translation import gettext as _

from backend.models.base import *

__all__ = ('Category', 'CategoryImage',)


class CategoryImage(BaseImageModel):
    category = models.ForeignKey('backend.Category', on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Изображение категории')
        verbose_name_plural = _('Изображения категорий')

    def __str__(self):
        return _('Изображение категории {}'.format(self.category.name))

    def save(self, *args, **kwargs):
        if self.is_default:
            try:
                default_category_image = self.category.images.get(is_default=True)
            except Category.DoesNotExist:
                pass
            else:
                default_category_image.is_default = False
                default_category_image.save()
        else:
            if not self.category.images.count():
                self.is_default = True
        super().save(*args, **kwargs)


class Category(BaseItemModel):

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return '{}'.format(self.name)
