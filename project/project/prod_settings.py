import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '(s&^w-3hmx@9x53u+8#x#o9e*ez&zpmmog*irqph1mjto!c0j3'

CART_SESSION_ID = 'cart'

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'u1145832_default',
        'USER': 'u1145832',
        'PASSWORD': '123456',
        'HOST': 'N!_66BLw',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = (
     os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = 'static/'
