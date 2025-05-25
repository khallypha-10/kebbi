from django.contrib import admin
from django.utils.text import slugify
from googletrans import Translator
from .models import Achievement

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    # ... (keep your existing fieldsets and list_display) ...

    def save_model(self, request, obj, form, change):
        # Auto-translate Hausa fields if empty
        if not obj.title_ha and obj.title_en:
            try:
                translator = Translator()
                obj.title_ha = translator.translate(obj.title_en, src='en', dest='ha').text
                obj.description_ha = translator.translate(obj.description_en, src='en', dest='ha').text
            except Exception as e:
                print(f"Translation error: {e}")  # Fail gracefully

        # Generate slug with title + PK (if object exists)
        if not obj.slug:
            title = obj.title_en or obj.title_ha  # Fallback to Hausa if English is empty
            if obj.pk:  # Only add PK if the object is already saved
                obj.slug = f"{slugify(title)}-{obj.pk}"
            else:
                obj.slug = slugify(title)
        
        super().save_model(request, obj, form, change)