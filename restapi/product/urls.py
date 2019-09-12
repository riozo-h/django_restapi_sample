from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from product import views


router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
