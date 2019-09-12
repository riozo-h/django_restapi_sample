from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User, Group
from core.models import Simple, Skeleton
from django.conf import settings
from product.models import Product
# Create your models here.

class Cart(Skeleton):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='cart_set',
                             on_delete=models.PROTECT, verbose_name=_("user"))
    total_price = models.DecimalField(decimal_places=2, max_digits=20, default=0, verbose_name=_("price"))
    items =  models.ForeignKey(
        Product,
        blank=True,
        null=True,
        related_name='product_items',
        on_delete=models.CASCADE,
        verbose_name=_("cart items")
    )
    def __str__(self):
        return "%s" % self.user.username

    class Meta(Skeleton.Meta):
        verbose_name = _("cart")
        verbose_name_plural = _("carts")

class Order(Skeleton):
    NEW = 'new'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    SENT = 'sent'
    DELIVERED = 'delivered'
    DECLINED = 'declined'
    NO_RESPONSE = 'no_response'
    TRANSIT = 'transit'
    STATUSES = (
            (NEW, _("New")),
            (CONFIRMED, _("Confirmed")),
            (CANCELLED, _("Canceled")),
            (SENT, _("Sent")),
            (DELIVERED, _("Delivered")),
            (DECLINED, _("Declined")),
            (NO_RESPONSE, _("No Response")),
            (TRANSIT, _("Transit")),
    )
    UNPAID = 'unpaid'
    PAID = 'paid'
    PAYMENT_STATUSES = (
        (UNPAID, _('Unpaid')),
        (PAID, _('Paid'))
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("id"))
    payment_status = models.CharField(default=UNPAID,max_length=16, blank=True, null=True, choices=PAYMENT_STATUSES,
                                      verbose_name=_('Payment status'))
    status = models.CharField(default=NEW,max_length=32, blank=True, null=True, choices=STATUSES,
                                      verbose_name=_('Order status'))
    cart = models.ForeignKey('cart.Cart', null=True, blank=True, on_delete=models.PROTECT, verbose_name=_("cart"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='order_set',
                             on_delete=models.PROTECT, verbose_name=_("user"))
