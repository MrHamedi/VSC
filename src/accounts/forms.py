from django import forms 
from .models import Profile
from django.contrib.auth.models import User 


class UserModelForm(forms.ModelForm):
    class Meta:
        fields=("username",)
        model=User


class ProfileForm(forms.ModelForm):
    class Meta:
        fields=("image",)
        model=Profile