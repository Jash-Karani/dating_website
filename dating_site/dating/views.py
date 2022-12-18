from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from users.models import Profile
from dating.models import Chatrequests
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Reports

from thefuzz import process, fuzz

class  UsersList(ListView):
    model=User
    template_name = 'dating/homepage.html'
    context_object_name='users'
    
    def post(self, request):
        user_requested = User.objects.all().filter(username=request.POST['chat_request']).first()
        try:
            json_file=user_requested.chatrequests.chat_request
        except:
            d=Chatrequests.objects.create(user=user_requested)
            d.save()
            json_file=user_requested.chatrequests.chat_request
        json_file.append(request.user.username)
        a=Chatrequests.objects.get(user=user_requested)
        a.chat_request=json_file
        a.save()
        try:
            json_file2=request.user.chatrequests.chat_requested
        except:
            c=Chatrequests.objects.create(user=request.user)
            c.save()
            json_file2=request.user.chatrequests.chat_requested
        json_file2.append(user_requested.username)
        b=Chatrequests.objects.get(user=request.user)
        b.chat_requested=json_file2
        b.save()
        return redirect('/')

    def get(self, request):
        if request.user.is_authenticated:
            try:
                json_file2=request.user.chatrequests.chat_requested
            except:
                Chatrequests.objects.create(user=request.user)
            try:
                a=request.user.profile.name
            except:
                profile=Profile.objects.create(user=request.user)
                profile.save()
            return render(request, self.template_name,{'users':User.objects.all()})
        else:
            return render(request, self.template_name,{'users':User.objects.all()})


def profile_check(request,**username):

    if request.method=='POST':
        user_requested = User.objects.all().filter(username=request.POST['chat_request']).first()
        try:
            json_file=user_requested.chatrequests.chat_request
        except:
            d=Chatrequests.objects.create(user=user_requested)
            d.save()
            json_file=user_requested.chatrequests.chat_request
        json_file.append(request.user.username)
        a=Chatrequests.objects.get(user=user_requested)
        a.chat_request=json_file
        a.save()
        try:
            json_file2=request.user.chatrequests.chat_requested
        except:
            c=Chatrequests.objects.create(user=request.user)
            c.save()
            json_file2=request.user.chatrequests.chat_requested
        json_file2.append(user_requested.username)
        b=Chatrequests.objects.get(user=request.user)
        b.chat_requested=json_file2
        b.save()
        return redirect('/')
        
    context={
            "u":User.objects.all().filter(username= username['username']).first(),
        }
    return render(request, 'dating/user_profile_check.html',context)



def user_report(request,**username):
    user_getting_reported = User.objects.all().get(username=username['username'])
    if request.method=='POST':
        report_reason=request.POST['report']
        a=Reports(report={request.user.username:[user_getting_reported.username,report_reason]})
        a.save()
        return redirect('dating-home')
    context={
            "user":User.objects.all().filter(username= username['username']).first(),
        }
    return render(request, 'users/report.html',context)
class  Findusers(ListView):
    model=User
    template_name = 'dating/find_users.html'
    context_object_name='users'
    
    def post(self, request):
        user_search = request.POST['search']

        user_list=[]
        for u in User.objects.all():
            if(u.username!=request.user.username):
                user_list.append(u.username)

        users_found=process.extract(user_search, user_list,scorer=fuzz.partial_token_set_ratio)
        filtered_list=[]
        print(len(users_found))
        print((users_found)[1][1])
        for i in range(len(users_found)):
            if(users_found[i][1]>=75):
                print(filtered_list)
                filtered_list.append(users_found[i])
        return render(request, 'dating/find_users.html',{'users_found':filtered_list})

