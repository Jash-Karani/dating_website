from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ModeratorLogin1,ModeratorLogin2
from django.contrib.auth.models import User
from users.models import Profile
from dating.models import Reports
from .tables import ProfileTable,ReportTable
from django.contrib.admin.views.decorators import staff_member_required
from dotenv import load_dotenv
import smtplib
import os
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
                u = User.objects.get(username = mod_decision_list[3])
                u.delete()
                obj=get_object_or_404(Reports,report= report_list)
                obj.delete() 

        return redirect(request.path_info)




def mod_table(request):
    table = ProfileTable(Profile.objects.all())

    report_list=[]
    for r in Reports.objects.all():
        key=(list(r.report.keys())[0])

        try:
            user_reported=User.objects.all().get(username=r.report[str(key)][1])
            check=True
        except:
            check=False
        temp_dict={'report_id':key,'report_from':r.report[str(key)][0],'report_against':r.report[str(key)][1],'reason':r.report[str(key)][2],'user_exists':check}
        report_list.append(temp_dict)

    table2 = ReportTable(report_list)

    return render(request, "moderator/tables.html", {
        "table": table,
        "table2": table2,
    })
def user_delete(request,report_id):

    for r in Reports.objects.all():
        print(r.report,report_id)
        if report_id in r.report:

            user_fetched=User.objects.all().get(username=r.report[str(report_id)][1])
            print(user_fetched)
            user_fetched.delete()
            r.delete() 
            break
    return redirect('moderator-table')

def report_ignore(request,report_id):
    for r in Reports.objects.all():
        if report_id in r.report:
            r.delete() 
            break
    return redirect('moderator-table')


class Modemail(ListView):
    model=User
    template_name='./email.html'
    context_object_name='users'
    
    def post(self, request):
        mail_msg = request.POST['mail-content']

        email_list=[]
        for u in User.objects.all():
            email_list.append(u.email)
    
        load_dotenv()
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
        server.sendmail(os.environ.get('EMAIL_USER'), email_list, mail_msg)
        server.quit()

        return redirect('moderator-home')