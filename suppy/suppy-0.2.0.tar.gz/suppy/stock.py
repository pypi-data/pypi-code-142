from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from suppy.pipeline import Receipt
from suppy.types import IdDict

if TYPE_CHECKING:
    from suppy import Node


@dataclass
class StockBatch:
    """A single batch of stock"""

    quantity: int
    period: int | None = None


class Stock(IdDict["Node", int]):
    """Stock levels at a specific node

    Each node can have stock for itself and any other node

    To get the stock level, use the ID of a node or the Node instance itself:
    ```
    > stock["A"] == stock[Node("A")]
    True
    ```

    Stock can be initialized with existing stock:
    ```
    > stock = Stock({"A":5})
    > stock["A"]
    5
    ```

    Changes to stock should be done using Stock.add() and Stock.consume()
    """

    def __init__(self, *args, **kwargs):
        self._batches: IdDict[Node, list[StockBatch]] = IdDict()
        super().__init__(*args, **kwargs)

    def __setitem__(self, key: str | Node, value: int) -> None:
        """Prevent Stock["A"] += something"""
        if key in self:
            # Allow only the first creation of any stock to happen as item access.
            # This ensures we can init a Stock with a dict but stops in-place updates
            # of values
            raise TypeError(
                f"Can't update stock for {key}, use .add or .consume instead"
            )
        if value < 0:
            raise ValueError(f"Stock for {key} can't go below zero")
        if value == 0:
            # Initialize stock at 0, there are no batches involved
            super().__setitem__(key, value)
        else:
            self.add(key, value)

    def __missing__(self, key: str | Node) -> int:
        """When a key is missing, return 0"""
        return 0

    def _sync(self, key: str | Node):
        """Sync total quantity to the sum of the batches"""
        value = sum(batch.quantity for batch in self._batches[key])
        super().__setitem__(key, value)

    def add_received(self, received: list[Receipt]) -> None:
        """Add the received receipts to the stock"""
        for receipt in received:
            self.add(receipt.sku_code, value=receipt.quantity)

    def add(self, key: str | Node, value: int, period: int | None = None):
        """Add stock for a Node"""
        if value == 0:
            return
        if value < 0:
            raise ValueError(f"Can only add positive stock, got: {value}")
        self._batches.setdefault(key, []).append(
            StockBatch(quantity=value, period=period)
        )
        self._sync(key)

    def consume(self, key: str | Node, value: int):
        """Consume stock of a Node"""
        if value == 0:
            return
        if value < 0:
            raise ValueError(f"Can only consume positive stock, got: {value}")
        if value > self[key]:
            raise ValueError(
                f"Can't consume more than current stock ({self[key]}), got: {value}"
            )
        batches_consumed = []
        for batch in self._batches[key]:
            if value < batch.quantity:
                batch.quantity -= value
                break
            value -= batch.quantity
            batches_consumed.append(batch)
            if value == 0:
                break

        for batch in batches_consumed:
            self._batches[key].remove(batch)

        self._sync(key)
