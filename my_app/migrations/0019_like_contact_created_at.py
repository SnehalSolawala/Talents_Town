# Generated by Django 3.2 on 2021-04-20 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0018_like_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='like_contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
