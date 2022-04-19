from cProfile import Profile
from difflib import restore
from django.test import TestCase
from django.urls import reverse 
from video.models import Video 
from django.contrib.auth.models import User 
from accounts.models import Profile
from django.core.files import File as DjangoFile
import os

class TestPage(TestCase):

    def setUp(self):
        user=User.objects.create(username="username",password="password")
        video=DjangoFile(open('media/home.mp4','rb'),name="test")
        video=Video.objects.create(video=video ,sharer=user.profile ,subject="test_subject")

    def test_base(self):
        response=self.client.get(reverse("core:homepage"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'core/homepage.html')
        self.assertContains(response,"VSC")
        self.assertContains(response,"ورود")
        self.assertContains(response,"ثبت نام")
        self.assertContains(response,"test_subject")
        self.assertContains(response, '<a class="navbar-brand" href="/">VSC</a>', html=True)       
        self.assertContains(response, '<a class="nav-link" href=%s>ورود</a>'%(reverse('account_login')), html=True)               
        self.assertContains(response, '<a class="nav-link" href="%s">ثبت نام</a>'%(reverse('account_signup')), html=True) 

    def test_file_deleter(self):
        for file in os.listdir('media/username'):
            os.remove(f"media/username/{file}")