from rest_framework import serializers
from django.contrib.auth.models import User, Permission
from IAM.models import Group


class GroupSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True, source='user_set')
    # TODO: Use SlugRelatedField (writable) instead of StringRelatedField (readonly)
    # users = serializers.SlugRelatedField(
    #     slug_field='username',
    #     queryset=User.objects.all()
    # )

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
