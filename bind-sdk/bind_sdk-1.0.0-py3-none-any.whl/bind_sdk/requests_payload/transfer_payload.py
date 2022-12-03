from ..requests_payload.base_payload import BasePayload


class TransferPayload(BasePayload):
    def __init__(
        self,
        origin_id: str,
        to: str,
        currency: str,
        amount: float,
        description: str,
        concept: str,
        emails: list = list(),
    ) -> None:
        self.origin_id = origin_id
        self.to = self._to(to)
        self.value = self._value(currency, amount)
        self.currency = currency
        self.amount = amount
        self.description = description
        self.concept = concept
        self.emails = emails
