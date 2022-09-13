from rest_framework import serializers

from .cards import CardCvvSerializer


class CreditCardsSerializer(serializers.Serializer):
    capture = serializers.BooleanField(required=True)
    statement_descriptor = serializers.CharField(required=False)
    card_id = serializers.CharField(required=True)
    card = CardCvvSerializer()
