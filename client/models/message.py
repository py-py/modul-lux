from django.db import models
from django.utils.translation import gettext as _

__all__ = ('ClientMessageModel', )


class ClientMessageModel(models.Model):
    name = models.CharField(verbose_name=_('Имя клиента'), max_length=255)
    email = models.CharField(verbose_name=_('Почтовый адрес клиента'), max_length=255)
    message = models.TextField(verbose_name=_('Сообщение'))

    is_done = models.BooleanField(verbose_name=_('Обработано'), default=False)

    def __str__(self):
        return _('{self.name}, отработано: {self.is_done}'.format(self=self))
