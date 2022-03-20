# Generated by Django 3.0 on 2022-03-18 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='تاریخ به اشتراک گذاری', verbose_name='تاریخ')),
                ('last_edit_date', models.DateTimeField(auto_now=True, help_text='تاریخ آخرین تغییر', verbose_name='آخرین تغییر')),
                ('content', models.CharField(max_length=500)),
                ('sharer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile', verbose_name='به اشتراک گذارنده')),
            ],
            options={
                'ordering': ('-create_date',),
                'abstract': False,
            },
        ),
    ]
