from django.db import models
from django.conf import settings 
from django.urls import reverse 


class Profile(models.Model):
    image=models.ImageField(upload_to="profiles/%Y/%m/%d",null=True,blank=True)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

#    def get_absolute_url(self):
#        return reverse("")


    def __str__(self):
        return(self.user)
