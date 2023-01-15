from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from users.models import Profile
from dating.models import Chatrequests,Userchat
from django.shortcuts import redirect
from django.http import HttpResponse

class Chathome(ListView):
    model=User
    template_name = 'chats/chat_home.html'
    context_object_name='object'

    def get_queryset(self):
        messages_left_list=[]
        for o in Userchat.objects.all():
            if o.user.username == self.request.user.username:
                for key,value in o.chat.items():
                    messages_left_list.append([key,value[1]['messages_left']])
                

        return {'users':User.objects.all(),'message_left':messages_left_list}


def chat_with_user(request,**username_2):

    user_2 = User.objects.all().filter(username=username_2['username_2']).first()
    user_1 = User.objects.all().filter(username=request.user.username).first()

    if request.method=='POST':
        message=request.POST['message']
        # a=Chatrequests.objects.get(user=user_1)
        # json_file=user_1.chatrequests.chats[user_2.username][0]['chat']
        # json_file.append([user_1.username,message])
        # a.chats[user_2.username][0]['chat']=json_file
        # a.save()

        # b=Chatrequests.objects.get(user=user_2)
        # json_file2=user_2.chatrequests.chats[user_1.username][0]['chat']
        # json_file2.append([user_1.username,message])
        # b.chats[user_1.username][0]['chat']=json_file2
        
        # value=user_2.chatrequests.chats[user_1.username][1]['messages_left']
        # value=(value)+1
        # b.chats[user_1.username][1]['messages_left']=value

        # b.save()
 
        userchat_object_fetched_1=Userchat.objects.get(user=user_1)
        json_file=userchat_object_fetched_1.chat[user_2.username][0]['chat']
        json_file.append([user_1.username,message])
        userchat_object_fetched_1.chat[user_2.username][0]['chat']=json_file
        userchat_object_fetched_1.save()

        userchat_object_fetched_2=Userchat.objects.get(user=user_2)
        json_file2=userchat_object_fetched_2.chat[user_1.username][0]['chat']
        json_file2.append([user_1.username,message])
        userchat_object_fetched_2.chat[user_1.username][0]['chat']=json_file2
        
        value=userchat_object_fetched_2.chat[user_1.username][1]['messages_left']
        value=(value)+1
        userchat_object_fetched_2.chat[user_1.username][1]['messages_left']=value

        userchat_object_fetched_2.save()
        
        return redirect(request.path_info)
    
    else:
        c=Userchat.objects.get(user=user_1)
        c.chat[user_2.username][1]['messages_left']=0
        c.save()

    context={
            "user_1":user_1,
            "user_2":user_2,
            "chat":Userchat.objects.get(user=user_1).chat[user_2.username][0]['chat'],
            "user_list":[user_1.username,user_2.username],
            "user1_check":[user_1.username],
            "user2_check":[user_2.username],

        }
    return render(request, 'chats/chat_with_user.html',context)
    
    