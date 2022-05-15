from django.db import models
from accounts.models import Profile
from video.models import Video
from comment.models import Comment 


# Create your models here.
class Like(models.Model):

    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="comments_likes")    
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="videos_likes")
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="user_likes")

    