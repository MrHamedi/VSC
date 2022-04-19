from django.db import models
from video.models import Video 
from core.models import CommonPostableFields
# Create your models here.


class Comment(CommonPostableFields):

    commentType=(('c','comment on comment'),('v','comment on video'))
    content=models.CharField(max_length=500)
    video=models.ForeignKey(Video,on_delete=models.CASCADE,related_name="video_comments" ,blank=True ,null=True)
    related_comment=models.ForeignKey('Comment',on_delete=models.CASCADE,related_name="comment_comments" ,blank=True ,null=True)
    comment_type=models.CharField(choices=commentType,max_length=1)

    class Meta:
        ordering=("-create_date",)
        verbose_name="کامنت"
        verbose_name_plural="کامنت ها"

    def __str__(self):
        return(self.content)