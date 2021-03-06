# Generated by Django 3.0 on 2022-05-10 22:48

import core.utils
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='تاریخ به اشتراک گذاری', verbose_name='تاریخ')),
                ('last_edit_date', models.DateTimeField(auto_now=True, help_text='تاریخ آخرین تغییر', verbose_name='آخرین تغییر')),
                ('video', models.FileField(upload_to=core.utils.upload_to_username)),
                ('slug', models.SlugField(blank=True, max_length=300, unique=True)),
                ('subject', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.utils.upload_to_username)),
                ('sharer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile', verbose_name='به اشتراک گذارنده')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'فیلم',
                'verbose_name_plural': 'فیلم ها',
                'ordering': ('-create_date',),
            },
        ),
    ]
