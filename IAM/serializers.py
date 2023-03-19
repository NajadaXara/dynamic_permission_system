from rest_framework import serializers
from .models import User, Group, Permission


class GroupSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True, source='user_set', required=False)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions', 'users')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
