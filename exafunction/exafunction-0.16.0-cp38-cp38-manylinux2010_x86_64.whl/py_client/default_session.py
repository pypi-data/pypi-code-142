# Copyright Exafunction, Inc.

"""Convenience functions for using Exafunction without managing a session.

A default session is created and automatically recreated when necessary. This
Python module currently requires the use of the environment variable
`EXA_SCHEDULER_ADDRESS` to know the location of the scheduler.

For most production use cases, managing sessions directly via
:class:`exa.Session` is recommended.
"""

import atexit
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
import warnings
import weakref

import numpy as np

from exa.py_client import module
from exa.py_client import session
from exa.py_value import value
from exa.session_pb import session_pb2
from exa.types import BaseModuleBase

# Dill is not available in the Exafunction Python 3.6 internal build.
try:
    from dill import source as dill_source
except ImportError:
    import inspect as dill_source  # type: ignore

_default_session: Optional[session.Session] = None
_default_session_atexit: Optional[Callable[..., Any]] = None
_live_modules: "weakref.WeakValueDictionary[int, module.Module]" = (
    weakref.WeakValueDictionary()
)
_live_values: "weakref.WeakSet[value.Value]" = weakref.WeakSet()
_module_construction_kwargs: Dict[int, dict] = {}
_METHOD_NAME = "_method"
_module_uid_counter = 1
_session_recreated_count = 0
_required_tags: List[str] = []
_required_hashes: List[str] = []


def _value_callback(val: value.Value):
    _live_values.add(val)


def _placement_groups_from_tags_or_hashes(
    module_tags: List[str], module_hashes: List[str]
) -> Dict[str, session.PlacementGroupSpec]:
    module_contexts = [
        session.ModuleContextSpec(module_hash=h)
        for h in module_hashes + _required_hashes
    ] + [session.ModuleContextSpec(module_tag=t) for t in module_tags + _required_tags]
    spec = session.PlacementGroupSpec(
        module_contexts=module_contexts, runner_fraction=0.1
    )
    return {"default": spec}


def _tags_and_hashes_from_live_modules() -> Tuple[List[str], List[str]]:
    module_tags: List[str] = []
    module_hashes: List[str] = []
    for uid in _live_modules.keys():
        construction_kwargs = _module_construction_kwargs[uid]
        if construction_kwargs[_METHOD_NAME] == "new_module":
            module_tags.append(construction_kwargs["module_tag"])
        elif construction_kwargs[_METHOD_NAME] == "new_module_from_hash":
            module_hashes.append(construction_kwargs["module_hash"])
        else:
            raise ValueError(
                f"Unexpected method name: {construction_kwargs[_METHOD_NAME]}"
            )
    return module_tags, module_hashes


def require_modules(
    tags: Optional[List[str]] = None, hashes: Optional[List[str]] = None
):
    """
    Adds a requirement for a module to be included in the default session.

    :param tags: Optional; the module tags to require.
    :param hashes: Optional; the module hashes to require.
    """
    if _default_session is not None:
        raise ValueError(
            "Default session already created. Please call require_modules() first."
        )
    if tags is None and hashes is None:
        raise ValueError("Must specify tags and/or hashes.")
    if tags is None:
        tags = []
    if hashes is None:
        hashes = []
    for tag in tags:
        if tag not in _required_tags:
            _required_tags.append(tag)
    for h in hashes:
        if h not in _required_hashes:
            _required_hashes.append(h)


def new_module(
    module_tag: str,
    config: Optional[Dict[str, bytes]] = None,
    module_cls: Optional[Type[BaseModuleBase]] = None,
) -> module.Module:
    """
    This is a variant of :func:`exa.Session.new_module` that uses the default
    session.

    Creates a new instance of a module from a module tag.

    :param module_tag: The module tag.
    :param config: The module configuration dictionary.
    :param module_cls: The module class to use.
    :return: The created module instance.
    """
    # pylint: disable=global-statement
    # pylint: disable=too-many-statements
    # pylint: disable=protected-access
    global _default_session, _default_session_atexit, _module_construction_kwargs
    # There should only be the default placement group.
    if _default_session is not None:
        existing_module_contexts = _default_session.session_config.placement_groups[
            0
        ].module_contexts
    else:
        existing_module_contexts = []
    for module_context in existing_module_contexts:
        if module_context.module_tag == module_tag:
            break
    else:
        # Pull all values.
        values = list(_live_values)
        value_data: List[Union[bytes, np.ndarray]] = []
        for val in values:
            if val.is_bytes():
                value_data.append(val.bytes())
            elif val.is_tensor():
                value_data.append(val.numpy().copy())
            else:
                raise ValueError(f"Unexpected value type: {val.metadata()}")

        # Recreate the session.
        if _default_session is None:
            _default_session = session.Session(
                placement_groups=_placement_groups_from_tags_or_hashes([module_tag], [])
            )
        else:
            global _session_recreated_count
            _session_recreated_count += 1
            session_config = session_pb2.SessionConfig()
            session_config.CopyFrom(_default_session.session_config)
            tags, hashes = _tags_and_hashes_from_live_modules()
            tags.append(module_tag)
            all_tags = tags + _required_tags
            all_hashes = hashes + _required_hashes
            warnings.warn(
                "Recreating the session to accommodate the new module."
                " This is not performant and should not be relied upon in production."
                " To pre-register modules for the default session, call:"
                f" exa.require_modules(tags={all_tags}"
                + (f", hashes={all_hashes}" if len(all_hashes) > 0 else "")
                + ").",
                RuntimeWarning,
            )
            del session_config.placement_groups[:]
            session_config.placement_groups.extend(
                [
                    v._to_proto(name=k)
                    for k, v in _placement_groups_from_tags_or_hashes(
                        tags, hashes
                    ).items()
                ]
            )
            assert _default_session_atexit is not None
            atexit.unregister(_default_session_atexit)
            _default_session.close()
            _default_session = session.Session(session_config=session_config)
        _default_session_atexit = _default_session.close
        atexit.register(_default_session_atexit)

        # Recreate other modules.
        new_module_construction_kwargs: Dict[int, dict] = {}
        for uid, mod in _live_modules.items():
            kwargs = _module_construction_kwargs[uid]
            new_module_construction_kwargs[uid] = kwargs
            kwargs = kwargs.copy()
            method = getattr(_default_session, kwargs.pop(_METHOD_NAME))
            new_mod = method(**kwargs)
            # Swap in the new modules.
            mod._c = new_mod._c
        _module_construction_kwargs = new_module_construction_kwargs

        # Recreate values.
        for idx, data in enumerate(value_data):
            if isinstance(data, bytes):
                values[idx]._c = _default_session.from_bytes(data)._c
            elif isinstance(data, np.ndarray):
                values[idx]._c = _default_session.from_numpy(data)._c
            else:
                raise ValueError(f"Unexpected value type: {type(data)}")

    # Create the new module.
    assert _default_session is not None
    mod = _default_session.new_module(module_tag, config, module_cls=module_cls)
    mod._value_callback = _value_callback
    global _module_uid_counter
    _live_modules[_module_uid_counter] = mod
    _module_construction_kwargs[_module_uid_counter] = {
        _METHOD_NAME: "new_module",
        "module_tag": module_tag,
        "config": config.copy() if config is not None else None,
        "module_cls": module_cls,
    }
    _module_uid_counter += 1

    return mod


def new_module_from_cls(
    module_cls: Type[BaseModuleBase],
    module_tag: str,
    config: Optional[Dict[str, bytes]] = None,
) -> module.Module:
    """
    This is a variant of :func:`exa.Session.new_module_from_cls` that uses the
    default session.

    Creates a new instance of a module from a Python class.

    Note that a python interpreter module must be included in the session's
    placement groups to use this function.

    :param module_cls: The module class. Must derive from exa.BaseModule.
    :param module_tag: The module tag for the python interpreter module.
    :param config: Optional; the module configuration dictionary.
    :return: The created module instance.
    """
    # TODO(prem): Deduplicate this with session.py.
    if config is None:
        config = {}
    config = config.copy()
    for invalid_key in ["_py_module_cls", "_py_module_name"]:
        if invalid_key in config:
            raise ValueError(
                "Config for python interpreter module may not contain key "
                + invalid_key
            )
    config["_py_module_cls"] = dill_source.getsource(module_cls).encode()
    config["_py_module_name"] = module_cls.__name__.encode()
    return new_module(module_tag, config, module_cls=module_cls)


def from_bytes(val: bytes) -> value.Value:
    """
    This is a variant of :func:`exa.Session.from_bytes` that uses the default
    session.

    Creates a new Exafunction value by copying an existing byte array.

    These values are mapped to Exafunction Bytes values.

    :param val: The byte array
    :return: The created value.
    """
    if _default_session is None:
        raise ValueError("Default session requires a module to be created first.")
    session_value = _default_session.from_bytes(val)
    _live_values.add(session_value)
    return session_value


def from_numpy(val: np.ndarray) -> value.Value:
    """
    This is a variant of :func:`exa.Session.from_numpy` that uses the default
    session.

    Creates an empty Exafunction value by copying an existing NumPy array.

    These values are mapped to Exafunction Tensor values.

    :param val: The byte array
    :return: The created value.
    """
    if _default_session is None:
        raise ValueError("Default session requires a module to be created first.")
    session_value = _default_session.from_numpy(val)
    _live_values.add(session_value)
    return session_value


def shutdown_session():
    """
    Shuts down the default session.

    This is automatically called on exit.
    """
    # pylint: disable=global-statement
    global _default_session, _default_session_atexit
    if _default_session is not None:
        _default_session.close()
        _default_session = None
    if _default_session_atexit is not None:
        atexit.unregister(_default_session_atexit)
        _default_session_atexit = None

    global _session_recreated_count, _required_tags, _required_hashes
    _session_recreated_count = 0
    _required_tags = []
    _required_hashes = []
