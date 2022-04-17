from django.db import models
from accounts.models.profile import Profile
from core.models import CommonPostableFields
from core.utils import upload_to_username
from video.utils.video_splitter import video_splitter
from django.urls import reverse


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

    def save(self,*args,**kwargs):
        super(Video,self).save(*args,**kwargs)
        if not self.image:
            video_splitter(self)