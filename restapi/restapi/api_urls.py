from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from user.views import UserProfileViewSet
from product.views import ProductViewSet, CategoryViewSet
from cart.views import CartViewSet
router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'carts', CartViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
]
