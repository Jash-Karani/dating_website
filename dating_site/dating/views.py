from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from users.models import Profile
from dating.models import Chatrequests
from django.shortcuts import redirect



# Create your views here.

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

            
            
            
        #     user_form=UserUpdateForm(request.POST,instance=request.user)
        #     profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        #     if user_form.is_valid() and profile_form.is_valid():
        #         user_form.save()
        #         profile_form.save()
        #         return redirect('/'+username['username']+'/profile/')

        # else:
        #     try:
        #         profile=request.user.profile
        #     except:
        #         profile=Profile.objects.create(user=request.user)
        #     user_form=UserUpdateForm(instance=request.user)
        #     profile_form=ProfileUpdateForm(instance=profile)

        # context={
        #         "user_form":user_form,
        #         "profile_form":profile_form
        #     }
        # return render(request, 'users/profile.html',context)