from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from cart import views


router = DefaultRouter()
router.register(r'cart', views.CartViewSet)
# router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
