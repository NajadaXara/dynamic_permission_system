import copy
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class CRUDPermissions(permissions.DjangoObjectPermissions):
    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)
        return request.user.has_perms(perms)

    def has_object_permission(self, request, view, obj):
        # authentication checks have already executed via has_permission
        queryset = self._queryset(view)
        model_cls = queryset.model
        user = request.user

        user_permissions = list(user.get_all_permissions())
        perms = self.get_required_object_permissions(request.method, model_cls)

        for perm in perms:
            if perm not in user_permissions:
                raise PermissionDenied

        return True


