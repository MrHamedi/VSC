import cv2
import numpy as np
from django.conf import settings
import os
import imutils
# Playing video from file:


def set_image(video):  
    if video.image:
        return
    username=video.sharer.user.username
    subject=video.subject
    cap = cv2.VideoCapture(video.video.path)
    path=os.path.join(settings.MEDIA_ROOT,username)
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print ('Error: Creating directory of data')
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=300)
    image = os.path.join(path, f"{subject}_{video.pk}.jpg")
    cv2.imwrite(image, frame)
    cap.release()
    cv2.destroyAllWindows()
    video.image=f"{username}/{subject}_{video.pk}.jpg"
    video.save()