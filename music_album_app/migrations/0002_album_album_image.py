# Generated by Django 4.1 on 2022-08-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_album_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
