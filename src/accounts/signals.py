from . import models 
from django.dispatch import receiver
from django.db.models import signals 
from django.conf import settings 



@receiver(signals.post_save,sender=settings.AUTH_USER_MODEL)
def create_profile(sender,instance,created,**kwargs):
    """
        This signal creates a profile for 
        user  each time a user signs up.
    """
    if not created:
        return
    profile=models.Profile.objects.create(user=instance)