from django.db import models
from django.utils.translation import gettext as _

__all__ = ('BaseImageAdmin',)


class BaseImageAdmin(models.Model):
    image = models.ImageField(verbose_name=_('Изображение'))
    is_default = models.BooleanField(verbose_name=_('Изображение по-умолчанию'), default=False)

    class Meta:
        abstract = True

