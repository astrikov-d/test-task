from django.db import models
from django.utils.translation import ugettext_lazy as _ul
from djangocms_text_ckeditor.fields import HTMLField
from taggit.managers import TaggableManager

from backend.generic.db.models import TimestampedModel


class Article(TimestampedModel):
    slug = models.SlugField(unique=True, verbose_name=_ul('Slug'))
    image = models.ImageField(upload_to='articles/%Y/%m/%d')

    # Translatable fields.
    title_en = models.CharField(max_length=255, verbose_name=_ul('Name (EN)'))
    title_de = models.CharField(max_length=255, verbose_name=_ul('Name (DE)'))

    content_en = HTMLField(verbose_name=_ul('Content (EN)'))
    content_de = HTMLField(verbose_name=_ul('Content (DE)'))

    tags = TaggableManager()

    class Meta:
        verbose_name = _ul('article')
        verbose_name_plural = _ul('articles')
        ordering = ['-creation_date']

    def __str__(self):
        return self.title_en
