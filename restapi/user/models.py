from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User, Group
from core.models import Skeleton
from django.conf import settings
# Create your models here.

class UserProfile(Skeleton):
    FA = 'fa'
    EN = 'en'
    LANGUAGES = (
        (FA, _('Farsi')),
        (EN, _('English'))
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("user"))
    credit = models.PositiveIntegerField(default=0)
    lang = models.CharField(max_length=16, default=FA, choices=LANGUAGES)

    def __str__(self):
        return "%s" % self.user

    class Meta(Skeleton.Meta):
        ordering = ['user']
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")
