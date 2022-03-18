from django.db import models
from accounts.models.profile import Profile
from core.models import CommonPostableFields
from core.utils import upload_to_username



class Video(CommonPostableFields):

    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="videos")
    video=models.FileField(upload_to=upload_to_username)
    slug=models.SlugField(unique=True ,max_length=300 ,default='slug_maker()')
    subject=models.CharField(max_length=150)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return(self.subject)

    @property
    def slug_maker(self):
        return f"{self.profile.user.username}/{self.subject}/"
