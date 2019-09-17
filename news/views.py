from rest_framework import generics, permissions
from .models import News
from .serializers import NewsSerializer
from news.permissions import IsOwnerOrReadOnly


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)
