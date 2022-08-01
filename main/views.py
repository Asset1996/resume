from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    """Main page view."""
    template_name = "index.html"
