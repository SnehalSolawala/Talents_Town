# Generated by Django 3.2 on 2021-04-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_uploadvideo_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadvideo',
            name='total_likes',
            field=models.IntegerField(default=0),
        ),
    ]
