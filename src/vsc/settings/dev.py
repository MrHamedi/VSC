from .base import *
from core.utils import get_secret


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware', ]+MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "vsc_db",
        'USER': get_secret("DB_USER"),
        "PASSWORD": get_secret("DB_PASSWORD"),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

USE_TZ = False
TIME_ZONE = 'Asia/Tehran'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = get_secret("EMAIL_USERNAME")
    EMAIL_HOST_PASSWORD = get_secret("EMAIL_PASSWORD")
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True


INSTALLED_APPS += [
    'debug_toolbar'
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
