from enum import Enum
from typing import List, ClassVar, Optional


class Direction(Enum):
    """
    Enumeration for sort directions.
    """

    ASC = 1
    DESC = -1

    @staticmethod
    def value_of(name: str) -> "Direction":
        """
        Returns the :class:`Direction` enum with the specified name.

        :param name: the name of the enum constant to be returned.
        :raises ValueError: in case the given value cannot be parsed into an enum value.
        :return the enum constant with the specified name.
        """
        for d in Direction:
            if d.name == name.upper():
                return d
        raise ValueError(
            f"Invalid value {name} for orders given, has to be either 'desc' or 'asc' (case insensitive)"
        )

    @staticmethod
    def values() -> List["Direction"]:
        """
        Returns an array containing the constants of this enum type, in the order they are declared.

        :return an array containing the constants of this enum type, in the order they are declared.
        """
        return [d for d in Direction]

    def is_ascending(self):
        """
        Returns whether the direction is ascending.
        """
        return self == Direction.ASC

    def is_descending(self):
        """
        Returns whether the direction is descending.
        """
        return self == Direction.DESC


class Order:
    """
    PropertyPath implements the pairing of a :class:`Direction` and a property.
    """

    DEFAULT_DIRECTION: ClassVar[Direction] = Direction.ASC

    def __init__(
        self,
        property_: str,
        direction: Optional[Direction] = DEFAULT_DIRECTION,
    ):
        if not property_:
            raise ValueError("Property must not be None or empty")
        self.property = property_
        self.direction = direction or self.DEFAULT_DIRECTION

    @classmethod
    def by(cls, property_: str) -> "Order":
        """
        Creates a new :class:`Order` instance. Takes a single property. :class:`Direction` defaults to
        Order.DEFAULT_DIRECTION.

        :param property_: must not be None or empty.
        """
        return cls(property_)

    @classmethod
    def asc(cls, property_: str) -> "Order":
        """
        Creates a new :class:`Order` instance. Takes a single property. :class:`Direction` is Direction.ASC.

        :param property_: must not be None or empty.
        """
        return cls(property_, Direction.ASC)

    @classmethod
    def desc(cls, property_: str) -> "Order":
        """
        Creates a new :class:`Order` instance. Takes a single property. :class:`Direction` is Direction.DESC.

        :param property_: must not be None or empty.
        """
        return cls(property_, Direction.DESC)

    def is_ascending(self):
        """
        Returns whether sorting for this property shall be ascending.
        """
        return self.direction.is_ascending()

    def is_descending(self):
        """
        Returns whether sorting for this property shall be descending.
        """
        return self.direction.is_descending()

    def with_direction(self, direction: Direction) -> "Order":
        """
        Returns a new :class:`Order` with the given :class:`Direction`.
        """
        return Order(self.property, direction)

    def with_property(self, property_: str) -> "Order":
        """
        Returns a new :class:`Order` with the given property.

        :param property_: must not be None or empty.
        """
        return Order(property_, self.direction)


class Sort:
    """
    Sort option for queries.

    You have to provide at least a list of properties to sort for that must not include None or empty strings. The
    direction defaults to Order.DEFAULT_DIRECTION.
    """

    def __init__(self, orders: List[Order]):
        self.orders = orders

    @classmethod
    def by(
        cls,
        *properties: str,
        direction: Optional[Direction] = Order.DEFAULT_DIRECTION,
    ) -> "Sort":
        """
        Creates a new :class:`Sort` for the given properties.

        :param properties: must not be None or contain None or empty strings.
        :param direction: defaults to Order.DEFAULT_DIRECTION
        :return:
        """
        if not properties:
            raise ValueError("You have to provide at least one property to sort by")
        return cls([Order(p, direction) for p in properties])

    @classmethod
    def unsorted(cls) -> "Sort":
        """
        Returns a :class:`Sort` instance representing no sorting setup at all.

        :return:
        """
        return cls([])

    def ascending(self) -> "Sort":
        """
        Returns a new :class:`Sort` with the current setup but ascending order direction.
        """
        for order in self.orders:
            order.direction = Direction.ASC
        return self

    def descending(self) -> "Sort":
        """
        Returns a new :class:`Sort` with the current setup but descending order direction.
        """
        for order in self.orders:
            order.direction = Direction.DESC
        return self

    def is_sorted(self) -> bool:
        return not bool(self.orders)

    def is_unsorted(self) -> bool:
        return not self.is_sorted()

    def and_(self, sort: "Sort") -> "Sort":
        """
        Returns a new :class:`Sort` consisting of the Orders of the current :class:`Sort` combined with the given ones.

        :param sort: must not be None.
        :return:
        """
        if sort is None:
            raise ValueError("Sort must not be None")
        orders = [order for order in self.orders]
        orders.extend(sort.orders)
        return Sort(orders)

    def get_order_for(self, property_: str) -> Optional[Order]:
        """
        Returns the class:`Order` registered for the given property.

        :param property_:
        :return:
        """
        for order in self.orders:
            if order.property == property_:
                return order
        return None

    def with_direction(self, direction: Direction) -> "Sort":
        """
        Creates a new :class:`Sort` with the current setup but the given order direction.

        :param direction:
        :return:
        """
        return Sort([Order(order.property, direction) for order in self.orders])
