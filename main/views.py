"""
Views for main app.
"""
from django.views.generic import TemplateView
from .models import WorkExperience, Education
from django.http import StreamingHttpResponse
import os
import mimetypes


class IndexView(TemplateView):
    """Main page view."""
    template_name = "home.html"
    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       return context

class AboutMeView(TemplateView):
    """About me page view."""
    template_name = "aboutMe.html"

class AboutWebsiteView(TemplateView):
    """About website page view."""
    template_name = "aboutWebsite.html"

class WorkExperienceAndEducationView(TemplateView):
    """About website page view."""
    template_name = "workExperienceAndEducation.html"
    def get_context_data(self, **kwargs):
       context = super(WorkExperienceAndEducationView, self).get_context_data(**kwargs)
       works = WorkExperience.objects.filter(user_id=1).order_by('-start_date')
       educations = Education.objects.filter(user_id=1).order_by('-start_date')
       context['works'] = works
       context['educations'] = educations
       return context

def DownloadFile(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
