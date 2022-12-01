"""
Loading and math on brackets.
"""
import csv
from decimal import Decimal
from functools import lru_cache
from pathlib import Path
from typing import Iterator, List, Union

from bracketeering.domain import Bracket, FilingStatus


@lru_cache(10)
def get_brackets(year: int, status: FilingStatus, country: str = "us") -> List[Bracket]:
    """
    Load or get tax brackets for the year.
    """
    return list(_get_brackets(year, status, country))


def _get_brackets(year: int, status: FilingStatus, country: str = "us") -> Iterator[Bracket]:
    """
    Load tax brackets for year.
    """
    # Find csv file
    csv_file = Path(__file__).parent / Path(f"data/{country}_{year}.csv")

    if not csv_file.exists():
        raise FileNotFoundError

    with open(csv_file, "r") as f:
        min_value = 0
        for row in csv.DictReader(f):
            if status.value not in row:
                raise ValueError(f"Unknown status {status} in data.")

            max_value = Decimal(row[status.value])
            max_value = None if max_value == Decimal(-1) else max_value

            yield Bracket(
                tax_rate=Decimal(row["rate"]) / 100,
                min_value=min_value,
                max_value=max_value,
            )

            if max_value is None:
                break

            min_value = max_value


def calculate_tax(value: Union[Decimal, int, float], year: int, status: FilingStatus, country: str = "us") -> Decimal:
    """
    Calculates tax.
    """
    value = Decimal(value)
    tax = Decimal(0)

    for bracket in get_brackets(year, status, country):
        max_value = Decimal("Infinity") if bracket.max_value is None else bracket.max_value

        amount_in_bracket = min(value, max_value) - bracket.min_value
        tax += amount_in_bracket * bracket.tax_rate

        if value <= max_value:
            return tax
