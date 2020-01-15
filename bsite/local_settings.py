

from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GhitaAlexandruIo$blog',
        'USER': 'GhitaAlexandruIo',
        'PASSWORD': 'GreenArrow',
        'HOST': 'GhitaAlexandruIon.mysql.pythonanywhere-services.com',
        'PORT': '',

    }
}

