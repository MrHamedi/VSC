from tabnanny import verbose
from django.db import models
from django.conf import settings 
from django.urls import reverse 
from ..utils import image_adress_finder


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE ,related_name='profile')
    image=models.ImageField(upload_to=image_adress_finder,null=True,blank=True)


    class Meta:
        verbose_name="پروفایل"
        verbose_name_plural="پروفایل ها"

    def __str__(self):
        return(self.user.username)

    @property
    def get_image(self):
        
        if(self.image): 
            return self.image.url
        
        else:
            return "/static/account/images/default_client_pic.png"