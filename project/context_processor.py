from django.conf import settings


def options(request):
    options = getattr(settings, 'SITE_OPTIONS', {})
    return {'options': options}
