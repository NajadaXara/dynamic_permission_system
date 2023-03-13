from rest_framework import serializers
from django.contrib.auth.models import User, Permission
from IAM.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        # fields = ('id', 'name', 'permissions', 'objects', 'users')
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
