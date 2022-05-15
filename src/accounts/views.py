from cProfile import Profile
from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required
from video.models import Video
# Create your views here.


@login_required(login_url="allauth.login")
def profile_page(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    videos=Video.objects.filter(sharer=profile)
    return(render(request ,"account/profile_page.html", {'user':user ,'user':user ,'videos' :videos}))
