from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from subscription.models import Subscription
from group.models import Group
from group.serializers import GroupSerializer
from .models import News
from .serializers import NewsSerializer
from news.permissions import IsOwnerOrReadOnly
from django.db.models import Q


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = NewsSerializer(data=request.data)
        info = request.data
        try:
            Group.objects.get(id=info['group'], author=request.user)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Group.DoesNotExist:
            return Response(status=404)
        # todo check and fix


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserNewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        # Subscription.objects.get_queryset().filter(user=request.user)
        s = Subscription.objects.filter(user=request.user).values_list('group_id')
        queryset = self.get_queryset().filter(group__in=s)

        # Group.objects.get(id=info['group'], author=request.user)

        # .filter(author=self.request.user)
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)
