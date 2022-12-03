from dataclasses import dataclass
from datetime import date, timedelta
from src.interest import Interval
from src.account import Account
from src.tax import Tax


@dataclass
class Portfolio:

    today: date

    yearly_income: float

    def __init__(self, yearly_income: float) -> None:
        self.accounts = []
        self.today = date.today()
        self.yearly_income = yearly_income

    def open_account(self, account: Account) -> None:
        self.accounts.append(account)

    def close_account(self, account_id: str) -> None:
        for acc in self.accounts:
            if acc.id == account_id:
                self.accounts.remove(acc)

    def simulate(self, years: int) -> None:
        for day in range(years * 365):
            for acc in self.accounts:
                acc.calculate_daily_balance()

            if self.today == date(self.today.year, month=4, day=5):
                interest = sum([acc.get_interest_balance() for acc in self.accounts])
                take_home_interest = Tax().take_home_interest(
                    self.yearly_income, interest
                )

                tax_to_pay = interest - take_home_interest
                print(tax_to_pay)

            self._increment_day()

    def _increment_day(self) -> None:
        self.today = self.today + timedelta(days=1)
