from django.forms import ModelForm
from .models import Video


class VideoShareForm(ModelForm):
    class Meta:
        model=Video
        fields=('video',"subject","description","image","tags")