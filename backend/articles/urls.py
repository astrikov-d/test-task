from django.urls import path

from backend.articles.views import ArticlesList, ArticleDetail

app_name = 'articles'

urlpatterns = [
    path('<slug:slug>/', ArticleDetail.as_view(), name='detail'),
    path('', ArticlesList.as_view(), name='list')
]
