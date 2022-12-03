from ..helpers.is_alias import is_alias


class BasePayload:
    def _to(self, to: str) -> bool:
        if is_alias(to):
            return {"label": to}
        else:
            return {"cbu": to}

    def _value(self, currency, amount):
        return {"currency": currency, "amount": amount}

    def to_json(self):
        return self.__dict__
