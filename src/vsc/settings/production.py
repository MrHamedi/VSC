from core.utils import get_secret
from .base import *

SECRET_KEY = get_secret("SECRET_KEY")
DEBUG = False

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = get_secret("EMAIL_USERNAME")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True