from .prod import *

ALLOWED_HOSTS += ['valeev0506624980.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'valeev0506624980$modullux',
        'USER': 'valeev0506624980',
        'PASSWORD': 'modulpassword',
        'HOST': 'valeev0506624980.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}