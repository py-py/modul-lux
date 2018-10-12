from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group


class ModulLuxSite(admin.AdminSite):
    site_header = _('Modul-Lux Admin')
    site_title = _('Modul-lux Admin')
    pass

admin_modullux = ModulLuxSite()
admin_modullux.register(User, UserAdmin)
admin_modullux.register(Group, GroupAdmin)
