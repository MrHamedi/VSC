from . import views 
from django.urls import path 

app_name="core"

urlpatterns = [
    path("",views.HomePage.as_view(),name="homepage"),
]