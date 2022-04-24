from django.shortcuts import render
from django.views.generic import DetailView 
from .models import Video 


class VideoDetail(DetailView):
    model=Video 
    template_name="video/video_detail.html"
    context_object_name="video"
