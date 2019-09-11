


from core.models import Skeleton
from rest_framework import serializers
class SkeletonSerializer(serializers.ModelSerializer):
    # creation_time = serializers.SerializerMethodField(required=False)
    # modification_time = serializers.SerializerMethodField(required=False)
    class Meta:
        model = Skeleton
        fields = '__all__'
