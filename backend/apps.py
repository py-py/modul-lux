from django.apps import AppConfig
from django.utils.translation import gettext as _


class BackendConfig(AppConfig):
    name = 'backend'

    def ready(self):
        self.verbose_name = _('Мебель')
