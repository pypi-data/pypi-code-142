from typing import List
from dataclasses import dataclass
from datetime import date, timedelta
from pandas import DataFrame
import uuid
from pledger.interest import Interest, Interval
from pledger.account.transfer import Transfer
from pledger.account.transfers import Transfers, transfers as trans


@dataclass
class Account:
    """The account model contains transfers and methods to interact with them."""

    initial_balance: float

    transfers: Transfers

    interest: Interest | None

    length_months: int

    opened: date

    day_from_opened: int

    id: str = None

    def __init__(
        self,
        transfers: Transfers = None,
        initial_balance: float = 0,
        total_balance: float = None,
        interest: Interest = None,
        length_months: int = 12,
    ) -> None:

        self.id = str(uuid.uuid4())
        self.accrued_interest = Transfers()
        self.opened = date.today()
        self.length_months = length_months
        self.day_from_opened = 0

        if transfers is not None:
            assert isinstance(transfers, Transfers), "transfers variable incorrect type"

        self.transfers = transfers if transfers is not None else trans()

        if initial_balance == 0 and total_balance is not None:
            initial_balance = total_balance - self.transfers.get_balance()

        initial_balance = initial_balance if initial_balance is not None else 0
        self.initial_balance = initial_balance if initial_balance > 0 else 0

        self.interest = interest

    def get_transfers(self) -> Transfers:
        """Get all transfers in account."""
        return self.transfers

    def set_transfers(self, transfers: List[Transfer]) -> None:
        self.transfers += trans(transfers)

    def get_balance(self) -> float:
        """Get total account balance. Initial balance plus the balance of all transfers."""
        return self.initial_balance + self.transfers.get_balance()

    def get_interest_balance(self) -> float:
        """Get total account balance. Initial balance plus the balance of all transfers."""
        return self.transfers.get_interest()

    def calculate_final_balance(self) -> None:
        """Payout the interest if this is an interest bearing account."""
        assert self.interest is not None, "This account does not pay interest."

        for _ in range(self.length_months * 30):
            self.calculate_daily_balance()

    def calculate_daily_balance(self) -> None:
        """Calculate the total balance per day, includig initial balance, payed and accrued interest."""
        # Get the total account balance, with or without the interest.
        # If the interest is not compounded, total balance will not include interest transfers.
        balance = self.transfers.get_balance()
        if self.interest.is_compounded() is False:
            balance -= self.transfers.get_interest()

        interest = Transfer.interest(
            self.interest.calculate_interest(balance),
            date=self.get_current_day().strftime("%d/%m/%Y"),
        )

        match self.interest.payout_interval:
            case Interval.DAILY:
                self.transfers.append(interest)
            case Interval.MONTHLY:
                self.accrued_interest.append(interest)
                if self.day_from_opened % 30:
                    self.payout()
            case Interval.YEARLY:
                self.accrued_interest.append(interest)
                if self.day_from_opened % 360:
                    self.payout()

        self.day_from_opened += 1

    def payout(self) -> None:
        """Payout the interest accrued into the main account balance."""
        interest = self.accrued_interest.get_interest()
        self.transfers.append(Transfer.interest(interest))
        self.accrued_interest = Transfers()

    def get_current_day(self) -> date:
        return self.opened + timedelta(days=self.day_from_opened)

    def get_statement(self) -> DataFrame:
        """Get statement of account activity per month. Includes account growth, balance, transactions and tax."""

        def calc_percentage_diff(initial: float, current: float) -> float:
            return abs(initial - current) / current

        data = []
        prev_balance = self.initial_balance
        for transfers in self.transfers.group_by_month():
            date = transfers[0].get_datetime().strftime("%b-%Y")
            balance = prev_balance + transfers.get_balance()

            data.append(
                [
                    date,
                    prev_balance,
                    balance,
                    transfers.get_balance(),
                    round(calc_percentage_diff(prev_balance, balance), 4),
                    len(transfers),
                ]
            )
            prev_balance = balance

        return DataFrame(
            data,
            columns=[
                "Date",
                "Start Balance",
                "End Balance",
                "Growth",
                "Growth %",
                "# transfers",
            ],
        )
