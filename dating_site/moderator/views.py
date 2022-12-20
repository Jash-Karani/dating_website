from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ModeratorLogin1,ModeratorLogin2
from django.contrib.auth.models import User
from dating.models import Reports
from django.contrib.admin.views.decorators import staff_member_required

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
    

    def post(self, request):
        mod_decision = request.POST['mod-decision']
        mod_decision_list = mod_decision.split(" ")
        i=4
        temp_str=""
        while i<len(mod_decision_list):
            temp_str=temp_str+(mod_decision_list[i])+" "
            i+=1
        report_list ={(mod_decision_list[1]):[mod_decision_list[2],mod_decision_list[3],temp_str.strip()]}
        
        if mod_decision_list[0] == 'ignored':
            obj=get_object_or_404(Reports,report= report_list)
            obj.delete()
        elif mod_decision_list[0] == 'delete_user':
            # try:
                print()
                u = User.objects.get(username = mod_decision_list[3])
                u.delete()
                obj=get_object_or_404(Reports,report= report_list)
                obj.delete()
                # messages.sucess(request, "The user is deleted")
            # except:
                # print('could not be deleted')
                # messages.error(request, "The user not found")    

        return redirect(request.path_info)

    


