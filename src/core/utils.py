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


def upload_to_username(instance ,filename):
    extension=os.path.splitext(instance.video.path)[1]
    return(f"{instance.sharer.user.username}/{instance.subject}.{extension}")


def upload_image_to_username(instance ,filename):
    return(f"{instance.sharer.user.username}/{instance.subject}")