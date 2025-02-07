"""
WSGI config for edstack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0,"/home/edstdvgy/public_html/edstack-mvp-one-backend")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edstack.settings')

application = get_wsgi_application()
