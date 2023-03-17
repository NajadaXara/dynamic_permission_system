from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .exceptions import *


@receiver([pre_save, pre_delete], sender=Group)
def guard_super_admin_group(sender, instance, **kwargs):
    if instance.name == 'SuperAdmin':
        raise NotAllowed()


# class Permission(models.Model):
#
#     CRUD = [
#         ('CREATE', 'create'),
#         ('EDIT', 'edit'),
#         ('DELETE', 'delete'),
#         ('VIEW', 'view')
#     ]
#
#     name = models.CharField(max_length=255)
#     type = models.CharField(choices=CRUD, max_length=2)
#     # associated specific resource (optional),
#     # if null then it is a class permission

#     TODO: resource = content_type?
#     resource = models.SlugField(unique=True, max_length=255)
#     # inversely ordered number indicating the hierarchy among permissions
#     degree = models.IntegerField()
#     # class or instance
#     category = models.SlugField(unique=True, max_length=255)
