from django.contrib import admin
from django.urls import path
from django.urls import path, include 
from . import views
from .views import UsersList
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', UsersList.as_view(),name='dating-home'),
    path('report-<username>',views.user_report,name='user-report'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)