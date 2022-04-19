# Generated by Django 3.0 on 2022-04-12 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_auto_20220407_2230'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-create_date',), 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_type',
            field=models.CharField(choices=[('c', 'comment on comment'), ('v', 'comment on video')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='related_comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_comments', to='comment.Comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='video_comments', to='video.Video'),
            preserve_default=False,
        ),
    ]
