import os 
from django.core.exceptions import ImproperlyConfigured

def get_secret(data):
    """
        Will read secret data from environment
    """
    try:
        data=os.environ[data]
        return data
    except KeyError:
        raise ImproperlyConfigured(f'Please insert {data} value into environment!!!')