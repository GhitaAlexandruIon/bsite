"""
WSGI config for bsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import bsite.local_settings
from django.core.wsgi import get_wsgi_application

DJANGO_SETTINGS_MODULE = bsite.local_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsite.settings')

application = get_wsgi_application()
