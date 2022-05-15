from .base import *
from core.utils import get_secret


DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")


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


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

