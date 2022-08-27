import os
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def cut(value, arg):
    """Removes all values of arg from the given string"""
    value['test'] = arg
    return value