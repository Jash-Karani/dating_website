from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import allauth.socialaccount
import json
from django.db.models import JSONField
from django import forms

# Create your models here.
class Chatrequests(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chat_request = JSONField(default=list)
    chat_requested = JSONField(default=list)
    match = JSONField(default=list)
    ban = JSONField(default=list)
    chats = JSONField(default=dict)
    
    def __str__(self):
        return f'{self.user}:{self.chat_request}'
class Reports(models.Model):
    report = JSONField(default =dict)

class CurrentChats(models.Model):
    current_chats = JSONField(default =dict)
    def __str__(self):
        return f'{self.current_chats}'


class UserChat(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    chats=JSONField(default =dict)
    def __str__(self):
        return f'{self.user.username} Chats'

