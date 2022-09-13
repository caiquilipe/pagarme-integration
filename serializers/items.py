from rest_framework import serializers


class ItemsSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)
    description = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True)
