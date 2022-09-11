# Generated by Django 3.0 on 2022-08-06 13:12

import core.utils
from django.db import migrations, models
import video.validators


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20220731_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.upload_image_to_username),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to=core.utils.upload_to_username, validators=[video.validators.video_validator]),
        ),
    ]
