from django.conf import settings


def enable_options(request):
    status = getattr(settings, 'ENABLE_SITE_OPTIONS', False)
    return {'enable_options': status}
