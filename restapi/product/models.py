from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User, Group
from core.models import Simple, Skeleton
from django.conf import settings
# Create your models here.

class Category(Simple):
    class Meta(Skeleton.Meta):
        verbose_name = _("category")
        verbose_name_plural = _("categories")

class Product(Simple):

    WEAK = 'weak'
    FINE = 'fine'
    SUPERB = 'superb'
    RATES = (
        (WEAK, _('Weak')),
        (FINE, _('Fine')),
        (SUPERB, _('Superb')),

    )
    cat = models.ForeignKey('product.Category', null=True, blank=True, on_delete=models.PROTECT, verbose_name=_("category"))
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0, verbose_name=_("price"))
    rate = models.CharField(max_length=40, default=FINE, choices=RATES, verbose_name=_("rate"))
    stack = models.IntegerField(verbose_name=_("stack"))
    available = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name


    class Meta(Skeleton.Meta):
        verbose_name = _("product")
        verbose_name_plural = _("products")
