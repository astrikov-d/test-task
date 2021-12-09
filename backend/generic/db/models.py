from django.db import models
from django.utils.translation import ugettext_lazy as _ul


class TimestampedModel(models.Model):
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_ul('Creation Date')
    )

    class Meta:
        abstract = True
