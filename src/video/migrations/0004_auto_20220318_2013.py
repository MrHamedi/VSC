# Generated by Django 3.0 on 2022-03-18 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20220318_1815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('-create_date',)},
        ),
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(default='slug_maker()', max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='subject',
            field=models.CharField(max_length=150),
        ),
    ]
