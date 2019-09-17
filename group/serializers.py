from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Group
        fields = ('id', 'name', 'author')


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'groups')
