from random import randrange
from .models import Video 
from django.dispatch import receiver
from django.db.models import signals
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify



@receiver(signals.post_save,sender=Video)
def slug_maker(sender,instance,created,**kwargs):
    if not created:
        return      
    slug=slugify(f"{instance.sharer.user.username} {instance.subject} {instance.id}")
    instance.slug=slug
    instance.save()
