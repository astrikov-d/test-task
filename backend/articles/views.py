from django.views.generic import ListView, DetailView

from backend.articles.forms import ArticleSearchForm
from backend.articles.models import Article


class ArticleQuerysetMixin:
    queryset = Article.objects.all()


class ArticlesList(ArticleQuerysetMixin, ListView):
    template_name = 'articles/list.html'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = ArticleSearchForm(data=self.request.GET)
        search_form.is_valid()
        if search_form.cleaned_data['tags']:
            queryset = queryset.filter(tags__in=search_form.cleaned_data['tags'])
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_form'] = ArticleSearchForm(initial=self.request.GET)
        return context


class ArticleDetail(ArticleQuerysetMixin, DetailView):
    template_name = 'articles/detail.html'
