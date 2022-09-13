from ..utils.handle_errors import handle_error_pagarme
from ..serializers.cards import CardsSerializer
from .config import Config

import requests
import json


class Card:
    @classmethod
    def get_cards(cls, customer_id):
        url = Config.__url + f"/customers/{customer_id}/cards"
        content = json.loads(
            requests.get(
                url,
                auth=Config.auth,
                headers=Config.header,
            ).text
        )
        serializer = CardsSerializer(data=content.get("data"), many=True)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data

    @classmethod
    def get_card(cls, customer_id, pk):
        url = Config.__url + f"/customers/{customer_id}/cards/{pk}"
        content = json.loads(
            requests.get(
                url,
                auth=Config.auth,
                headers=Config.header,
            ).text
        )
        serializer = CardsSerializer(data=content)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data

    @classmethod
    def insert_card(cls, customer_id, payload):
        url = Config.__url + f"/customers/{customer_id}/cards"
        header = Config.__header
        header["Content-Type"] = "application/json"
        content = json.loads(
            requests.post(
                url,
                auth=Config.auth,
                headers=header,
                json=payload,
            ).text
        )
        serializer = CardsSerializer(data=content)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data
