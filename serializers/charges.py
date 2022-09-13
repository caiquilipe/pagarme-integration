from .transactions import TransactionsSerializer
from .customers import CustomersSerializer

from rest_framework import serializers


class ChargesSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    gateway_id = serializers.CharField(required=False)
    amount = serializers.IntegerField(required=False)
    paid_amount = serializers.IntegerField(required=False)
    status = serializers.CharField(required=False)
    currency = serializers.CharField(required=False)
    payment_method = serializers.CharField(required=False)
    customer = CustomersSerializer()
    last_transaction = TransactionsSerializer()
