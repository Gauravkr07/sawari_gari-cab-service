# Generated by Django 5.0.3 on 2024-05-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cab_driver_info',
            name='password',
            field=models.CharField(default=None),
        ),
        migrations.AddField(
            model_name='user_info',
            name='password',
            field=models.CharField(default=None, max_length=50),
        ),
    ]