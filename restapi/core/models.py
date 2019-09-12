from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
# Create your models here.
class Skeleton(models.Model):
    creation_time = models.DateTimeField(editable=False, verbose_name=_("creation time"),auto_now_add=True)
    modification_time = models.DateTimeField( editable=False, verbose_name=_("modification time"),auto_now=True)

    def __str__(self):
        return unicode(self.pk)

    def __unicode__(self):
        return self.__str__()

    class Meta:
        abstract = True


class Simple(Skeleton):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    name_en = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("English name"))
    description_en = models.TextField(null=True, blank=True, verbose_name=_("English description"))

    def __str__(self):
        return self.name
