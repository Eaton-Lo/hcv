"""
WSGI config for hcv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise #heroku add

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hcv.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application) #heroku add
