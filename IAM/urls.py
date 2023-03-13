from django.urls import include, path
from rest_framework import routers
from IAM.views import GroupViewSet, UserViewSet, PermissionViewSet


router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
