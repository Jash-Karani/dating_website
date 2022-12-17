from django.contrib import admin
from django.urls import path
from django.urls import path, include 
from . import views
from .views import Chathome
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', Chathome.as_view(),name='chat-home'),
    path('<username_2>', views.chat_with_user ,name='chat-with-user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)