from django.utils.translation import gettext_lazy as _
from rest_framework import status, exceptions


class NotAllowed(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('It is not allowed to modify or delete this resource!')
    default_code = 'readonly_resource'


class SuperAdminError(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Superusers are assigned only from superusers!')
    default_code = 'check_superuser_rights'


class UserAssignmentError(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Can not assign users! Groups can only be assigned from user!')
    default_code = 'check_superuser_rights'

