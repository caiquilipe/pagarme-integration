from schemas.gateway_responses import GatewayResponseSchema
from schemas.cards import CardSchema


class TransactionSchema:
    __get = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "card": CardSchema.validate_get(),
            "gateway_response": GatewayResponseSchema.validate_get(),
        },
        "required": ["id", "card", "gateway_response"],
    }

    @classmethod
    def validate_get(cls):
        return cls.__get
