from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User, Group
from core.models import Simple, Skeleton
from django.conf import settings
# Create your models here.

class Category(Simple):
    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
    def __str__(self):
        return self.name

class Product(Skeleton):

    WEAK = 'weak'
    FINE = 'fine'
    SUPERB = 'superb'
    RATES = (
        (WEAK, _('Weak')),
        (FINE, _('Fine')),
        (SUPERB, _('Superb')),

    )

    category = models.ForeignKey(Category, related_name='products',on_delete=models.PROTECT,blank=True, null=True)
    name = models.CharField(max_length=40,null=False,verbose_name=_("name"),default='None')
    price = models.DecimalField(decimal_places=2, max_digits=20, verbose_name=_("price"))
    rate = models.CharField(max_length=40, default=FINE, choices=RATES, verbose_name=_("rate"))
    stack = models.IntegerField(verbose_name=_("stack"))
    available = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name


    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
