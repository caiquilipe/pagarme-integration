def handle_error_pagarme(content: dict) -> dict:
    if content.get("errors"):
        return {"detail": sum(content.get("errors").values(), [])}
    return {"detail": content.get("message")}


def handle_error_serializer(errors: dict) -> dict:
    print(errors)
    return {
        "detail": [
            f"{keys}:{str(v)}" for keys, values in errors.items() for v in values
        ]
    }
