import os 
from django.core.exceptions import ValidationError


def video_validator(video): 
    video=os.path.splitext(video.name)[1]
    if str(video) not  in [".mp4" ,".ogv" ,".m4v" , ".webm"]:
        raise ValidationError(f"متاسفانه فرمت ارسال شده قابل قبول نیست! فرمت های قابل قبول شامل mp4 , ogv , m4v و webm است.")