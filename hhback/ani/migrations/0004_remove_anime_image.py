# Generated by Django 3.0.4 on 2020-04-26 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ani', '0003_anime_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='image',
        ),
    ]