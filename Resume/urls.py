from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import ( UploadResume, ResumeView, ResumeSaveView, 
                    ResumeUserView, DownloadView,
                )

urlpatterns = [
    path('', UploadResume.as_view(), name='resume-upload'),
    path('resume/',ResumeView.as_view(),name='resume'),
    path('resume/<str:pk>', ResumeSaveView.as_view(), name = 'resume-view'),
    path('resume-user/<str:pk>/', ResumeUserView.as_view(), name = 'resume-user'),
    path('resume/download/<str:pk>', DownloadView.as_view(), name='download'),
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)