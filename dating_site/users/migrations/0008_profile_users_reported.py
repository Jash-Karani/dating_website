# Generated by Django 4.1.3 on 2022-12-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_moderator_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='users_reported',
            field=models.JSONField(default=list),
        ),
    ]
