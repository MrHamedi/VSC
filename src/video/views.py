from django.shortcuts import render
from django.views.generic import DetailView ,CreateView
from .models import Video 
from comment.models import Comment
from .forms import VideoShareForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class VideoDetail(DetailView):
    model=Video 
    template_name="video/video_detail.html"
    context_object_name="video"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(video=self.object)
        return context 


class VideoShare(LoginRequiredMixin,CreateView):
    form_class=VideoShareForm
    template_name="video/video_share.html"
    success_url=reverse_lazy("accounts:profile_page")

    def form_valid(self ,form):
        self.object=form.save(commit=False)
        self.object.sharer=self.request.user.profile
        self.object.save()
        return super().form_valid(form)
