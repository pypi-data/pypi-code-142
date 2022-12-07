from __future__ import annotations

from math import ceil

from suppy.node import Node
from suppy.orders import Orders


class AllocationFraction:  # pylint: disable=too-few-public-methods
    """Allocation fraction implementation of the supply-chain release strategy"""

    def get_releases(self, node: Node) -> Orders:  # pylint: disable=no-self-use
        """Build a set of Orders that should be released"""
        releases = Orders()
        orders = node.orders
        stock = node.stock[node]
        allocation_fraction = node.data.get("allocation_fraction", None)

        if allocation_fraction is None:
            raise TypeError(
                f"Node {node.id} did not define allocation fractions."
                f"These are defined through a dictionary where the keys are node id's, and the values are the "
                f"corresponding allocation fractions. The dictionary can be provided through"
                f"node.data['allocation_fraction']. It is assumed that the values sum up to 1."
            )

        if sum(allocation_fraction.values()) != 1:
            raise ValueError(
                f"The allocation fractions for node {node.id} do not sum up to 1."
            )

        # determine the total amount ordered
        order_total = orders.sum()
        # if there are no orders
        if order_total == 0:
            # release nothing
            return releases

        # shortage can not be negative
        shortage = max(order_total - stock, 0)

        # create an order release where the shortage is divided by allocation fraction
        for q_str, order in orders.items():
            releases[q_str] = max(
                ceil(order - shortage * allocation_fraction[q_str]), 0
            )

        # In case the rounding caused more to be released than possible, reduce the largest
        # release by 1 until the total released equals the available stock.
        while releases.sum() > stock:
            max_order_release = max(releases, key=lambda x: releases[x])
            releases.consume(max_order_release, 1)

        return releases
