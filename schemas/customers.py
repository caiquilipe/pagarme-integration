from abc import abstractmethod


class CustomerSchema:
    __insert = {
        "type": "object",
        "properties": {"name": {"type": "string"}, "email": {"type": "string"}},
        "required": ["name"],
    }

    __get = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "email": {"type": "string"},
        },
        "required": ["id", "name", "email"],
    }

    __list = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "email": {"type": "string"},
            },
        },
    }

    @classmethod
    def insert(cls):
        return cls.__insert

    @classmethod
    def get(cls):
        return cls.__get

    @classmethod
    def list(cls):
        return cls.__list
