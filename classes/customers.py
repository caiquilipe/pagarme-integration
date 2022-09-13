from classes.config import Config
from schemas.customers import CustomerSchema
from jsonschema import validate
import requests
import json


class Customer(Config, CustomerSchema):
    @classmethod
    def get_customers(cls):
        url = Config.get_url() + f"/customers"
        content = json.loads(
            requests.get(
                url,
                auth=Config.get_auth(),
                headers=Config.get_header(),
            ).text
        )
        validate(instance=content.get("data"), schema=CustomerSchema.list())
        return content

    @classmethod
    def get_customer(cls, pk):
        url = Config.get_url() + f"/customers/{pk}"
        content = json.loads(
            requests.get(
                url,
                auth=Config.get_auth(),
                headers=Config.get_header(),
            ).text
        )
        validate(instance=content, schema=CustomerSchema.get())
        return content

    @classmethod
    def insert_customer(cls, payload):
        url = Config.get_url() + f"/customers"
        header = Config.get_header
        header["Content-Type"] = "application/json"
        content = json.loads(
            requests.post(
                url,
                auth=Config.get_auth(),
                headers=header,
                json=payload,
            ).text
        )
        validate(instance=content, schema=CustomerSchema.get())
        return content
