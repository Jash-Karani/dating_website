from django.db import models
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
    accept = JSONField(default=list)
    reject = JSONField(default=list)
    
    
    def __str__(self):
        return f'{self.user}:{self.chat_request}'
class Reports(models.Model):
    report = JSONField(default =dict)
