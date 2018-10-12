from django.db import models
from django.utils.translation import gettext as _

from backend.models.base import BaseImageAdmin

__all__ = ('Furniture', 'FurnitureImage', )


class FurnitureImage(BaseImageAdmin):
    furniture = models.ForeignKey('backend.Furniture', on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Изображение мебели')
        verbose_name_plural = _('Изображения мебели')

    def __str__(self):
        return _('Изображение мебели {}'.format(self.furniture.name))

    def save(self, *args, **kwargs):
        if self.is_default:
            try:
                default_category_image = self.furniture.images.get(is_default=True)
            except Furniture.DoesNotExist:
                pass
            else:
                default_category_image.is_default = False
                default_category_image.save()
        else:
            if not self.furniture.images.count():
                self.is_default = True
        super().save(*args, **kwargs)

class Furniture(models.Model):
    name = models.CharField(verbose_name=_('Наименование'), max_length=255)
    category = models.ForeignKey('backend.Category', verbose_name=_('Категория'), on_delete=models.CASCADE, related_name='furnitures')

    class Meta:
        verbose_name = _('Мебель')
        verbose_name_plural = _('Мебели')

    def __str__(self):
        return '{}'.format(self.name)
