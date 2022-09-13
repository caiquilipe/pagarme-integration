from .messages import MessagesSerializer

from rest_framework import serializers


class GatewayResponseSerializers(serializers.Serializer):
    code = serializers.CharField(required=False)
    errors = MessagesSerializer(many=True)
