from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
# Create your views here.

class UsersList(ListView):
    model=User
    template_name = 'dating/homepage.html'
    context_object_name='users'