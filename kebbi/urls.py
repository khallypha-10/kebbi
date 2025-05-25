# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('setlang/', set_language, name='set_language'),  # Explicit language setter
] + i18n_patterns(
    path('', include('project.urls')),
    prefix_default_language=False
)