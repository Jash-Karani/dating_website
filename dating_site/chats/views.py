from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from users.models import Profile
from dating.models import Chatrequests
from django.shortcuts import redirect
from django.http import HttpResponse

class Chathome(ListView):
    model=User
    template_name = 'chats/chat_home.html'
    context_object_name='users'

def chat_with_user(request,**username_2):
    user_2 = User.objects.all().filter(username=username_2['username_2']).first()
    user_1 = User.objects.all().filter(username=request.user.username).first()
    # if request.method=='POST':
    #     report_reason=request.POST['report']
    #     a=Reports(report={request.user.username:[user_getting_reported.username,report_reason]})
    #     a.save()
    #     return redirect('dating-home')
    context={
            "user_1":user_1,
            "user_2":user_2,

        }
    return render(request, 'chats/chat_with_user.html',context)
    
    