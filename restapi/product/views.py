from django.shortcuts import render
from rest_framework import viewsets
from product.serializers import ProductSerializer,CategorySerializer
from product.models import Product,Category
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
import logging
logger = logging.getLogger('debug')
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permissions_classes = (AllowAny,)


    def create(self,request):
        data = request.data
        cat = request.data.pop('category',None)
        try:
            category = Category.objects.get(id=cat)
        except:
            return Response(status=404)
        serializer = self.serializer_class(data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            product = Product.objects.get(id=serializer.data['id'])
            product.category = category
            product.save()
            return Response(self.serializer_class(product).data,status=200)
        else:
            return Response(status=400)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permissions_classes = (AllowAny,)
