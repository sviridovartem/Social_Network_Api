from rest_framework import serializers
from .models import Friendship


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('id', 'first_user', 'second_user', 'first_accepted', 'second_accepted')


class FriendshipCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('id', 'second_user')
