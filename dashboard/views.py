from django.shortcuts import render
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
# Create your views here.
def index(request):
    return render(request, 'pages/dashboard.html')


def setLanguage(request, language):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language in ['en', 'fr']:  # Specify the supported languages
            request.session['django_language'] = language
            translation.activate(language)
            response = index(request)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        else:
            return render(request, 'pages/dashboard.html')


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        # next_url = reverse(view.url, args=view.args, kwargs=view.kwargs)
        response = index(request)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response