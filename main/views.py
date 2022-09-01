"""
Views for main app.
"""
import os
import mimetypes
from django.views.generic import TemplateView
from .models import WorkExperience, Education, User
from django.http import HttpResponse


class IndexView(TemplateView):
    """Main page view."""
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class AboutMeView(TemplateView):
    """About me page view."""
    template_name = "aboutMe.html"

    def get_context_data(self, **kwargs):
        from django.utils.translation import get_language_from_request
        lang = get_language_from_request(self.request)
        context = super(AboutMeView, self).get_context_data(**kwargs)
        user = User.objects.raw(
            ("""SELECT 1 as id, email,
                surname_{1} as surname,
                name_{1} as name,
                address_{1} as address
            FROM main_user WHERE id={0}
            """).format(1, lang)
        )[0]
        context['user'] = user
        return context


class WebsiteStackView(TemplateView):
    """About website page view."""
    template_name = "aboutWebsite.html"


class WorkExperienceAndEducationView(TemplateView):
    """About website page view."""
    template_name = "workExperienceAndEducation.html"

    def get_context_data(self, **kwargs):
        from django.utils.translation import get_language_from_request
        lang = get_language_from_request(self.request)
        context = super(
            WorkExperienceAndEducationView, self
        ).get_context_data(**kwargs)
        works = WorkExperience.objects.raw(
            ("""SELECT 1 as id, start_date, end_date,
                company_name_{1} as company_name,
                position_{1} as position,
                work_description_{1} as work_description
            FROM main_workexperience WHERE user_id={0}
            ORDER BY start_date
            """).format(1, lang)
        )
        educations = Education.objects.raw(
            ("""SELECT 1 as id, type, degree, start_date, end_date,
                speciality_{1} as speciality,
                institution_name_{1} as institution_name,
                course_description_{1} as course_description
            FROM main_education WHERE user_id={0}
            ORDER BY start_date
            """).format(1, lang)
        )
        context['works'] = works
        context['educations'] = educations
        return context


def DownloadFile(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Asset Khaitbay CV.pdf'
    filepath = os.path.join(BASE_DIR, 'static/doc/' + 'Asset Khaitbay CV.pdf')
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
