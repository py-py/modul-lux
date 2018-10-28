from django.conf import settings


def options(request):
    options = getattr(settings, 'SITE_OPTIONS', {})
    return {'options': options}


def site_settings(request):
    site_settings = getattr(settings, 'SITE_SETTINGS', {})
    return {'site_settings': site_settings}
