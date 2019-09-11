from django.shortcuts import render
from rest_framework import viewsets
from user.serializers import UserSerializer, UserProfileSerializer
from user.models import UserProfile
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    permissions_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        username = request.data.get("username",None)
        password = request.data.get("password",None)
        lang = request.data.get("lang" ,'fa')
        user_serializer = UserSerializer(data={"username":username,"password":password},context={"request":request})
        if user_serializer.is_valid():
            user = user_serializer.save()
            if password:
                user.set_password(password)
                user.save()
            profile = UserProfile.objects.create(user=user,lang=lang)
            return Response(self.serializer_class(profile).data)
        else:
            return Response(status=400)
