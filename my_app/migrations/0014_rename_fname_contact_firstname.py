# Generated by Django 3.2 on 2021-04-17 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0013_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='firstname',
        ),
    ]