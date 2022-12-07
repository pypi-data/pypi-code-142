from __future__ import annotations

import logging
from collections import UserDict
from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from typeguard import typechecked

from .backorders import BackOrders
from .edge import Edge
from .leadtime import LeadTime
from .orders import Orders
from .pipeline import Pipeline
from .stock import Stock
from .types import IdDict, LeadTimeStrategy, SalesStrategy
from .utils.metrics import log_event


class Sales(UserDict[int, list[int]]):
    """dict of sales per period"""

    @typechecked
    def __init__(
        self, _dict: Optional[dict[int, list[int]]] = None, /, **kwargs: list[int]
    ):
        super().__init__(_dict, **kwargs)

    def get_sales(self, period: int) -> list[int]:
        """Return the order-lines for a specific period"""
        return self.data.get(period, [])

    def loop_data(self, loop_size: int) -> None:
        """Shift the period of all data by 1 loop size"""
        self.data = {period + loop_size: sales for period, sales in self.items()}


@dataclass
class Node:  # pylint: disable=too-many-instance-attributes
    """A single node in a supply-chain

    A node is identified by it's `id` and can be used as a key in IdDict instances

    The behaviour of a node during simulation can be influenced by providing custom
    `sales` and `lead_time` objects.

    Any additional data for a Node can be provided using the `data` field.

    Arguments:
        id: Unique identifier of this Node
        lead_time: An object capable of returning the lead-time for a specific period
            should adhere to the LeadTimeStrategy Protocol
        sales: An object capable of returning the sales order-lines for a specific period
            should adhere to the SalesStrategy Protocol
        predecessors: A list of Edges that together could produce/assemble this Node or form the
            supplier(s) of this Node
        successors: A list of Edges that describe production/assembly relations in which this Node
            is a part, or distribution relations in which this Node is a supplier
        backorders: The outstanding backorders for this Node
            defaults to 0, provide this to initialize the simulation with existing backorders
        pipeline: A Pipeline instance for this Node
            defaults to an empty pipeline, provide this to initialize the simulation with
            existing receipts in the pipeline
        stock: Current stock levels at this Node
            defaults to an empty stock, provide this to initialize the simulation with existing
            items in stock
        orders: Outstanding orders at this Node
            default to no outstanding orders, provide this to initialize the simulation with
            existing orders at this Node
        data: dict of any additional data this Node might need
            This should be used to provide per-Node data for user-configurable parts of the sim
            For example when using the RSQ control-strategy this should contain the
            `review_time`, `reorder_level` and `order_quantity` fields.
            See `:RsqData:` for more info.
        llc: The low-level-code of this Node
            Will be automatically set/overwritten when initializing a SupplyChain with this Node
    """

    id: str
    lead_time: LeadTimeStrategy = field(default_factory=LeadTime)
    sales: SalesStrategy = field(default_factory=Sales)
    predecessors: list[Edge] = field(default_factory=list)
    successors: list[Edge] = field(default_factory=list)
    backorders: BackOrders = field(default_factory=BackOrders)
    pipeline: Pipeline = field(default_factory=Pipeline)
    stock: Stock = field(
        default_factory=lambda: Stock()  # pylint: disable=unnecessary-lambda
    )
    orders: Orders = field(
        default_factory=lambda: Orders()  # pylint: disable=unnecessary-lambda
    )
    data: dict[Any, Any] = field(default_factory=dict)
    llc: int = -1

    def __post_init__(self):
        """Verify if the provided predecessors/successors make sense"""
        for edge in self.predecessors:
            if edge.destination != self.id:
                raise ValueError(
                    f"Node {self} defined a predecessor "
                    f"with a destination that is not Node {self}: {edge}"
                )
        for edge in self.successors:
            if edge.source != self.id:
                raise ValueError(
                    f"Node {self} defined a successor "
                    f"with a source that is not Node {self}: {edge}"
                )

    def __str__(self) -> str:
        """Only include the Node ID in it's string representation

        Each node is supposed to be unique within a supply-chain so this
        is enough to identify a Node
        """
        return f"Node({self.id})"

    def __hash__(self) -> int:
        """Hash by the Node ID

        This, in combination with the dataclass generated __eq__,
        allows using a Node as a key in a dict
        Be aware that this hash does not uniquely identify this instance
        and should not be relied upon to ensure uniqueness
        """
        return hash(f"{self.id}")

    def asdict(self, *, dict_factory=dict) -> dict[str, Any]:
        """Return the dict representation of this Node"""
        result = asdict(self, dict_factory=dict_factory)
        del result["predecessors"]
        del result["successors"]
        return result

    @property
    def intercompany(self) -> bool:
        """Indicates if this Node is an inter-company Node

        A Node is considered inter-company if it has predecessors
        """
        return len(self.predecessors) > 0

    @property
    def supplier(self) -> bool:
        """Indicates if this Node is a supplier Node

        A Node is considered supplier if it has no predecessors
        """
        return len(self.predecessors) == 0

    def satisfy_received_receipts(self) -> None:
        """Update the stock with the received receipts from the pipeline"""
        received_receipts = self.pipeline.pop_received()
        self.stock.add_received(received_receipts)

    def assemble(self) -> None:
        """Assemble this node where possible

        In order to assemble the node, all needed quantities of all predecessors should be in stock
        """
        feasible = self.assemblies_feasible()
        for edge in self.predecessors:
            self.stock.consume(edge.source, feasible * edge.number)
        self.stock.add(self, feasible)

    def assemblies_feasible(self, stock: IdDict[Node, int] | None = None) -> int:
        """Returns the number of self that could be assembled from stock

        If no stock is provided use the stock at this node
        """
        if stock is None:
            stock = self.stock
        # for intercompany skus
        if self.intercompany:
            feasible = min(
                [int(stock[edge.source] / edge.number) for edge in self.predecessors]
            )
        # for supplier skus
        else:
            feasible = 0

        return feasible

    def satisfy_backorders(self) -> None:
        """Send out any backorders we can satisfy from stock"""
        if self.backorders.quantity > 0:
            feasible = min(self.stock[self], self.backorders.quantity)
            self.backorders.deliver(feasible)
            self.stock.consume(self, feasible)

    def satisfy_sales(self, period: int) -> None:
        """Satisfy sales for this period from stock

        adds backorders for any sales that could not be satisfied
        """
        order_lines = self.sales.get_sales(period)
        sales = sum(order_lines)

        if sales:
            log_event(
                event="sales",
                metric="sales",
                quantity=sales,
            )
        if order_lines:
            log_event(
                event="sales",
                metric="order-lines",
                quantity=len(order_lines),
            )

        feasible: int = min(self.stock[self], sales)
        backorders = sales - feasible
        satisfied_order_lines = 0
        if feasible > 0:
            self.stock.consume(self, feasible)

            log_event(
                event="sales",
                metric="sales-satisfied",
                quantity=feasible,
            )
            # find number of order-lines satisfied
            total = 0
            satisfied_order_lines = 0
            for quantity in order_lines:
                total += quantity
                if total > feasible:
                    break
                satisfied_order_lines += 1
            if satisfied_order_lines:
                log_event(
                    event="sales",
                    metric="order-lines-satisfied",
                    quantity=satisfied_order_lines,
                )
        if backorders > 0:
            self.backorders.add(backorders, period)
            log_event(
                event="sales",
                metric="sales-backordered",
                quantity=backorders,
            )
            log_event(
                event="sales",
                metric="order-lines-backordered",
                quantity=len(order_lines) - satisfied_order_lines,
            )

    def get_lead_time(self, period: int) -> int:
        """Return the lead-time of this Node at the provided period"""
        return self.lead_time.get_lead_time(period)

    def loop_data(self, loop_size: int):
        """Shift Sales and LeadTime data periods by loop_size"""
        self.sales.loop_data(loop_size)
        self.lead_time.loop_data(loop_size)

    def log_state(self) -> None:
        """Add a debug metric of the state of node"""

        # log stock
        for sku, stock in self.stock.data.items():
            log_event(
                level=logging.DEBUG,
                node=self,
                sku=sku,
                event="state",
                metric="stock",
                quantity=stock,
            )

        # log backorders
        log_event(
            level=logging.DEBUG,
            node=self,
            sku=self.id,
            event="state",
            metric="backorders",
            quantity=self.backorders.quantity,
        )

        # log pipeline receipts
        for rcpt in self.pipeline:
            log_event(
                level=logging.DEBUG,
                node=self,
                sku=rcpt.sku_code,
                event="state",
                metric="pipeline",
                quantity=rcpt.quantity,
            )

        # log orders
        for sku, order in self.orders.data.items():
            log_event(
                level=logging.DEBUG,
                node=self,
                sku=sku,
                event="state",
                metric="orders",
                quantity=order,
            )
