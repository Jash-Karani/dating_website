from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class ModeratorLogin1(forms.ModelForm):
    class Meta:
        model = User
        
        fields = ['username']
class ModeratorLogin2(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['moderator_password']
