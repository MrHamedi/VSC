from django.urls import path
from .views import create_comment

app_name="comments"

urlpatterns = [
    path("<int:pk>/",create_comment,name="comment_creation"),

]