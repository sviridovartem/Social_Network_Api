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
from django.http import HttpResponse, Http404
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

    @action(detail=True, url_path='accept_friendship', url_name='accept_friendship', methods=['get'])
    def accept_friendship(self, request, pk):
        friendship_info = self.get_object()

        if friendship_info.first_user == friendship_info.second_user:
            return Response(f"You have got bad friends {friendship_info.first_user} and {friendship_info.second_user}",
                            status=status.HTTP_401_UNAUTHORIZED)
        elif friendship_info.first_user.id == request.user.id or friendship_info.second_user.id == request.user.id:
            return Response(
                f"Friendship id: {friendship_info.id} "
                f"Friendship first user {friendship_info.first_user.username},  "
                f"Friendship second user {friendship_info.second_user.username},  "
                f"{request.user.id}", status=status.HTTP_200_OK)
        else:
            return Response(f"Permission denied", status=status.HTTP_401_UNAUTHORIZED)
        # serializer.save(second_accepted=True)




    @action(detail=True, url_path='delete_friendship', url_name='delete_friendship', methods=['DELETE'])
    def delete_friendship(self, request, pk):
        friendship = self.get_object()

        if friendship.first_user.id == request.user.id or friendship.second_user.id == request.user.id:
            friendship.delete()
            return Response(f"Friendship with was deleted", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(f"Permission denied", status=status.HTTP_401_UNAUTHORIZED)

