from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from suppy.types import IdDict

if TYPE_CHECKING:
    from suppy import Node


@dataclass
class OrderBatch:
    """A single batch of order"""

    quantity: int
    period: int | None = None


class Orders(IdDict["Node", int]):
    """Orders placed at a node

    The key represents the target node, the value the quantity to send
    To get the orders for a specific Node, use the ID of a node or the Node instance itself:
    ```
    > orders["A"] == orders[Node("A")]
    True
    ```

    Orders can be initialized with existing outstanding orders:
    ```
    > orders = Orders({"A":5})
    > orders["A"]
    5
    ```

    Changes to orders should be applied using Orders.add() and Orders.consume()
    """

    def __init__(self, *args, **kwargs):
        self._batches: IdDict[Node, list[OrderBatch]] = IdDict()
        super().__init__(*args, **kwargs)

    def __setitem__(self, key: str | Node, value: int) -> None:
        """Prevent Order["A"] += something"""
        if key in self:
            # Allow only the first creation of any stock to happen as item access.
            # This ensures we can init an Order with a dict but stops in-place updates
            # of values
            raise TypeError(
                f"Can't update order for {key}, use .add or .consume instead"
            )
        if value < 0:
            raise ValueError(f"Order for {key} can't go below zero")
        if value == 0:
            # Initialize stock at 0, there are no batches involved
            super().__setitem__(key, value)
        else:
            self.add(key, value)

    def __missing__(self, key: Union[str, Node]) -> int:
        """When a key is missing, create the key and default to 0"""
        self.__setitem__(key, 0)
        return 0

    def _sync(self, key: str | Node):
        """Sync total quantity to the sum of the batches"""
        value = sum(batch.quantity for batch in self._batches[key])
        super().__setitem__(key, value)

    def add(self, key: str | Node, value: int, period: int | None = None):
        """Add order for a Node"""
        if value == 0:
            return
        if value < 0:
            raise ValueError(f"Can only add positive order, got: {value}")
        self._batches.setdefault(key, []).append(
            OrderBatch(quantity=value, period=period)
        )
        self._sync(key)

    def consume(self, key: str | Node, value: int) -> list[OrderBatch]:
        """Consume order of a Node"""
        if value == 0:
            return []
        if value < 0:
            raise ValueError(f"Can only consume positive order, got: {value}")
        if value > self[key]:
            raise ValueError(
                f"Can't consume more than current order ({self[key]}), got: {value}"
            )
        orders_released = []
        while (value > 0) and (len(self._batches) > 0):
            release = min(self._batches[key][0].quantity, value)
            value -= release
            self._batches[key][0].quantity -= release
            orders_released.append(
                OrderBatch(quantity=release, period=self._batches[key][0].period)
            )
            if self._batches[key][0].quantity == 0:
                self._batches[key].pop(0)

        self._sync(key)

        return orders_released

    def sum(self) -> int:
        """Return the sum of all orders"""
        return sum(self.values())
