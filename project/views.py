from django.shortcuts import render
from . models import Achievement
# Create your views here.

from googletrans import Translator

def translate_to_hausa(text):
    translator = Translator()
    return translator.translate(text, src='en', dest='ha').text

def home(request):
    achievements = Achievement.objects.all().order_by('-id')[:3]
    context = {'achievements': achievements}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def achievements(request):
    achievements = Achievement.objects.all().order_by('-id')
    context = {'achievements': achievements}
    return render(request, "achievements.html", context)

def achievement(request, slug):
    achievement = Achievement.objects.get(slug=slug)
    context = {'achievement': achievement}
    return render(request, "achievement-details.html", context)