from django.db import models
from accounts.models.profile import Profile
from core.models import CommonPostableFields
from core.utils import upload_to_username ,upload_image_to_username
from ..utils.set_image import set_image
from ..validators import video_validator
from django.urls import reverse
import os
from taggit.managers import TaggableManager


class Video(CommonPostableFields):

    video=models.FileField(upload_to=upload_to_username ,validators=[video_validator])
    slug=models.SlugField(unique=True ,max_length=300,blank=True ,null=True)
    subject=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to=upload_image_to_username ,null=True ,blank=True)
    tags=TaggableManager()

    class Meta:
        verbose_name="فیلم"
        verbose_name_plural="فیلم ها"
        ordering=('-create_date',)

    def __str__(self):
        return(self.subject)
    
    def get_absolute_url(self):
        return(reverse(
            'video:video_detail',args=[self.sharer.user.username,self.subject,self.id]
        ))

    @property
    def extension_splitter(self):
        return os.path.splitext(self.video.path)[1]

    def save(self,*args,**kwargs):
        super(Video,self).save(*args,**kwargs)
        set_image(self)
