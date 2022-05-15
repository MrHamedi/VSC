from django.test import TestCase
from django.contrib.auth.models import User
from comment.models import comment 
from video.models import Video
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from .models import Comment
# Create your tests here.


class CommentTest(TestCase):

    def setUp(self):
        user=User.objects.create(username='username',password='password')
        video=open("media/home.mp4","rb")
        video=SimpleUploadedFile("an_example" ,video.read() ,content_type="video/mp4")
        video=Video.objects.create(video=video,subject='example_subject' ,sharer=user.profile)
        comment=Comment.objects.create(content="example comment on video" ,video=video ,comment_type="v" ,sharer=user.profile)
        comment_on_comment=Comment.objects.create(content="example comment on comment" ,related_comment=comment ,comment_type="c" ,sharer=user.profile)

    def test_comment(self):
        comment_on_video=Comment.objects.get(id=1)
        self.assertGreaterEqual(Comment.objects.count(),2)
        self.assertEqual(comment_on_video.content ,"example comment on video")
        self.assertEqual(comment_on_video.comment_type ,"v")
        comment_on_comment=Comment.objects.get(id=2)
        self.assertEqual(comment_on_comment.comment_type,'c')
        self.assertEqual(comment_on_comment.content,"example comment on comment")
        self.assertEqual(comment_on_comment.related_comment,comment_on_video)


    def test_file_deleter(self):
        for file in os.listdir('media/username'):
            os.remove(f"media/username/{file}")
