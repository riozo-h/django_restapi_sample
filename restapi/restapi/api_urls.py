from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from user.views import UserProfileViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
]
