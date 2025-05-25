# your_app/templatetags/lang_utils.py
from django import template
from django.urls import translate_url
from urllib.parse import urlparse

register = template.Library()

@register.filter
def remove_lang(url):
    parsed = urlparse(url)
    path = parsed.path
    if path.startswith('/ha/'):
        return path[3:] or '/'
    elif path.startswith('/en/'):
        return path[3:] or '/'
    return path