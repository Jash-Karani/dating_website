from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from users.models import Profile
from dating.models import Chatrequests
from django.shortcuts import redirect

class  UsersList(ListView):
    model=User
    template_name = 'dating/homepage.html'
    context_object_name='users'
    def post(self, request):
        user_requested = request.POST['chat_request']
        
        try:
            json_file=request.user.chatrequests.chat_request
        except:
            chat_request_var=Chatrequests.objects.create(user=request.user)
            json_file=request.user.chatrequests.chat_request
        json_file.append(user_requested)
        a=Chatrequests.objects.get(user=request.user)
        a.chat_request=json_file
        a.save()
        return redirect('/')
