from typing import Any
from typing import Dict
from typing import Iterable
from typing import List
from typing import OrderedDict

__contracts__ = ["soft_fail"]


async def distinct(hub, data: List[str or int]) -> Dict:
    """
    distinct takes a list and returns a new list with any duplicate elements removed.
    e.g. for list ["a", "b", "a", "c", "d", "b"], distinct returns new list ["a", "b", "c", "d"]
    """
    result = dict(comment=[], ret=None, result=True)
    if not data:
        result["result"] = False
        result["comment"].append(f"data for distinct is empty")
        return result
    # maintain the order of list
    result["ret"] = {"data": list(OrderedDict.fromkeys(data))}
    return result


async def flatten(hub, data: List[Any]) -> Dict:
    """
    flatten takes a list and replaces any elements that are lists with a flattened sequence of the list.
    e.g. [["a", "b"], [], ["c"]] gets replaced to ["a", "b", "c"]
    flatten can be applied to List of numbers, strings, nested lists and mixed containers.
    """
    result = dict(comment=[], ret=None, result=True)
    if not data:
        result["result"] = False
        result["comment"].append(f"data for flatten is empty")
        return result

    flat_list = list(__flatten(data))

    result["ret"] = {"data": flat_list}
    return result


def __flatten(items):
    """Yield items from any nested iterable."""
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from __flatten(item)
        else:
            yield item


async def element(hub, data: List[Any], index: int) -> Dict:
    """
    Retrieves a single element from a list.
    element can be applied to List of numbers, strings, nested lists and mixed containers.
    """
    result = dict(comment=[], ret=None, result=True)
    if not data:
        result["result"] = False
        result["comment"].append(f"data for element is empty")
        return result
    index = index % len(data)
    result["ret"] = {"data": data[index]}
    return result


async def length(hub, data: List or Dict or str) -> Dict:
    """
    length determines the length of a given list, map, or string
    """
    result = dict(comment=[], ret=None, result=True)
    if not data:
        result["result"] = False
        result["comment"].append(f"data for length is empty")
        return result

    result["ret"] = {"data": len(data)}
    return result
