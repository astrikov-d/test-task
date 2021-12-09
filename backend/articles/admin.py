from django.contrib import admin

from backend.articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('slug', 'title_en', 'title_de')


admin.site.register(Article, ArticleAdmin)
