# {
#     "origin_id": "556677",
#     "to": {
#         "label": "aliasCBU"
#     },
#     "value": {
#         "currency": "ARS",
#         "amount": "10"
#     },
#     "concept": "EXP",
#     "expiration": 36
# }

from ..requests_payload.base_payload import BasePayload


class DebinPayload(BasePayload):
    def __init__(
        self,
        origin_id: str,
        to: str,
        currency: str,
        amount: float,
        concept: str,
        expiration: int = 36,
    ) -> None:
        self.origin_id = origin_id
        self.to = self._to(to)
        self.value = self._value(currency, amount)
        self.concept = concept
        self.expiration = expiration
