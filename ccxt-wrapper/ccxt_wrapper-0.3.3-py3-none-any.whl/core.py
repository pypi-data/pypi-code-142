from __future__ import annotations

import inspect
import warnings
from typing import Any, ForwardRef, Literal, Mapping, TypeVar, Union

T = TypeVar("T")


def cast(type_: type[T], dict_: Mapping[str, Any]) -> T:
    if not inspect.isclass(type_):
        raise TypeError("type_ must be a class")
    if not isinstance(dict_, dict):
        raise TypeError("dict_ must be a dict, got " + type(dict_).__name__)

    # Get signature of type_.__init__.
    sig = inspect.signature(type_.__init__)

    # Build a dict of kwargs for type_.__init__.
    kwargs: dict[str, Any] = {}
    for name, param in sig.parameters.items():
        if name == "self":
            continue
        # If dict_ does not have a value for this parameter, None is used.
        if name not in dict_:
            warnings.warn(RuntimeWarning(f"Cannot find key {name} in dict_"))
            kwargs[name] = None
            continue

        val = dict_[name]

        def isinstance_better(obj: object, annotation: Any) -> bool:
            if isinstance(annotation, str):
                return any(
                    [
                        a.replace(" ", "").split(".")[-1]
                        in [
                            cl.__name__
                            for cl in [obj.__class__] + obj.__class__.__subclasses__()
                        ]
                        for a in annotation.split("|")
                    ]
                )
            elif isinstance(annotation, ForwardRef):
                return isinstance_better(obj, annotation.__forward_arg__)
            elif hasattr(annotation, "__origin__"):
                origin = annotation.__origin__
                if origin is Union:
                    return any(isinstance_better(obj, t) for t in annotation.__args__)
                elif origin is Literal:
                    return any(obj == t for t in annotation.__args__)
                else:
                    return isinstance(obj, origin)

            if not inspect.isclass(annotation):
                warnings.warn(RuntimeWarning(f"Unknown annotation {annotation}"))
                return True
                # raise TypeError("annotation must be a class")
            return isinstance(obj, annotation)

        # Check if the type of val is compatible with the type of param.
        if not isinstance_better(val, param.annotation):
            # warnings.warn(
            #    RuntimeWarning(
            #        f"{name} is not of type {param.annotation}, "
            #        + f"but {type(val)}, value: {val}"
            #    )
            # )
            pass
        kwargs[name] = val

    # Warn if dict_ has keys that are not in kwargs.
    for name in dict_:
        if name not in kwargs:
            warnings.warn(RuntimeWarning(f"{name} is not a parameter of {type_}"))

    # Return an instance of type_.
    return type_(**kwargs)
