# -*- coding: utf-8 -*-
import os, sys

sys.path.insert(0, '/var/www/u1145832/data/www/ordocorp.ru/ordo-shop')
sys.path.insert(1, '/var/www/u1145832/data/ordo-shop/venv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ordo-shop.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
