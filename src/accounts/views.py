from cProfile import Profile
from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required
from video.models import Video
from .forms import UserModelForm, ProfileForm

# Create your views here.


@login_required(login_url="account_login")
def profile_page(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    videos = Video.objects.filter(sharer=profile)
    return(render(request, "account/profile_page.html", {'user': user, 'user': user, 'videos': videos}))


@login_required(login_url="account_login")
def profile_editor(request):
    user = request.user
    profile = user.profile

    if(request.method == "POST"):
        user_model_form = UserModelForm(request.POST)
        profile_model_form = ProfileForm(files=request.FILES)

        if(user_model_form.is_valid()):

            user_model_form = user_model_form.cleaned_data 
            user.username=user_model_form["username"]
            user.save()

        if(profile_model_form.is_valid()):
            profile_model_form = profile_model_form.cleaned_data
            if(profile_model_form["image"]):
                profile.image = profile_model_form["image"]
                profile.save()

    return(render(request, "account/profile_editor_page.html", {}))
