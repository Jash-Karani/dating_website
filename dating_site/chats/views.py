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
    


    if request.method=='POST':
        message=request.POST['message']
        a=Chatrequests.objects.get(user=user_1)
        json_file=user_1.chatrequests.chats[user_2.username][2]['chat']
        json_file.append([user_1.username,message])
        a.chats[user_2.username][2]['chat']=json_file
        a.save()

        b=Chatrequests.objects.get(user=user_2)
        json_file2=user_2.chatrequests.chats[user_1.username][2]['chat']
        json_file2.append([user_1.username,message])
        b.chats[user_1.username][2]['chat']=json_file2
        
        value=user_2.chatrequests.chats[user_1.username][3]['messages_left']
        value=value+1
        b.chats[user_1.username][3]['messages_left']=value

        b.save()
        return redirect(request.path_info)
    else:

        b=Chatrequests.objects.get(user=user_1)
        b.chats[user_2.username][3]['messages_left']=0
        b.save()

    context={
            "user_1":user_1,
            "user_2":user_2,
            "chat":user_1.chatrequests.chats[user_2.username][2]['chat'],
            "user_list":[user_1.username,user_2.username],
            "user1_check":[user_1.username],
            "user2_check":[user_2.username],

        }
    return render(request, 'chats/chat_with_user.html',context)
    
    