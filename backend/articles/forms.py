from django import forms
from taggit.models import Tag


class ArticleSearchForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
    )
