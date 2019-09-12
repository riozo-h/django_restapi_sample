from core.serializers import SkeletonSerializer
from product.models import Product, Category
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
import logging
logger = logging.getLogger('debug')

class CategorySerializer(SkeletonSerializer):
    class Meta:
        model = Category
        fields = ('id','name','name_en')
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField(required=False)
    # name = serializers.SerializerMethodField(required=False)
    class Meta:
        model = Product
        fields = ['category','name','price','rate','stack','available','id']
        # fields = '__all__'
    def get_category(self,obj):
        self.context['dynamic_fields'] = ['id', 'name','name_en']
        serializer = CategorySerializer(obj.category,partial=True,context=self.context)
        return serializer.data
    # def get_name(self,obj):
    #     return obj.name
