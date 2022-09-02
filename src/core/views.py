from django.shortcuts import render
from video.models import Video
from django.views.generic import ListView 
# Create your views here.


class HomePage(ListView):
    model=Video 
    template_name="core/homepage.html"
    context_object_name="videos"
    paginate_by = 16
    