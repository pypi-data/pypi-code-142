from __future__ import annotations
from typing import List
from datetime import datetime, date
from pledger.account.transfer import Transfer, TransferType


def transfers(*transfers: List[Transfer]) -> Transfers:
    t = Transfers()
    if len(transfers) == 0:
        return t

    if isinstance(transfers[0], list):
        transfers = transfers[0]

    for trans in transfers:
        assert isinstance(trans, Transfer), "Not instance of Transfer class"
        t.append(trans)

    return t


class Transfers(list):
    def __init__(self, *data: List[Transfer]):
        super(Transfers, self).__init__(data)

    def __add__(self, transfers: Transfers) -> Transfers:
        res = Transfers()
        for t in self:
            res.append(t)

        for t in transfers:
            res.append(t)

        return res

    def _str_to_dt(self, value: str) -> datetime:
        """Transform string of format %d/%m/%Y to datetime"""
        return datetime.strptime(value, "%d/%m/%Y")

    def between(self, from_date: str, to_date: str) -> Transfers:
        res = Transfers()
        for t in self:
            if (
                self._str_to_dt(from_date)
                <= t.get_datetime()
                < self._str_to_dt(to_date)
            ):
                res.append(t)

        return res

    def from_date(self, from_date: str) -> Transfers:
        res = Transfers()
        for t in self:
            if self._str_to_dt(from_date) <= t.get_datetime():
                res.append(t)

        return res

    def to_date(self, to_date: str) -> Transfers:
        res = Transfers()
        for t in self:
            if t.get_datetime() < self._str_to_dt(to_date):
                res.append(t)

        return res

    def last_month(self) -> Transfers:
        first_day_of_current_month = date.today().replace(day=1)
        first_day_of_last_month = first_day_of_current_month.replace(
            month=first_day_of_current_month.month - 1
        )
        if first_day_of_last_month.month == 12:
            first_day_of_last_month.replace(year=first_day_of_last_month.year - 1)

        return self.between(
            first_day_of_last_month.strftime("%d/%m/%Y"),
            first_day_of_current_month.strftime("%d/%m/%Y"),
        )

    def current_month(self) -> Transfers:
        first_day_of_current_month = date.today().replace(day=1)

        return self.from_date(
            first_day_of_current_month.strftime("%d/%m/%Y"),
        )

    def last_year(self) -> Transfers:
        first_day_of_current_year = date.today().replace(day=1, month=1)
        first_day_of_last_year = first_day_of_current_year.replace(
            year=first_day_of_current_year.year - 1
        )

        return self.between(
            first_day_of_current_year.strftime("%d/%m/%Y"),
            first_day_of_last_year.strftime("%d/%m/%Y"),
        )

    def current_year(self) -> Transfers:
        first_day_of_current_year = date.today().replace(day=1, month=1)

        return self.from_date(
            first_day_of_current_year.strftime("%d/%m/%Y"),
        )

    def get_balance(self) -> float:
        balance = 0
        for t in self:
            balance += t.amount

        return balance

    def get_interest(self) -> float:
        return sum(t.amount for t in self if t.transfer_type == TransferType.INTEREST)

    def get_credits(self) -> float:
        """Money going out of the account"""
        balance = 0
        for t in self:
            if t.amount < 0:
                balance += t.amount

        return balance

    def get_debits(self) -> float:
        """Money going into the account"""
        balance = 0
        for t in self:
            if t.amount > 0:
                balance += t.amount

        return balance

    def group_by_month(self) -> List[Transfers]:
        res = {}
        for t in self:
            key = t.get_datetime().strftime("%b-%Y")
            if key not in res:
                res[key] = Transfers(t)
                continue

            res[key].append(t)

        return list(res.values())
