from django.contrib import admin
from django.urls import path
from django.urls import path, include 
from . import views
from .views import UsersList,Findusers
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', UsersList.as_view(),name='dating-home'),
    path('report-<username>/',views.user_report,name='user-report'),
    path('<username>/profile_check',views.profile_check,name='user-profile-check'),
    path('chats/',include('chats.urls')),
    path('search/',Findusers.as_view(),name='find-users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)