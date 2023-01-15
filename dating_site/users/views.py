from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render,redirect
from dating.models import Chatrequests,Userchat
# Create your views here.

@login_required
def profile(request,**username):
    if request.method=='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/'+username['username']+'/profile/')
    else:
        try:
            profile=request.user.profile
        except:
            profile=Profile.objects.create(user=request.user)
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=profile)

    context={
            "user_form":user_form,
            "profile_form":profile_form
        }
    return render(request, 'users/profile.html',context)

class ChatRequestsView(ListView):
    model=User
    template_name = 'users/chat_request_template.html'
    context_object_name='object'

    def get_queryset(self):
        user_array=[]
        counter=1
        for u in User.objects.all():
            if u.username in self.request.user.chatrequests.chat_request:
                user_array.append(u)
        return {'users':user_array,'user_logged_in':self.request.user}
    def post(self, request,username):

        user_decision = request.POST['user_decision']
        user_who_requested=User.objects.all().filter(username=user_decision[:-6]).first()
        user_who_decided=User.objects.all().filter(username=request.user.username).first()
        if 'accept' in user_decision: 
            
            json_file=user_who_decided.chatrequests.match
            json_file.append(user_who_requested.username)
            json_filea=user_who_decided.chatrequests.chat_request
            json_filea.remove(user_who_requested.username)
            a=Chatrequests.objects.all().filter(user=user_who_decided).first()
            a.match=json_file
            a.chat_request=json_filea
            a.save()
            
            userchat_fetched , fetching_boolean= Userchat.objects.get_or_create(user=user_who_decided)
            if fetching_boolean:
                userchat_fetched.chat[user_who_requested.username]=[]
                json_user_who_decided=userchat_fetched.chat[user_who_requested.username]
                json_user_who_decided.append({'chat':[]})
                json_user_who_decided.append({'messages_left':0})
                userchat_fetched.save()
                
            
            json_file=user_who_requested.chatrequests.match
            json_file.append(user_who_decided.username)
            json_fileb=user_who_requested.chatrequests.chat_requested
            json_fileb.remove(user_who_decided.username)
            b=Chatrequests.objects.all().filter(user=user_who_requested).first()
            b.match=json_file
            b.chat_requested=json_fileb
            b.save()

            userchat_fetched , fetching_boolean= Userchat.objects.get_or_create(user=user_who_requested)
            if fetching_boolean:
                userchat_fetched.chat[user_who_decided.username]=[]
                json_user_who_requested=userchat_fetched.chat[user_who_decided.username]
                json_user_who_requested.append({'chat':[]})
                json_user_who_requested.append({'messages_left':0})
                userchat_fetched.save()
        
        elif 'reject' in user_decision: 
            json_file=user_who_decided.chatrequests.ban
            json_file.append(user_who_requested.username)
            a=Chatrequests.objects.all().filter(user=user_who_decided).first()
            a.ban=json_file
            a.save()

        return redirect(request.path_info)
