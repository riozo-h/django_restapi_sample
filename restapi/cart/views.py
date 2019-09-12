from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from cart.serializers import CartSerializer
from cart.models import Cart,Order
from product.models import Product
from user.models import UserProfile
import logging
logger = logging.getLogger('debug')
# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('-id')
    serializer_class = CartSerializer
    permissions_classes = (AllowAny,)

    def create(self,request):
        items_ids = request.data.pop('items',None)
        products = Product.objects.filter(id__in=items_ids).all()
        user_id = request.data.get("user",None)
        if not user_id:
            return Response({"error":"user field is needed!"},status=400)
        try:
            userprofile = UserProfile.objects.get(id=user_id)
            user = userprofile.user
        except:
            return Response({"user not found"},status=404)
        total_price = 0
        for product in products:
            total_price += product.price
        data = {"items":items_ids,"total_price":total_price,"user":user.id}
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors,status=400)
