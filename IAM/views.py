from rest_framework import viewsets
from .permissions import CRUDPermissions
from .serializers import *
from .exceptions import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CRUDPermissions]
    http_method_names = ['get', 'patch']

    def partial_update(self, request, *args, **kwargs):
        """
        - Only superuser can promote/demote other generic users to/from superusers
        - A superuser can only be modified by other superusers
        """

        is_superuser = request.user.is_superuser
        superuser_data = 'is_superuser' in request.data
        groups = 'groups' in request.data and request.data.get('groups', []) or []
        admin_group = Group.objects.get(name='SuperAdmin')
        admin_group_id = admin_group and admin_group.id or False
        instance = self.get_object()

        if not is_superuser:
            if superuser_data or admin_group_id in groups or instance.is_superuser:
                raise SuperAdminError()

        if is_superuser and superuser_data:
            # add superadmin group ID to groups when is_superuser = TRUE
            if request.data.get('is_superuser') and admin_group_id not in groups:
                groups.extend([admin_group_id])
                request.data['groups'] = groups

            # remove superadmin group ID from user groups when is_superuser = FALSE
            if not request.data.get('is_superuser') and 'groups' not in request.data:
                from builtins import filter
                instance_groups = instance.groups.values_list('id', flat=True)
                groups = list(filter(lambda i: i != admin_group_id, instance_groups))
                request.data['groups'] = groups

        return super(UserViewSet, self).partial_update(request, *args, **kwargs)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [CRUDPermissions]

    def update(self, request, *args, **kwargs):
        # assign group from user instead
        if 'users' in request.data:
            raise UserAssignmentError
        return super(GroupViewSet, self).update(request, *args, **kwargs)

    def create(self, request):
        # assign group from user instead
        if 'users' in request.data:
            raise UserAssignmentError
        return super(GroupViewSet, self).create(request)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [CRUDPermissions]
