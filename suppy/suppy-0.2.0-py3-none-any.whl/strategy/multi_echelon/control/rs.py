from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict

from suppy.node import Node
from suppy.orders import Orders
from suppy.simulator import SupplyChain


class RSData(TypedDict):
    """Typed dict with mandatory data fields when using the RS strategy"""

    review_time: int
    order_up_to_level: int


@dataclass
class RS:
    """Multi-echelon RS implementation of the supply-chain control strategy

    Arguments:
        supply_chain(SupplyChain) SupplyChain instance to fetch the echelon inventory levels from
    """

    supply_chain: SupplyChain

    def get_orders(self, node: Node, period: int) -> Orders:
        """Return the quantity of `node` to order"""

        # update the order up to level if necessary.
        self.update_control_parameters(node, period)

        # Cast node.data to RSData
        # This is only done to allow mypy to infer the types of `data` properly.
        data = RSData(
            review_time=node.data["review_time"],
            order_up_to_level=node.data["order_up_to_level"],
        )

        # Get the echelon inventory level for the requested node
        echelon_inventory = 0
        echelon = [node]
        while echelon:
            echelon_next = []
            for _node in echelon:
                echelon_inventory += self.supply_chain.inventory_assemblies_feasible(
                    _node
                )
                for edge in _node.successors:
                    if self.supply_chain.nodes[edge.destination] not in echelon_next:
                        echelon_next.append(self.supply_chain.nodes[edge.destination])
            echelon = echelon_next

        order_quantity = 0
        if period % data["review_time"] == 0:
            order_quantity = max(data["order_up_to_level"] - echelon_inventory, 0)
        orders = Orders()
        orders[node] = order_quantity
        return orders

    @staticmethod
    def update_control_parameters(node: Node, period: int) -> None:
        """
        Method that updates the control parameters if necessary.
        """
        if node.data.get("order_up_to_level_updates", None) is not None:
            node.data["order_up_to_level"] = node.data["order_up_to_level_updates"].get(
                period, node.data["order_up_to_level"]
            )

    def loop_data(self, node: Node, loop_size: int) -> None:
        """Shift the order_up_to_level_updates for the next loop"""
        if "order_up_to_level_updates" in node.data:
            node.data["order_up_to_level_updates"] = {
                period + loop_size: value
                for period, value in node.data["order_up_to_level_updates"].items()
            }
