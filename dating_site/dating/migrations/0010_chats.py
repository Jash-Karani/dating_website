# Generated by Django 4.1.3 on 2022-12-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dating', '0009_rename_accept_chatrequests_ban_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_chats', models.JSONField(default=dict)),
            ],
        ),
    ]
