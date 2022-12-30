from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.core import validators
from django.forms import CharField

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','image','gender','status','hobbies','age']

class ReportForm(forms.Form):
    report_reason = forms.CharField(validators=[validators.validate_slug])
