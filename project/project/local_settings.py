import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '(s&^w-3hmx@9x53u+8#x#o9e*ez&zpmmog*irqph1mjto!c0j3'

CART_SESSION_ID = 'cart'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (
     os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
