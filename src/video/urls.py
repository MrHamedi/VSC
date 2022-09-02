from django.urls import path 
from .import views

app_name="video"

urlpatterns=[
    path("<str:username>/<int:year>/<int:month>/<int:day>/<int:pk>/",views.VideoDetail.as_view(),name="video_detail"),
    path("share/",views.VideoShare.as_view(),name="video_share"),
]