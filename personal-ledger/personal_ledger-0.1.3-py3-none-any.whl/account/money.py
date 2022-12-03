from __future__ import annotations
from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum


class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"


@dataclass
class Money:

    amount: int

    currency: Currency = Currency.GBP

    def __post_init__(self):
        if isinstance(self.amount, float):
            self.amount = int(self.amount)

        assert self.currency.value in [
            c.value for c in Currency
        ], f"Currency {self.currency.value} is not supported"

        if isinstance(self.currency, str):
            self.currency = Currency(self.currency)

    @abstractmethod
    def zero(currency: Currency = Currency.GBP) -> Money:
        return Money(0, currency)

    def __add__(self, val: Money) -> Money:
        return Money(self.amount + val.amount)

    def __iadd__(self, val: Money) -> Money:
        return Money(self.amount + val.amount)

    def __sub__(self, val: Money) -> Money:
        return Money(self.amount - val.amount)

    def __isub__(self, val: Money) -> Money:
        return Money(self.amount - val.amount)

    def __mul__(self, val: Money) -> Money:
        return Money(self.amount * val.amount)

    def __truediv__(self, val: Money) -> Money:
        return Money(self.amount / val.amount)

    def __mod__(self, val: Money) -> Money:
        return Money(self.amount % val.amount)

    def __lt__(self, val: Money) -> bool:
        return self.amount < val.amount

    def __le__(self, val: Money) -> bool:
        return self.amount <= val.amount

    def __eq__(self, val: Money) -> bool:
        return self.amount == val.amount

    def __eq__(self, val: Money) -> bool:
        return self.amount != val.amount

    def __ge__(self, val: Money) -> bool:
        return self.amount >= val.amount

    def __gt__(self, val: Money) -> bool:
        return self.amount > val.amount
