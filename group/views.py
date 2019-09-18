from django.shortcuts import render

from rest_framework import generics, permissions, viewsets, status
from .models import Group
from .serializers import GroupSerializer, UserSerializer
from django.contrib.auth.models import User
from group.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(author=self.request.user)
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupDetail(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)

    @action(detail=True, url_path='delete_group', url_name='delete_group', methods=['DELETE'])
    def delete_group(self, request, pk):
        group_obj = self.get_object()

        if group_obj.author.id == request.user.id:
            group_obj.delete()
            return Response(f"Group with was deleted", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(f"Permission denied", status=status.HTTP_403_FORBIDDEN)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
