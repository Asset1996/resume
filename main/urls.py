"""
Urls for main app.
"""
from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path(_('about-me'), views.AboutMeView.as_view(), name='about_me'),
    path(_('website-stack'), views.WebsiteStackView.as_view(), name='website_stack'),
    path(
        _('work-experience-education'), 
        views.WorkExperienceAndEducationView.as_view(), 
        name='work_experience_and_education'
    ),
    path(_('download-cv'), views.DownloadFile, name='download-cv'),
]
