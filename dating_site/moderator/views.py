from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ModeratorLogin1,ModeratorLogin2
from django.contrib.auth.models import User
from dating.models import Reports

# Create your views here.

def login_moderator(request):
    if request.method == 'POST':
        user_form=ModeratorLogin1(request.POST)
        profile_form=ModeratorLogin2(request.POST)
        username = request.POST['username']
        password = request.POST['moderator_password']
        user=User.objects.all().filter(username=username).first()
        if user and password==user.profile.moderator_password:
            if user.is_active and user.profile.moderator==True:
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect(reverse('moderator-home'))
        else:
            messages.error(request,'username not correct')
            return redirect(reverse('moderator-login'))
    else:
        user_form=ModeratorLogin1()
        profile_form=ModeratorLogin2()
    return render(request,'./login.html',{'user_form':user_form,'profile_form':profile_form})

def home(request):
    return render(request,'./home.html',{'user':request.user})

class Reported(ListView):
    model=Reports
    template_name='./reported.html'
    context_object_name='reports'

