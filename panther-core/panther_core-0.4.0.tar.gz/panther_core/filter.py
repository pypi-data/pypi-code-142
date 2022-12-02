import ipaddress
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional

import jmespath


@dataclass
class FilterConditionBase:
    target: str
    value: Any
    operator: str
    source: Optional[str] = None
    target_type_hint: Optional[str] = None
    compiled_path: Optional[Callable[[Any], Any]] = None

    @classmethod
    def from_dict(cls, data: Dict) -> Any:
        return cls(
            source=data.get("source", None),
            target=data.get("target", ""),
            value=data.get("value", ""),
            operator=data.get("operator", ""),
            target_type_hint=data.get("targetTypeHint"),
        )

    @staticmethod
    def is_valid_dict(data: Dict) -> bool:
        return (
            data.get("target", None) is not None
            and data.get("operator", None) is not None
            and data.get("value", None) is not None
        )


class FilterOperator(ABC):  # pylint: disable=too-few-public-methods
    """
    FilterOperator is an abstract class that all operator classes should implement.

    Methods
    -------
    compare(event:Any) -> bool
        this is the main function that will run operation logic. If operation matches compare
        should return true
    """

    @abstractmethod
    def compare(self, event: Any) -> bool:
        pass


@dataclass
class FilterCondition(FilterConditionBase):
    value_is_list: Optional[bool] = None
    target_is_ip: Optional[bool] = None

    def __post_init__(self) -> None:
        if self.target.isalnum():
            # if target is alphanumeric we can call the get method
            # on the event directly for optimization purposes
            self.compiled_path = lambda x: x.get(self.target, None)
        else:
            # use jmespath whenever a more complex expression is detected
            self.compiled_path = jmespath.compile(self.target).search
        self.value_is_list = isinstance(self.value, list)
        self.target_is_ip = self.target_type_hint == "ip"


@dataclass
class BaseFilterOperator(FilterOperator):
    """
    BaseFilterOperator is the base class for all operators.
    It contains the predominant condition field that will be used for all operations.
    """

    condition: FilterCondition

    @abstractmethod
    def compare(self, event: Any) -> bool:
        pass

    def target_value(self, event: Any) -> Any:
        """
        target_value grabs the relevant path defined in the condition and extracts it from
        the provided event
        """
        return self.condition.compiled_path(event)  # type: ignore


_registered_ops: Dict[str, Callable[[FilterCondition], BaseFilterOperator]] = {}


def op(op_id: str) -> Any:  # pylint: disable=invalid-name
    """
    Registers associated operator class with the provided operator.
    Associated class gets instantiated when a comparison is made against a filter condition
    with an operator matching the provided filter operator

    e.g.
        @op('==')
        @dataclass
        class EqualOperator(BaseFilterOperator):
            pass

    Whenever a FilterCondition with the operator of '==' is detected the EqualOperator class will get
    instantiated to validate the condition
    """

    def wrap(cls: Any) -> Any:
        _registered_ops[op_id] = cls
        return cls

    return wrap


@op("==")
@dataclass
class EqualFilterOperator(BaseFilterOperator):
    def compare(self, event: Any) -> bool:
        return self.target_value(event) == self.condition.value


@op("!=")
@dataclass
class NotEqualFilterOperator(EqualFilterOperator):
    def compare(self, event: Any) -> bool:
        return not super().compare(event)


@op("<")
@dataclass
class LessThanFilterOperator(BaseFilterOperator):
    def compare(self, event: Any) -> bool:
        return self.target_value(event) < self.condition.value


@op(">")
@dataclass
class GreaterThanFilterOperator(BaseFilterOperator):
    def compare(self, event: Any) -> bool:
        return self.target_value(event) > self.condition.value


@op(">=")
@dataclass
class GreaterThanOrEqualFilterOperator(GreaterThanFilterOperator):
    equal: Optional[EqualFilterOperator] = None

    def __post_init__(self) -> None:
        self.equal = EqualFilterOperator(condition=self.condition)

    def compare(self, event: Any) -> bool:
        return super().compare(event) or self.equal.compare(event)  # type: ignore


@op("<=")
@dataclass
class LessThanOrEqualFilterOperator(LessThanFilterOperator):
    equal: Optional[EqualFilterOperator] = None

    def __post_init__(self) -> None:
        self.equal = EqualFilterOperator(condition=self.condition)

    def compare(self, event: Any) -> bool:
        return super().compare(event) or self.equal.compare(event)  # type: ignore


@op("contains")
@dataclass
class ContainsFilterOperator(BaseFilterOperator):
    def compare(self, event: Any) -> bool:
        return self.condition.value in self.target_value(event)


@op("!contains")
@dataclass
class NotContainsFilterOperator(ContainsFilterOperator):
    def compare(self, event: Any) -> bool:
        return not super().compare(event)


@op("in")
@dataclass
class InFilterOperator(BaseFilterOperator):
    def compare(self, event: Any) -> bool:
        lhs = self.target_value(event)
        rhs = self.condition.value
        result = False
        if self.condition.value_is_list and isinstance(lhs, list):
            for value in rhs:
                if value in lhs:
                    return True
        else:
            result = lhs in rhs
        return result


@op("!in")
@dataclass
class NotInFilterOperator(InFilterOperator):
    def compare(self, event: Any) -> bool:
        return not super().compare(event)


class FilterException(Exception):
    pass


def to_ip_network(value: Any) -> Any:
    if isinstance(value, list):
        raise FilterException("expected target field to be an ip or cidr but got an array")
    try:
        return ipaddress.ip_network(value, False)
    except ValueError as v:  # pylint: disable=invalid-name
        raise FilterException("invalid ip or cidr detected") from v


@op("in_cidr")
@dataclass
class InCIDRFilterOperator(BaseFilterOperator):
    """
    Expects the event value to be an ip address and expects the condition value to be a CIDR
    e.g.
    event.srcIp IN CIDR 255.255.255.240/24

    would return true if event.srcIp was 255.255.255.2

    note: this works for IPv4 and IPv6 addresses and CIDR blocks
    """

    value_converted: bool = False

    def compare(self, event: Any) -> bool:
        if not self.value_converted:
            self.condition.value = to_ip_network(self.condition.value)
            self.value_converted = True

        lhs = to_ip_network(self.target_value(event))
        rhs = self.condition.value

        return lhs.overlaps(rhs)


@op("!in_cidr")
@dataclass
class NotInCIDRFilterOperator(InCIDRFilterOperator):
    def compare(self, event: Any) -> bool:
        return not super().compare(event)


@op("contains_ip")
@dataclass
class ContainsIPFilterOperator(BaseFilterOperator):
    """
    Expects the event value to be a list of ips and expects the condition to be CIDR block
    e.g.
    p_any_ip_addresses contains_ip 255.255.255.240/24

    would return true if p_any_ip_addresses contained [255.255.255.2, 127.0.0.1]

    note: this works for IPv4 and IPv6 addresses as well as CIDR blocks
    """

    value_converted: bool = False

    def compare(self, event: Any) -> bool:
        if not self.value_converted:
            self.condition.value = to_ip_network(self.condition.value)
            self.value_converted = True
        lhs = self.target_value(event)
        if not isinstance(lhs, list):
            raise FilterException(f"expected {self.condition.target} to be a list of ips")

        ips = map(to_ip_network, lhs)
        for ip in ips:  # pylint: disable=invalid-name
            if self.condition.value.overlaps(ip):
                return True

        return False


@op("!contains_ip")
@dataclass
class NotContainsIPFilterOperator(ContainsIPFilterOperator):
    """
    Expects the event value to be a list of ips and expects the condition to be CIDR block
    e.g.
    p_any_ip_addresses not contains_ip 255.255.255.240/24

    would return false if p_any_ip_addresses contained [255.255.255.2, 127.0.0.1]

    note: this works for IPv4 and IPv6 addresses and CIDR blocks
    """

    def compare(self, event: Any) -> bool:
        return not super().compare(event)


class UnsupportedFilterOperator(Exception):
    pass


def get_compare_fn(condition: FilterCondition) -> Any:
    op_cls = _registered_ops.get(condition.operator, None)
    if op_cls is None:
        raise UnsupportedFilterOperator(f"unsupported operator id detected. ({condition.operator})")

    return op_cls(condition).compare


class Filter:  # pylint: disable=too-few-public-methods
    """
    Filter is a recursive data structure that allows filtering by any logical operation against an event.

    e.g.
        (event.srcPort > 443 && event.name IN ["hello", "world"]) || (underAttack == True || !(atPeace == True))

        would be represented as:
        {
            'or': {
                'and': [
                    {
                        'target': 'event.srcPort',
                        'operator': '>',
                        'value': 443
                    },
                    {
                        'target': 'event.name'
                        'operator': 'in',
                        'value': ['hello', 'world']
                    }
                ],
                'or': [
                    {
                        'target': 'underAttack',
                        'operator': '=',
                        'value': True
                    },
                    'not': [
                        {
                            'target': 'atPeace',
                            'operator: '=',
                            'value': True
                        }
                    ]
                ]
            }
        }

    Attributes
    ----------
    condition : Optional[FilterCondition]
        if set will contain a relevant condition
    exception : Optional[BaseException]
        if set the filter will always return with this exception when called
    ands : List[Filter]
        a list of filters if set that will be ANDed together
    ors : List[Filter]
        a list of filters if set that will be ORed together
    nots : List[Filter]
        a list of filters if set that will be ANDed together with a NOT expression

    Methods
    -------
    filter(event:Any)
        this is the main function that will filter a configured filter against an event.
        if an exception occurs during initialization of the filter it will always return the exception/
    """

    condition: Optional[FilterCondition]
    exception: Optional[BaseException] = None

    def filter(self, event: Any) -> bool:
        if self.exception:
            raise self.exception
        return self._compiled_filter(event)

    def total_conditions(self) -> int:
        total = 0
        if self.condition is not None:
            total += 1
        else:
            for field in self.nots:
                total += field.total_conditions()
            for field in self.ands:
                total += field.total_conditions()
            for field in self.ors:
                total += field.total_conditions()

        return total

    def __init__(self, info: Dict):
        if FilterCondition.is_valid_dict(info):
            self.condition = FilterCondition.from_dict(info)
        else:
            self.condition = None

        self.nots = []
        self.ors = []
        self.ands = []

        for i in info.get("not", []):
            self.nots.append(Filter(i))
        for i in info.get("and", []):
            self.ands.append(Filter(i))
        for i in info.get("or", []):
            self.ors.append(Filter(i))

        try:
            self._compiled_filter = self.__compile()
        except Exception as e:  # pylint: disable=invalid-name,broad-except
            self.exception = e

    def _compiled_or_fn(self) -> Callable[[Any], bool]:
        def _or(event: Any) -> bool:
            for ops in self.ors:
                if ops.filter(event):
                    return True
            return False

        return _or

    def _compiled_and_fn(self) -> Callable[[Any], bool]:
        def _and(event: Any) -> bool:
            for ops in self.ands:
                if ops.filter(event) is False:
                    return False
            return True

        return _and

    def _compiled_not_fn(self) -> Callable[[Any], bool]:
        def _not(event: Any) -> bool:
            for ops in self.nots:
                if ops.filter(event) is True:
                    return False

            return True

        return _not

    def __compile(self) -> Callable[[Any], bool]:
        if self.condition is not None:
            return get_compare_fn(self.condition)

        if len(self.ors) > 0:
            return self._compiled_or_fn()

        if len(self.ands) > 0:
            return self._compiled_and_fn()

        if len(self.nots) > 0:
            return self._compiled_not_fn()

        return lambda x: False
