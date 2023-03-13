from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, DjangoObjectPermissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from IAM.serializers import *
from IAM.models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        serializer = GroupSerializer(self.queryset, many=True)
        if not self.check_permissions(self):
            return Response(data="User do not have permission to perform this action",
                            status=self.HTTP_403_FORBIDDEN)
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if not self.check_permissions(self):
            return Response(data="User do not have permission to perform this action",
                            status=self.HTTP_403_FORBIDDEN)
        return super(GroupViewSet, self).destroy(request, pk, *args, **kwargs)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        if not self.check_permissions(self):
            return Response(data="User do not have permission to perform this action",
                            status=self.HTTP_403_FORBIDDEN)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if not self.check_permissions(self):
            return Response(data="User do not have permission to perform this action",
                            status=self.HTTP_403_FORBIDDEN)
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if not self.check_permissions(self):
            return Response(data="User do not have permission to perform this action",
                            status=self.HTTP_403_FORBIDDEN)
        # instance = self.get_object()
        return super(UserViewSet, self).destroy(request, pk, *args, **kwargs)
