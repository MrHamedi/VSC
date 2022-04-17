from termios import VINTR
from django.test import TestCase
from .models import Video 
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
import os

class VideoTest(TestCase):

    def setUp(self):
        user=User.objects.create(username='username',password='password')
        video=open("media/home.mp4","rb")
        video=SimpleUploadedFile("an_example" ,video.read() ,content_type="video/mp4")
        Video.objects.create(video=video,subject='example_subject' ,sharer=user.profile)

    def test_video(self):
        self.assertGreaterEqual(Video.objects.count(),1)

    def test_file_deleter(self):
        for file in os.listdir('media/username'):
            os.remove(f"media/username/{file}")
