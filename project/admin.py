from django.contrib import admin
from django.utils.text import slugify
from googletrans import Translator
from .models import Achievement

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Auto-translate Hausa fields if empty
        if not obj.title_ha and obj.title_en:
            try:
                translator = Translator()
                obj.title_ha = translator.translate(obj.title_en, src='en', dest='ha').text
                obj.description_ha = translator.translate(obj.description_en, src='en', dest='ha').text
            except Exception as e:
                print(f"Translation error: {e}")

        # First save to get a primary key if new object
        is_new = obj.pk is None
        super().save_model(request, obj, form, change)

        if is_new and not obj.slug:
            title = obj.title_en or obj.title_ha
            obj.slug = f"{slugify(title)}-{obj.pk}"
            obj.save(update_fields=["slug"])
