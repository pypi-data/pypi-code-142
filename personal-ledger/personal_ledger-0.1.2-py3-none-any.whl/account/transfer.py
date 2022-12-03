from __future__ import annotations
from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime, date
from enum import Enum
import uuid


class TransferType(Enum):
    DEPOSIT = "deposit"
    INTEREST = "interest"
    DIVIDEND = "dividend"
    WITHDRAWAL = "withdrawal"
    TAX = "tax"


class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"


@dataclass
class Transfer:

    amount: float

    currency: Currency

    transfer_type: TransferType

    category: str = None

    note: str = None

    date: str = None

    id: str = None

    def __init__(
        self,
        amount: float,
        currency: Currency,
        transfer_type: TransferType,
        category: str = None,
        note: str = None,
        date: str = None,
        id: str = None,
    ) -> None:

        if isinstance(amount, str):
            amount = float(amount)

        if transfer_type in [TransferType.WITHDRAWAL, TransferType.TAX]:
            assert amount < 0, "Amount must be negative."

        if transfer_type in [
            TransferType.DEPOSIT,
            TransferType.INTEREST,
            TransferType.DIVIDEND,
        ]:
            assert amount >= 0, "Amount must be positive."

        self.amount = float(amount) if isinstance(amount, str) else amount
        self.currency = currency
        self.transfer_type = transfer_type
        self.category = category
        self.note = note
        self.date = date if date is not None else datetime.now().strftime("%d/%m/%Y")
        self.id = id if id is not None else str(uuid.uuid4())

    @abstractmethod
    def deposit(amount: float, date: str = None) -> Transfer:
        return Transfer(amount, Currency.GBP, TransferType.DEPOSIT)

    @abstractmethod
    def interest(amount: float, date: str = None) -> Transfer:
        return Transfer(amount, Currency.GBP, TransferType.INTEREST, date=date)

    def get_datetime(self) -> datetime:
        """Transform string of format %d/%m/%Y to datetime"""
        return datetime.strptime(self.date, "%d/%m/%Y")
