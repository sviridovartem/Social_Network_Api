from django.shortcuts import render
from rest_framework import generics
from .models import Friendship
from .serializers import FriendshipSerializer


class FriendshipList(generics.ListCreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


class FriendshipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
