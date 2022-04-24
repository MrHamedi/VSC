import os 
from django.core.exceptions import ValidationError
import magic


def is_format_valid(video): 
    if(os.path.isfile(video)):
        video=magic.from_file(video,mime=True)
        if str(video) not  in ["video/mp4" ,"video/ogv" ,"video/m4v" , "video/webm"]:
            raise ValidationError(f"Video Format is not valid",code='invalid')