from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework import generics
from django.db.models import Q
from rest_framework import generics, permissions, viewsets, status

from .models import Friendship
from .serializers import FriendshipSerializer, FriendshipCreateSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from group.permissions import IsOwnerOrReadOnly


class FriendshipList(generics.ListCreateAPIView):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(Q(first_user=self.request.user) | Q(second_user=self.request.user))
        serializer = FriendshipSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save(first_user=self.request.user, first_accepted=True)


class FriendshipDetail(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipCreateSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly)

    @action(detail=True, url_path='accept_friendship', url_name='accept_friendship', methods=['POST'])
    def accept_friendship(self, request, pk):
        friendship_info = self.get_object()

        if friendship_info.first_user == friendship_info.second_user:
            return Response(f"You have got bad friends {friendship_info.first_user} and {friendship_info.second_user}",
                            status=status.HTTP_401_UNAUTHORIZED)
        elif friendship_info.first_user.id == request.user.id:
            request.serializer.save(first_accepted=True)
            return Response(f"Friendship with was deleted", status=status.HTTP_204_NO_CONTENT)
        elif friendship_info.second_user.id == request.user.id:
            request.serializer.save(second_accepted=True)
            return Response(f"Friendship with was deleted", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(f"Permission denied", status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, url_path='delete_friendship', url_name='delete_friendship', methods=['DELETE'])
    def delete_friendship(self, request, pk):
        friendship = self.get_object()

        if friendship.first_user == friendship.second_user:
            return Response(f"You have got bad friends {friendship.first_user} and {friendship.second_user}",
                            status=status.HTTP_401_UNAUTHORIZED)
        elif friendship.first_user.id == request.user.id:
            request.serializer.save(first_accepted=False)
            return Response(f"Friendship with was deleted", status=status.HTTP_204_NO_CONTENT)
        elif friendship.second_user.id == request.user.id:
            request.serializer.save(second_accepted=False)
            return Response(f"Friendship with was deleted", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(f"Permission denied", status=status.HTTP_403_FORBIDDEN)
