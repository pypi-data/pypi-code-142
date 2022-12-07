from __future__ import annotations

from dataclasses import dataclass

from suppy.utils import context
from suppy.utils.metrics import log_event


@dataclass
class BackOrder:
    """
    A single batch of backorders

    To get the backordered quantity use BackOrders().quantity

    BackOrders can be initialized with existing backorders:
    ```
    > backorders = BackOrders(5)
    > backorders.quantity
    5
    ```

    Updates to backorders should be made using BackOrders().add() and BackOrders().deliver()
    """

    quantity: int
    period: int | None = None


class BackOrders:
    """Backorders at a specific node"""

    def __init__(self, quantity: int = 0):

        self._backorders: list[BackOrder] = []
        if quantity > 0:
            self._backorders.append(BackOrder(quantity=quantity, period=0))

    def __eq__(self, other) -> bool:
        """Consider two BackOrders with the same set of backorders equal"""
        if isinstance(other, self.__class__):
            return self._backorders == other._backorders
        return super().__eq__(other)

    @property
    def quantity(self):
        """Return total quantity to the sum of backorders"""
        return sum(backorder.quantity for backorder in self._backorders)

    def deliver(self, quantity: int):
        """Deliver back ordered customer order"""
        if quantity < 0:
            raise ValueError(
                f"Problem delivering back order. Can't deliver negative quantity, got: {quantity}"
            )

        while (quantity > 0) and (len(self._backorders) > 0):
            delivery = min(self._backorders[0].quantity, quantity)
            quantity -= delivery
            self._backorders[0].quantity -= delivery
            _log_delivery(delivery, self._backorders[0].period)
            if self._backorders[0].quantity == 0:
                self._backorders.pop(0)

    def add(self, quantity: int, period: int | None = None):
        """Create a backorder"""
        if quantity == 0:
            return
        if quantity < 0:
            raise ValueError(f"Can only create positive backorders, got: {quantity}")
        self._backorders.append(BackOrder(quantity=quantity, period=period))

    def asdict(self, *, dict_factory=dict) -> int:
        """Helper method for json serialization"""
        return self.quantity


def _log_delivery(delivery: int, delivery_period: int | None):
    """Emit the delivery metrics"""
    log_event(
        event="deliver-backorders",
        metric="backorders-delivered",
        quantity=delivery,
    )
    log_event(
        event="deliver-backorders",
        metric="wait-time",
        quantity=context.period.get() - delivery_period
        if delivery_period is not None
        else None,
    )
