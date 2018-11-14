from .prod import *

SECRET_KEY = 'p)d1@8z3ynm7duiu_@nc$j+!x*o(naye8e35g%^xlg-@yha_%%'
ALLOWED_HOSTS += ['valeev0506624980.pythonanywhere.com']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'valeev0506624980$default',
        'USER': 'valeev0506624980',
        'PASSWORD': 'modulpassword',
        'HOST': 'valeev0506624980.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
