from django.urls import path 
from . import views

app_name="accounts"

urlpatterns=[
    path("profile/" ,views.profile_page ,name="profile_page"),
    path("profile_editor/",views.profile_editor,name="profile_editor")
]