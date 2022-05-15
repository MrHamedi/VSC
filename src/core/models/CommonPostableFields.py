from django.db import models
from django.conf import settings
from accounts.models import Profile

# Create your models here.

class CommonPostableFields(models.Model):
    """
        This fields are common between posts and comments so we only write them once
    """
    create_date=models.DateTimeField(auto_now_add=True ,null=False ,blank=False,help_text="تاریخ به اشتراک گذاری" ,verbose_name='تاریخ')
    last_edit_date=models.DateTimeField(auto_now=True ,null=False ,blank=False,help_text="تاریخ آخرین تغییر" ,verbose_name="آخرین تغییر")
    sharer=models.ForeignKey(Profile  ,null=False ,blank=False, verbose_name='به اشتراک گذارنده' ,on_delete=models.CASCADE)

    class Meta:
        abstract=True 
        ordering=("-create_date",)