from django.db import models
from django.contrib.auth.models import User, Group


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
