from . import models
from . import serializers
from rest_framework import viewsets, permissions, generics


class PushApplicationViewSet(viewsets.ModelViewSet):
    """ViewSet for the PushApplication class"""

    queryset = models.PushApplication.objects.all()
    serializer_class = serializers.PushApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterTokenViewSet(viewsets.ModelViewSet):
    queryset = models.RegisteredToken.objects.all()
    serializer_class = serializers.RegisteredTokenSerializer


class RegisterTokenList(generics.ListCreateAPIView):
    queryset = models.RegisteredToken.objects.all()
    serializer_class = serializers.RegisteredTokenSerializer


class RegisterTokenCreateView(generics.CreateAPIView):
    serializer_class = serializers.RegisteredTokenSerializer

    def perform_create(self, serializer):
        return super(RegisterTokenCreateView, self).perform_create(serializer)







