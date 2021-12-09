from django.utils.translation import ugettext_lazy as _ul

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse


class ArticleToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu(
            'articles',
            _ul('Articles'),
        )
        menu.add_sideframe_item(
            name=_ul('Article list'),
            url=admin_reverse('articles_article_changelist'),
        )
        menu.add_sideframe_item(
            name=_ul('Create an Article'),
            url=admin_reverse('articles_article_add'),
        )


toolbar_pool.register(ArticleToolbar)
