from django.http import Http404
from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from .models import Subscription
from .serializers import SubscriptionSerializer, SubscriptionCreateSerializer


class SubscriptionList(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user=self.request.user)
        serializer = SubscriptionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SubscriptionCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(f"permission denied", status=status.HTTP_403_FORBIDDEN)


class SubscriptionDetail(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.user.id == request.user.id:
                self.perform_destroy(instance)
                return Response(f"Subscription with was deleted", status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(f"Permission denied", status=status.HTTP_403_FORBIDDEN)
        except Http404:
            pass
