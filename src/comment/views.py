from email import message
from django.contrib.auth.decorators import login_required
from .models import Comment
from video.models import Video
from django.shortcuts import  redirect 
from django.contrib import messages
# Create your views here.

@login_required
def create_comment(request,pk):
    video=Video.objects.get(id=pk)
    if(request.method=="POST"):
        content=request.POST["content"]
        if(len(content) ==0):
            messages.error(request,"کامنت باید دارای محتوا باشه!!!")
        else:
            comment=Comment(content=content,sharer=request.user.profile,video=video)
            comment.save()
        return redirect(video.get_absolute_url())
    else:
        return(redirect(video.get_absolute_url()))
        