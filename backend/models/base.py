from django.db import models
from django.utils.translation import gettext as _

__all__ = ('BaseItemModel', 'BaseImageModel',)


class FilteredManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BaseItemModel(models.Model):
    name = models.CharField(verbose_name=_('Наименование'), max_length=255)
    description = models.CharField(verbose_name=_('Описание'), max_length=255, null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_('Активность'), default=True)
    date_added = models.DateField(verbose_name=_('Дата создания продукта'), auto_now_add=True, null=True)
    date_updated = models.DateField(verbose_name=_('Дата последнего изменения продукта'), auto_now=True, null=True)

    active_objects = FilteredManager()

    @property
    def default_image(self):
        return self.images.get(is_default=True)

    class Meta:
        abstract = True


class BaseImageModel(models.Model):
    image = models.ImageField(verbose_name=_('Изображение'))
    is_default = models.BooleanField(verbose_name=_('Изображение по-умолчанию'), default=False)

    class Meta:
        abstract = True
