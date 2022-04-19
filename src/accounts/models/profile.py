from tabnanny import verbose
from django.db import models
from django.conf import settings 
from django.urls import reverse 


class Profile(models.Model):
    image=models.ImageField(upload_to="profiles/%Y/%m/%d",null=True,blank=True)
    user=models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE ,related_name='profile')

    class Meta:
        verbose_name="پروفایل"
        verbose_name_plural="پروفایل ها"

    def __str__(self):
        return(self.user.username)
