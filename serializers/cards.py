from rest_framework import serializers


class CardsInsertSerializer(serializers.Serializer):
    number = serializers.CharField(required=True)
    holder_name = serializers.CharField(required=True)
    exp_month = serializers.IntegerField(required=True)
    exp_year = serializers.IntegerField(required=True)
    cvv = serializers.CharField(required=True)


class CardsSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    holder_name = serializers.CharField(required=True)
    exp_month = serializers.IntegerField(required=True)
    exp_year = serializers.IntegerField(required=True)
    last_four_digits = serializers.CharField(required=True)


class CardCvvSerializer(serializers.Serializer):
    cvv = serializers.CharField(required=True)
