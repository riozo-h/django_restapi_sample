from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from user import views


router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet)
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
