from django.shortcuts import render
from django.views.generic import DetailView 
from .models import Video 
from comment.models import Comment


class VideoDetail(DetailView):
    model=Video 
    template_name="video/video_detail.html"
    context_object_name="video"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(video=self.object)
        return context 