# Generated by Django 3.1.7 on 2021-04-07 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('EmailId', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]