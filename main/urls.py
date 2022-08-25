"""
Urls for main app.
"""
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about-me', views.AboutMeView.as_view(), name='about_me'),
    path('about-website', views.AboutWebsiteView.as_view(), name='about_website'),
    path(
        'work-experience-education', 
        views.WorkExperienceAndEducationView.as_view(), 
        name='work_experience_and_education'
    ),
    path('download-cv', views.DownloadFile, name='download-cv'),
]
