from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
# Create your models here.
class Skeleton(models.Model):
    creation_time = models.DateTimeField(editable=False, verbose_name=_("creation time"))
    modification_time = models.DateTimeField(default=None, editable=False, verbose_name=_("modification time"))

    def __str__(self):
        return unicode(self.pk)

    def __unicode__(self):
        return self.__str__()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.creation_time:
            self.creation_time = datetime.now()
        self.modification_time = datetime.now()
        return super(Skeleton, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Simple(Skeleton):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    name_en = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("English name"))
    description_en = models.TextField(null=True, blank=True, verbose_name=_("English description"))

    def __str__(self):
        return self.name
