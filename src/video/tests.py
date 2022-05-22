from django.test import TestCase
from .models import Video 
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.urls import reverse 


class VideoTest(TestCase):

    def setUp(self):
        user=User.objects.create(username='username',password='password')
        video=open("media/home.mp4","rb")
        video=SimpleUploadedFile("an_example" ,video.read() ,content_type="video/mp4")
        Video.objects.create(video=video,subject='example_subject' ,sharer=user.profile ,description="This is an testing video",tags=["tag",])
    
    def test_video_detail_page(self):
        self.assertGreaterEqual(Video.objects.count(),1)

        video=Video.objects.get(subject='example_subject')
        response=self.client.get(reverse("video:video_detail",args=["username","example_subject",video.id]))
        self.assertEqual(response.status_code,200)

        self.assertTemplateUsed(response,"video/video_detail.html")

        self.assertContains(response,"پیشنهادی")
        self.assertContains(response,"مشابه")
        self.assertContains(response,"دیدگاه ها")
        self.assertContains(response,"username")
        self.assertContains(response,"example_subject")       
        self.assertContains(response,"This is an testing video")
        self.assertContains(response,"tag")


    def test_file_deleter(self):
        for file in os.listdir('media/username'):
            os.remove(f"media/username/{file}")
