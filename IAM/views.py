from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions
from .permissions import CustomDjangoModelPermission
from .exceptions import NotAllowed
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, CustomDjangoModelPermission, DjangoObjectPermissions)

    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        if instance and instance.name == "SuperAdmin":
            raise NotAllowed()
        return super(GroupViewSet, self).update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        if instance and instance.name == "SuperAdmin":
            raise NotAllowed()
        return super(GroupViewSet, self).destroy(request, pk, *args, **kwargs)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAuthenticated, CustomDjangoModelPermission, DjangoObjectPermissions)
