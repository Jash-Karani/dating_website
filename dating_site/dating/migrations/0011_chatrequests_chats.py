# Generated by Django 4.1.3 on 2022-12-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0010_chats'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatrequests',
            name='chats',
            field=models.JSONField(default=dict),
        ),
    ]
