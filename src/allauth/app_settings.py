from django.conf import settings


SITES_ENABLED = "django.contrib.sites" in settings.INSTALLED_APPS
SOCIALACCOUNT_ENABLED = "allauth.socialaccount" in settings.INSTALLED_APPS



USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")

ACCOUNT_EMAIL_VERIFICATION ="mandatory"
