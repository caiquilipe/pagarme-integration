from schemas.customers import CustomerSchema
from classes.customers import Customer
from classes.config import Config

from abc import abstractmethod

from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError


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
            validate(instance=payload, schema=CustomerSchema.insert)
            return Customer.insert_customer(payload=payload)
        except ValidationError as ve:
            raise ve
        except SchemaError as se:
            raise se
        """
    @abstractmethod
    def get_cards(customer_id):
        return Card.get_cards(customer_id=customer_id)

    @abstractmethod
    def get_card(customer_id, pk):
        return Card.get_card(customer_id=customer_id, pk=pk)

    @abstractmethod
    def insert_card(customer_id, payload):
        try:
            serializer = CardsInsertSerializer(data=payload)
            if not serializer.is_valid():
                raise ValidationError(detail=handle_error_serializer(serializer.errors))
            return Card.insert_card(customer_id=customer_id, payload=serializer.data)
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
            serializer = OrdersInserirSerializer(data=payload)
            if not serializer.is_valid():
                raise ValidationError(detail=handle_error_serializer(serializer.errors))
            return Order.insert_order(payload=serializer.data)
        except ValidationError as ve:
            raise ve
        """
