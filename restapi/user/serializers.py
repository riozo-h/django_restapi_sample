from core.serializers import SkeletonSerializer
from user.models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserProfileSerializer(SkeletonSerializer):
    username = serializers.SerializerMethodField(required=False)
    class Meta:
        model = UserProfile
        fields = ['id','username','creation_time','credit','lang']
    def get_username(self,obj):
        if obj:
            return obj.user.username
class UserSerializer(SkeletonSerializer):
    class Meta:
        model = User
        fields = ['password','username']
