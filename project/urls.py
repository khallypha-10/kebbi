from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about-Dr-Nasir-Idris/', views.about, name="about"),
    path('achievements/', views.achievements, name="achievements"),
    path('achievement/<slug>/', views.achievement, name="achievement"),
    
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)