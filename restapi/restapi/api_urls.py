from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from user.views import UserProfileViewSet
from product.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
]
