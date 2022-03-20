from tabnanny import verbose
from django.db import models
from core.models import CommonPostableFields
# Create your models here.


class Comment(CommonPostableFields):

    content=models.CharField(max_length=500)


    def __str__(self):
        return(self.content)

    