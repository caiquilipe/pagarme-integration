from rest_framework import serializers


class MessagesSerializer(serializers.Serializer):
    message = serializers.CharField(required=False)
