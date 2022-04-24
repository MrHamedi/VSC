from django.db import models
from accounts.models.profile import Profile
from core.models import CommonPostableFields
from core.utils import upload_to_username
from ..utils.set_image import set_image
from ..utils import is_format_valid
from django.urls import reverse
import os


class Video(CommonPostableFields):

    video=models.FileField(upload_to=upload_to_username)
    slug=models.SlugField(unique=True ,max_length=300,blank=True)
    subject=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to=upload_to_username ,null=True ,blank=True)

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
        print(self.video)
        is_format_valid(self.video.path)
        super(Video,self).save(*args,**kwargs)
        set_image(self)
