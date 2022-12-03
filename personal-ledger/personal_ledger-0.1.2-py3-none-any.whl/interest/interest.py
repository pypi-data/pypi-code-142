from dataclasses import dataclass
from enum import Enum


class Interval(Enum):
    DAILY = "daily"
    MONTHLY = "monthly"
    YEARLY = "yearly"


@dataclass
class Interest:

    rate: float

    compounded: bool = False

    payout_interval: Interval = None

    def __init__(
        self,
        rate: float,
        compounded: bool = False,
        payout_interval: Interval = Interval.YEARLY,
    ) -> None:

        assert 0 < rate < 1, "Interest rate should be between 0 and 1."
        self.rate = rate
        self.compounded = compounded
        self.payout_interval = payout_interval

    def is_compounded(self) -> bool:
        return self.compounded

    def calculate_interest(self, balance: float, interval: Interval = None) -> float:
        """Calculate the interest payout based on interest rate and user balance."""
        if interval is None:
            interval = self.payout_interval
        match interval:
            case Interval.DAILY:
                return balance * self.rate / 360
            case Interval.MONTHLY:
                return balance * self.rate / 12
            case Interval.YEARLY:
                return balance * self.rate
