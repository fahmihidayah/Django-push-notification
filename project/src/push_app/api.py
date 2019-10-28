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


class RegisterTokenListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.RegisteredToken.objects.all()
    serializer_class = serializers.RegisteredTokenSerializer


class RegisterTokenRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.RegisteredToken.objects.all()
    serializer_class = serializers.RegisteredTokenSerializer





