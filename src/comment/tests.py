from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .models import comment 
from video.models import Video
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from .models import Comment
from django.contrib.auth import login
# Create your tests here.


class CommentTest(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(username='username',password='test_user_password')
        video=open("media/home.mp4","rb")
        video=SimpleUploadedFile("an_example" ,video.read() ,content_type="video/mp4")
        self.video=Video.objects.create(video=video,subject='example_subject' ,sharer=self.user.profile)
        comment=Comment.objects.create(content="example comment on video" ,video=self.video ,comment_type="v" ,sharer=self.user.profile)
        comment_on_comment=Comment.objects.create(content="example comment on comment" ,related_comment=comment ,comment_type="c" ,sharer=self.user.profile)

    def test_comment(self):
        comment_on_video=Comment.objects.get(id=1)
        self.assertGreaterEqual(Comment.objects.count(),2)
        self.assertEqual(comment_on_video.content ,"example comment on video")
        self.assertEqual(comment_on_video.comment_type ,"v")
        comment_on_comment=Comment.objects.get(id=2)
        self.assertEqual(comment_on_comment.comment_type,'c')
        self.assertEqual(comment_on_comment.content,"example comment on comment")
        self.assertEqual(comment_on_comment.related_comment,comment_on_video)

    def test_comment_creation(self):
        #test comment creation redirects to video_detail without content
        self.client.login(username="username",password="test_user_password")
        response=self.client.get(reverse("comments:comment_creation",args=[Video.objects.get(subject="example_subject").id]),follow=True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"video/video_detail.html")

        #test comment creations form makes comment on specified video 
        self.client.post(reverse("comments:comment_creation",args=[Video.objects.get(subject="example_subject").id]),{"content":"example comment content"},follow=True)
        comments=Comment.objects.filter(video=self.video).order_by("create_date")
        self.assertEqual(comments.count(),2)
        self.assertEqual(comments[1].content,"example comment content")
        
        #test after creating comment it will end up in video detail page
        self.assertTemplateUsed(response,"video/video_detail.html")
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"example_subject")

        #test comment have been added to detail page
        response=self.client.get(reverse("video:video_detail",args=["username","example_subject",self.video.id]))
        self.assertContains(response,"example comment content")


    def test_file_deleter(self):
        for file in os.listdir('media/username'):
            os.remove(f"media/username/{file}")
