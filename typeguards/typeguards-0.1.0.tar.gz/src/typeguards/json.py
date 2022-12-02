"""TypeGuard_ functions for JSON and JSON schemas.

.. _TypeGuard:
   https://docs.python.org/3/library/typing.html?highlight=typeguard#typing.TypeGuard

"""

from collections.abc import Iterable, Sequence
from inspect import get_annotations
import logging
from types import UnionType
from typing import Callable, Dict, List, Optional, Tuple, TypeAlias, TypeGuard, Union

JSONKey: TypeAlias = str
"""JSON key type."""

JSONValue = (
    str | int | float | bool | None | List["JSONValue"] | Dict[JSONKey, "JSONValue"]
)
"""JSON value type defined recursively."""

JSON = Dict[JSONKey, JSONValue]
"""JSON type."""


def is_json(value: object) -> TypeGuard[JSON]:
    """Type narrow an ``object`` to :data:`JSON`.

    Perform a deep check on a ``Dict`` to ensure that each key is a :data:`JSONKey`,
    and each value is a :data:`JSONValue`.

    Args:
        value: The ``object`` to narrow.

    Returns:
        ``True`` if ``value`` is a ``Dict`` of JSON keys and values.

    """
    res = isinstance(value, Dict) and all(
        is_json_key(maybe_json_key) and is_json_value(maybe_json_value)
        for maybe_json_key, maybe_json_value in value.items()
    )
    logger.debug("\n\tvalue=%s\n\tres=%s", value, res)
    return res


def is_json_key(key: object) -> TypeGuard[JSONKey]:
    """Type narrow an ``object`` to :data:`JSONKey`.

    Args:
        key: The ``object`` to narrow.

    Returns:
        ``True`` if ``key`` is a JSON key.

    """
    return isinstance(key, JSONKey)


def is_json_value(value: object) -> TypeGuard[JSONValue]:
    """Type narrow an ``object`` to :data:`JSONValue`.

    Perform a deep check on an ``object`` to ensure that it is a JSON value.

    Args:
        value: The ``object`` to narrow.

    Returns:
        ``True`` if ``value`` is a JSON value.

    """
    return _is_json_simple_value(value) or _is_json_list_value(value) or is_json(value)


def _is_json_simple_value(value: object) -> bool:
    """Check that an ``object`` is a simple JSON value: ``str | int | float | bool
    | None``

    Args:
        value: The ``object`` to check.

    Returns:
        ``True`` if ``value`` is a simple JSON type.

    """
    return isinstance(value, str | int | float | bool | None)


def _is_json_list_value(value: object) -> bool:
    """Check that an ``object`` is a ``List`` of :data:`JSONValue`.

    Performs a deep check on each item of the list.

    Args:
        value: The ``object`` to check.

    Returns:
        ``True`` if ``value`` is a ``List`` of JSON values.

    """
    return isinstance(value, List) and all(
        is_json_value(maybe_json_value) for maybe_json_value in value
    )


SchemaT = type | UnionType | Tuple[type | UnionType, ...]
"""Schema type, in general."""

_CheckSchemaTypeValue = Callable[[object, SchemaT], bool]
"""Function type that checks if a value conforms to a :ref:`schema type<Schema Types>`.
"""


def is_json_schema(value: object, schema: SchemaT) -> TypeGuard[SchemaT]:
    """Type narrow an ``object`` to a JSON schema.

    Perform a deep check on a ``Dict`` to ensure that it conforms to a schema. If
    a schema specifies the keys that may exist in the ``Dict``, and types for their
    values, then the ``Dict`` may not contain any keys not in the schema. Each value
    in the ``Dict`` must also be an instance of the type associated with its key in
    the schema. Note that the ``Dict`` does not have to contain every key defined
    in the schema.

    .. _Schema Types:

    **Schema Types**

    A schema must describe the keys and values in a ``Dict``, and can be:

        - an annotated ``object``, such as a ``NamedTuple`` or ``TypedDict``
        - a generic ``Dict`` of :data:`JSONKey` keys and :data:`JSONValue` or schema
          type values
        - a ``Dict`` of :data:`JSONKey` keys and :data:`JSONValue` values
        - a generic union of any of the preceding schema types

    The types of the keys in a schema can also be any of the preceding schema types,
    as well as any of these addtional schema types:

        - a generic union of any of the :data:`JSONValue` types, or schema types
        - a generic ``List`` of any of the :data:`JSONValue` types, or schema types
        - a ``List`` of :data:`JSONValue`
        - a simple JSON value: ``str | int | float | bool | None``

    Args:
        value: The ``object`` to narrow. This must be a ``Dict``.
        schema: An ``object`` that describes the schema for a ``Dict``.

    Returns:
        ``True`` if ``value`` is a ``Dict`` that conforms to ``schema``.

    .. _annotated: https://docs.python.org/3/howto/annotations.html

    """
    res = isinstance(value, Dict) and _is_json_schema_value(value, schema)
    logger.debug("\n\tvalue=%s\n\tschema=%s\n\tres=%s", value, schema, res)
    return res


def _is_json_schema_value(value: object, schema: SchemaT) -> bool:
    """Check that an ``object`` conforms to a :ref:`schema type<Schema Types>`.

    Args:
        value: The ``object`` to check. This may be the entire ``Dict``, or one of
            its values.
        schema: An ``object`` that describes the schema for a value.

    Returns:
        ``True`` if ``value`` conforms to ``schema``.

    """
    check_schema_type_value = _select_json_check_schema_type_value(schema)
    res = check_schema_type_value(value, schema) if check_schema_type_value else False
    logger.debug(
        "\n\tvalue=%s\n\tschema=%s\n\tcheck_fn=%s\n\tres=%s",
        value,
        schema,
        check_schema_type_value.__name__ if check_schema_type_value else None,
        res,
    )
    return res


def _select_json_check_schema_type_value(  # pylint: disable=too-many-return-statements
    schema: SchemaT,
) -> Optional[_CheckSchemaTypeValue]:
    """Determine the :ref:`schema type<Schema Types>` for ``schema``.

    Args:
        schema: An ``object`` that describes the schema for a value.

    Returns:
        The function that checks if a value conforms to the schema type of
        ``schema``. ``None`` if ``schema`` doesn't describe a schema type.

    """
    if isinstance(schema, type):
        if _try_issubclass(schema, str | int | float | bool | None):
            return _is_json_schema_value_simple

        if get_annotations(schema):
            return _is_json_schema_value_annotated

    generic_type = getattr(schema, "__origin__", None)
    generic_params = getattr(schema, "__args__", None)
    if (generic_type is Union or isinstance(schema, UnionType)) and isinstance(
        generic_params, Iterable
    ):
        return _is_json_schema_value_generic_union

    if generic_type is not None and isinstance(generic_params, Sequence):
        if _try_issubclass(generic_type, List) and len(generic_params) == 1:
            return _is_json_schema_value_generic_list

        if _try_issubclass(generic_type, Dict) and len(generic_params) == 2:
            return _is_json_schema_value_generic_dict

    if _try_issubclass(schema, List):
        return _is_json_schema_value_list

    if _try_issubclass(schema, Dict):
        return _is_json_schema_value_dict

    return None


def _is_json_schema_value_simple(value: object, schema: SchemaT) -> bool:
    """Check that an ``object`` conforms to a simple JSON value: ``str | int | float |
    bool | None``.

    Args:
        value: The ``object`` to check. This must be a simple JSON value.
        schema: A simple JSON value type.

    Returns:
        ``True`` if ``value`` is a simple JSON value.

    """
    return _is_json_simple_value(value) and isinstance(value, schema)


def _is_json_schema_value_annotated(value: object, schema: SchemaT) -> bool:
    """Check that an ``object`` is a ``Dict`` where each key exists in the annotations
    for ``schema``, and each value is an instance of the type associated with its
    key in the schema.

    Args:
        value: The ``object`` to check. This must be a ``Dict``.
        schema: An ``object`` with annotations that describes the schema, e.g., a
            ``NamedTuple`` or a ``TypedDict``.

    Returns:
        ``True`` if ``value`` is a ``Dict`` that conforms to ``schema``.

    """
    if not isinstance(value, Dict):
        return False

    assert isinstance(schema, type)
    anns = get_annotations(schema)
    return all(
        is_json_key(each_key)
        and _is_json_schema_value(each_value, anns.get(each_key, None))
        for each_key, each_value in value.items()
    )


def _is_json_schema_value_generic_union(value: object, schema: SchemaT) -> bool:
    """Check that an ``object`` conforms to one of the :ref:`schema types<Schema
    Types>` in a union of schema types.

    Args:
        value: the ``object`` to check.
        schema: A union that consists of other schema types.

    Returns:
        ``True`` if ``schema`` is union of schema types, and ``value`` conforms to
        one of those types.

    """
    generic_params = getattr(schema, "__args__", None)
    assert isinstance(generic_params, Iterable)
    return any(
        _is_json_schema_value(value, generic_param) for generic_param in generic_params
    )


def _is_json_schema_value_generic_list(value: object, schema: SchemaT) -> bool:
    """Check that an ``object`` conforms to a ``List`` of :data:`JSONValue` or
    :ref:`schema type<Schema Types>` values.

    Args:
        value: The ``object`` to check. This must be a ``List``.
        schema: A generic ``List`` of JSON values or schema types.

    Returns:
        ``True`` if ``value`` is a ``List`` that conforms to ``schema``.

    """
    if not isinstance(value, List):
        return False

    generic_params = getattr(schema, "__args__", None)
    assert isinstance(generic_params, Sequence)
    return all(
        _is_json_schema_value(each_value, generic_params[0]) for each_value in value
    ) or (generic_params[0] is object and _is_json_list_value(value))


def _is_json_schema_value_generic_dict(value: object, schema: SchemaT) -> bool:
    """Check that an ``object`` conforms to a ``Dict`` of :data:`JSONKey` keys,
    and :data:`JSONValue` or :ref:`schema type<Schema Types>` values.

    Args:
        value: The ``object`` to check. This must be a ``Dict``.
        schema: A generic ``Dict`` type of JSON keys, and JSON values or schema
            type values.

    Returns:
        ``True`` if ``value`` is a ``Dict`` that conforms to ``schema``.

    """
    if not isinstance(value, Dict):
        return False

    generic_params = getattr(schema, "__args__", None)
    assert isinstance(generic_params, Sequence)
    return (
        _try_issubclass(generic_params[0], str)
        and all(
            is_json_key(each_key)
            and _is_json_schema_value(each_value, generic_params[1])
            for each_key, each_value in value.items()
        )
    ) or (generic_params[1] is object and is_json_value(value))


def _is_json_schema_value_list(value: object, _: SchemaT) -> bool:
    """Check that an ``object`` is a ``List`` of :data:`JSONValue` values.

    Args:
        value: The ``object`` to check. This must be a ``List``.

    Returns:
        ``True`` if ``value`` is a ``List`` of JSON values.

    """
    return _is_json_list_value(value)


def _is_json_schema_value_dict(value: object, _: SchemaT) -> bool:
    """Check that an ``object`` is a ``Dict`` of :data:`JSONKey` keys and
    :data:`JSONValue` values.

    Args:
        value: The ``object`` to check. This must be a ``Dict``.

    Returns:
        ``True`` if ``value`` is a ``Dict`` of str keys and JSON values.

    """
    return is_json(value)


def _try_issubclass(subcls: SchemaT, cls: SchemaT) -> bool:
    """Check that a ``type`` is a subclass of another ``type`` with error handling.

    ``issubclass``_ will raise a ``TypeError`` if ``subcls`` or ``cls`` can't be
    used in a subclass comparison.

    Args:
        subcls: The class to check.
        cls: The class to check against.

    Returns:
        ``True`` if ``subcls`` is a subclass of ``cls``. ``False`` if ``subcls``
        is not a subclass of ``cls``, or ``issubclass`` raises a ``TypeError``.

    .. _issubclass:
        https://docs.python.org/3/library/functions.html#issubclass

    """
    try:
        return issubclass(subcls, cls)  # type: ignore
    except TypeError:
        return False


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
