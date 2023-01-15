from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render
from django.http import Http404,HttpResponse


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        # if not u.email.split('@')[1] == "pilani.bits-pilani.ac.in":
            # raise ImmediateHttpResponse(render(request, "dating/invalid_user.html"))
