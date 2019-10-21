from . import models
from . import serializers
from rest_framework import viewsets, permissions


class PushApplicationViewSet(viewsets.ModelViewSet):
    """ViewSet for the PushApplication class"""

    queryset = models.PushApplication.objects.all()
    serializer_class = serializers.PushApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


