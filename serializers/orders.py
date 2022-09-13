from .payments import PaymentsSerializer
from .charges import ChargesSerializer
from .items import ItemsSerializer

from rest_framework import serializers


class OrdersInserirSerializer(serializers.Serializer):
    customer_id = serializers.CharField(required=True)
    items = ItemsSerializer()
    payments = PaymentsSerializer()


class OrdersSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    items = ItemsSerializer(many=True)
    charges = ChargesSerializer()
