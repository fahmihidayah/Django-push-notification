from . import models

from rest_framework import serializers


class PushApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PushApplication
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'description', 
            'api_key', 
        )


