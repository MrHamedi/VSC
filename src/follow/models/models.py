from django.db import models
from accounts.models import Profile
# Create your models here.


class Follow(models.Model):

    follower=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="followers")
    following=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="followings")

    