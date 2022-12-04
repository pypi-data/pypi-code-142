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

    def calculate_daily_interest(self, balance: int) -> int:
        """Calculate the interest payout based on interest rate and user balance."""
        return int(balance * self.rate / 360)

    def calculate_interest(self, balance: int) -> int:
        """Calculate the interest payout based on interest rate and user balance, based on the payout interval."""
        daily_interest = self.calculate_daily_interest(balance)
        match self.payout_interval:
            case Interval.DAILY:
                return daily_interest
            case Interval.MONTHLY:
                return daily_interest * 30
            case Interval.YEARLY:
                return daily_interest * 360
