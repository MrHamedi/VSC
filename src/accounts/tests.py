from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.


class ProfileTest(TestCase):

    def setUp(self):
        user=User.objects.create(username='username',password='password')


    def test_profile_fields(self):
        profile=Profile.objects.get(id=1)
        self.assertEqual(profile.user.username,"username")


