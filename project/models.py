from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _

class Achievement(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    slug = models.SlugField(null=True, blank=True)
    image = ResizedImageField(size=[400, 400], quality=100, crop=['middle', 'center'], upload_to='achievements')
    image_2 = ResizedImageField(size=[400, 400], quality=100, crop=['middle', 'center'], upload_to='achievements')
    image_3 = ResizedImageField(size=[400, 400], quality=100, crop=['middle', 'center'], upload_to='achievements')
    image_4 = ResizedImageField(size=[400, 400], quality=100, crop=['middle', 'center'], upload_to='achievements', null=True, blank=True)
    image_5 = ResizedImageField(size=[400, 400], quality=100, crop=['middle', 'center'], upload_to='achievements', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title