"""
WSGI config for gpsonlineweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

# add the path to the folder
sys.path.append('/home/server/Documentos/gpsonline/onlinegpsweb')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlinegpsweb.settings")

application = get_wsgi_application()
