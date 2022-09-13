class ItemSchema:
    __get = {
        "type": "object",
        "properties": {
            "amount": {"type": "number"},
            "description": {"type": "string"},
            "quantity": {"type": "number"},
        },
        "required": ["amount", "description", "quantity"],
    }

    @classmethod
    def validate_get(cls):
        return cls.__get
