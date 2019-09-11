from django.shortcuts import render
from rest_framework import viewsets
from user.serializers import UserSerializer, UserProfileSerializer
from user.models import UserProfile
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permissions_classes = (AllowAny,)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('-id')
    serializer_class = UserProfileSerializer
    permissions_classes = (AllowAny,)
