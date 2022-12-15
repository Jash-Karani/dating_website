from django.contrib import admin
from django.urls import path
from django.urls import path, include 
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import ChatRequestsView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('login/', views.login_moderator,name='moderator-login'),
    path('login/', views.login_moderator,name='moderator-login'),
    path('home/', views.home,name='moderator-home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='./logout.html'),name='moderator-logout'),
    path('reported/', views.Reported.as_view(),name='moderator-report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
