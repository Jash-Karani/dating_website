from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.shortcuts import render,redirect
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