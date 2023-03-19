from django.db.models.signals import pre_delete, pre_save, m2m_changed
from django.dispatch import receiver
from .models import *
from .exceptions import *


@receiver([pre_save, pre_delete], sender=Group)
def guard_super_admin_group(sender, instance, **kwargs):
    try:
        group_id = Group.objects.get(name='SuperAdmin').id
        if not kwargs.get("raw", False) and instance.id == group_id:
            raise NotAllowed()
    except Exception:
        pass


def update_superuser(sender, instance, action, pk_set, **kwargs):
    """
    Automatic update or is_superuser field
    when the user is or is not anymore part of SuperAdmin group.
    Triggered on M2M groups field update on User
    """
    superadmin_group = Group.objects.get(name='SuperAdmin')
    superadmin_group_id = superadmin_group and superadmin_group.id or False

    # demote from superuser when user is removed from SuperAdmin group
    if superadmin_group_id in pk_set and action == 'post_remove':
        instance.is_superuser = False
        instance.save()

    # promote to superuser when user is added to SuperAdmin group
    if superadmin_group_id in pk_set and action == 'post_add':
        instance.is_superuser = True
        instance.save()


m2m_changed.connect(update_superuser, sender=User.groups.through)
