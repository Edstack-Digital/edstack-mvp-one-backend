# passenger_wsgi.py
import os
import sys

VENV_PATH = '/home/edstdvgy/virtualenv/edstack-mvp-one-backend/3.9/lib/python3.x/site-packages'
if VENV_PATH not in sys.path:
    sys.path.insert(0, VENV_PATH)

# Add your project directory to system path
PROJ_PATH = '/home/edstdvgy/edstack-mvp-one-backend'
if PROJ_PATH not in sys.path:
    sys.path.insert(0, PROJ_PATH)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edstack.settings')

# Import and create the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

