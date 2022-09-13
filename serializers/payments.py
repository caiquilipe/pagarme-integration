from .credit_cards import CreditCardsSerializer

from rest_framework import serializers


class PaymentsSerializer(serializers.Serializer):
    payment_method = serializers.CharField(required=True)
    credit_card = CreditCardsSerializer()
