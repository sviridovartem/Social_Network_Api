from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Friendship
from django.shortcuts import get_object_or_404
from .serializers import FriendshipSerializer, FriendshipCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
import datetime
import json


class FriendshipList(generics.ListCreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # filter
        serializer = FriendshipSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save(first_user=self.request.user, first_accepted=True)


class FriendshipDetail(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipCreateSerializer

    @action(detail=True, url_path='accept_friendship', url_name='accept-friendship', methods=['post'])
    def accept_friendship(self, request, pk):
        self.get_object()
        # serializer.save(second_accepted=True)
        return Response("test")
