from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    """Main page view."""
    template_name = "pages/index.html"
    def get_context_data(self, **kwargs):
       context = super(IndexView, self).get_context_data(**kwargs)
       context['test_param'] = 'My nameee'
       context['test_param_2'] = 'is Asset'
       return context
