from .gateway_response import GatewayResponseSerializers
from .cards import CardsSerializer

from rest_framework import serializers


class TransactionsSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    card = CardsSerializer()
    gateway_response = GatewayResponseSerializers()
