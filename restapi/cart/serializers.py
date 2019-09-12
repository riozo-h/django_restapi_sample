from core.models import Skeleton
from core.serializers import SkeletonSerializer
from rest_framework import serializers
from cart.models import Cart, Order

class CartSerializer(SkeletonSerializer):
    class Meta:
        model = Cart
        fields = ('user','total_price','items')
