from jsonschema.exceptions import ValidationError, SchemaError
from jsonschema import validate

from classes.customers import Customer
from classes.config import Config
from classes.orders import Order
from classes.cards import Card

from abc import abstractmethod


class PaymentGatewayClass:
    def __init__(self, key) -> None:
        Config.set_auth(key=key)

    @abstractmethod
    def get_customers():
        return Customer.get_customers()

    @abstractmethod
    def get_customer(pk):
        return Customer.get_customer(pk=pk)

    @abstractmethod
    def insert_customer(payload):
        try:
            validate(instance=payload, schema=Customer.validate_insert())
            return Customer.insert_customer(payload=Customer.mount_obj(content=payload))
        except ValidationError as ve:
            raise ve
        except SchemaError as se:
            raise se

    @abstractmethod
    def get_cards(customer_id):
        return Card.get_cards(customer_id=customer_id)

    @abstractmethod
    def get_card(customer_id, pk):
        return Card.get_card(customer_id=customer_id, pk=pk)

    @abstractmethod
    def insert_card(customer_id, payload):
        try:
            validate(instance=payload, schema=Card.validate_insert())
            return Card.insert_card(
                customer_id=customer_id, payload=Card.mount_obj(content=payload)
            )
        except ValidationError as ve:
            raise ve

    @abstractmethod
    def get_orders():
        return Order.get_orders()

    @abstractmethod
    def get_order(pk):
        return Order.get_order(pk=pk)

    @abstractmethod
    def insert_order(payload):
        try:
            validate(instance=payload, schema=Order.insert_order())
            return Order.insert_order(payload=Order.mount_obj(content=payload))
        except ValidationError as ve:
            raise ve
