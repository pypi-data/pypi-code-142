import json
from typing import Dict

import yaml


__contracts__ = ["soft_fail"]


async def to_json(
    hub,
    data,
    skip_keys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    indent=None,
    separators=None,
    default=None,
    sort_keys=False,
) -> Dict:
    """
    Serialize an object to a string of JSON

    Args:
        data: It serializes the data as a JSON formatted.
        skip_keys: The default parameter for skipkeys is False, but if it is True, then dict keys that are not of a basic type (str, int, float, bool, None) will be skipped instead of raising a TypeError.
        ensure_ascii: The default value for ensure_ascii is True, and the output is assured to have all incoming non-ASCII characters escaped.
        check_circular: The default value for check_circular is True and if it is False, then the circular reference check for container types will be skipped, and a circular reference will result in an OverflowError.
        allow_nan: The default value for check_circular is True and if it is False, then it will be a ValueError to serialize out-of-range float values (nan, inf, -inf) in strict acquiescence with the JSON specification.
        indent:
            If indent is a non-negative integer or string, then JSON array elements and object members will be pretty-printed with that indent level.
            An indent level of 0, negative, or ” ” will only insert newlines. None (the default) selects the most compact representation.
            A positive integer indent indents that many spaces per level. If indent is a string (such as “\t”), that string is used to indent each level.
        separators: If specified, separators should be an (item_separator, key_separator) tuple. The default is (‘, ‘, ‘: ‘) if indent is None and (‘, ‘, ‘: ‘) otherwise. To get the most compact JSON representation, you should specify (‘, ‘, ‘:’) to trim whitespace.
        default: If specified, the default should be a function called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a TypeError. If not specified, TypeError is raised.
        sort_keys: The sort_keys parameter value is False by default, but if it is true, then the output of dictionaries will be sorted by key.
    """
    result = dict(comment=[], ret=None, result=True)
    if not data:
        result["result"] = False
        result["comment"].append(f"data for json conversion is empty")
        return result

    json_string = json.dumps(
        data,
        skipkeys=skip_keys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        indent=indent,
        separators=separators,
        default=default,
        sort_keys=sort_keys,
    )
    result["ret"] = {"data": json_string}
    return result


async def json_to_dict(
    hub,
    data: str,
    parse_float: str = None,
    parse_int: str = None,
    parse_constant: str = None,
    object_pairs_hook: str = None,
):
    """Convert the JSON String document into the Python dictionary
    Args:
        data(str):
            string that needs to be converted to Python dictionary
        parse_float(str, Optional):
            if specified, will be called with the string of every JSON float to be decoded. By default, this is equivalent to float(num_str). This can be used to use another datatype or parser for JSON floats (e.g. decimal.Decimal)
        parse_int(str, Optional):
            if specified, will be called with the string of every JSON int to be decoded. By default, this is equivalent to int(num_str). This can be used to use another datatype or parser for JSON integers (e.g. float).
        parse_constant(str, Optional):
            if specified, will be called with one of the following strings: '-Infinity', 'Infinity', 'NaN'. This can be used to raise an exception if invalid JSON numbers are encountered.
        object_pairs_hook(str, Optional):
            object_pairs_hook is an optional function that will be called with the result of any object literal decoded with an ordered list of pairs. The return value of object_pairs_hook will be used instead of the dict. This feature can be used to implement custom decoders. If object_hook is also defined, the object_pairs_hook takes priority.
    """
    result = dict(comment=(), ret=None, result=True)
    if not data:
        result["ret"] = {"data": {}}
        return result
    try:
        dict_val = json.loads(
            data,
            parse_float=parse_float,
            parse_int=parse_int,
            parse_constant=parse_constant,
            object_pairs_hook=object_pairs_hook,
        )
        result["ret"] = {"data": dict_val}
    except Exception as e:
        result["comment"] = result["comment"] + (str(e),)
        result["result"] = False
    return result


async def yaml_to_dict(hub, data: str):
    """Convert the YAML String document into the Python dictionary
    Args:
        data(str):
            string that needs to be converted to Python dictionary
    """
    result = dict(comment=(), ret=None, result=True)
    if not data:
        result["ret"] = {"data": ""}
        return result
    try:
        data = data.encode().decode("unicode-escape")
        dict_val = yaml.load(data, Loader=yaml.FullLoader)
        result["ret"] = {"data": dict_val}
    except Exception as e:
        result["comment"] = result["comment"] + (str(e),)
        result["result"] = False
    return result
