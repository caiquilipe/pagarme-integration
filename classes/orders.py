from ..utils.handle_errors import handle_error_pagarme
from ..serializers.orders import OrdersSerializer
from .config import Config

import requests
import json


class Order(Config):
    @classmethod
    def get_orders(cls):
        url = Config.__url + "/orders"
        content = json.loads(
            requests.get(
                url,
                auth=Config.auth,
                headers=Config.__header,
            ).text
        )
        serializer = OrdersSerializer(data=content.get("data"), many=True)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data

    @classmethod
    def get_order(cls, pk):
        url = Config.__url + f"/orders/{pk}"
        content = json.loads(
            requests.get(
                url,
                auth=Config.auth,
                headers=Config.__header,
            ).text
        )
        serializer = OrdersSerializer(data=content)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data

    @classmethod
    def insert_order(cls, payload):
        url = Config.__url + "/orders/"
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
        serializer = OrdersSerializer(data=content)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data
