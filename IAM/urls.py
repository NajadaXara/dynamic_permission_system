from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'permissions', views.PermissionViewSet)

urlpatterns = [
   path('', include(router.urls))
]
