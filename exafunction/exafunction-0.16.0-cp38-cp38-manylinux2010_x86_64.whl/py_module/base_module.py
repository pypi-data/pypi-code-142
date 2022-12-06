# Copyright Exafunction, Inc.

import abc
import functools
import inspect
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

from typing_extensions import is_typeddict  # type: ignore

import exa._C as _C
from exa.common_pb.common_pb2 import ModuleInfo
from exa.py_module.base_module_context import BaseModuleContext
from exa.py_module.base_module_context import wrap_call
from exa.py_module.method_context import MethodContext
from exa.py_value.value import Value
from exa.types import AutoModuleBase
from exa.types import BaseModuleBase
from exa.types import ExaMethodOutputType
from exa.types import ExportDecoratorBase


class BaseModule(BaseModuleBase):
    """Base class for Exafunction PyModules."""

    def _initialize(self, config_map: Dict[str, bytes]) -> None:
        self.initialize(config_map)

    def initialize(self, config_map: Dict[str, bytes]) -> None:
        pass

    # pylint: disable=unused-argument
    def module_info(self, module_ctx) -> ModuleInfo:
        info = ModuleInfo()
        for name, (inputs, outputs) in getattr(type(self), "_methods", {}).items():
            m = info.method_infos[name]
            for input_ in inputs:
                m.inputs[input_].SetInParent()
            for output in outputs:
                m.outputs[output].SetInParent()
        return info

    def _module_info(self, module_ctx: BaseModuleContext) -> str:
        info = self.module_info(module_ctx)
        return info.SerializeToString()

    def _run_method(
        self,
        ctx: MethodContext,
        method_name: str,
        inputs: Dict[str, _C.Value],
    ) -> Dict[str, _C.Value]:
        m = getattr(self, method_name)
        py_inputs = {k: Value(v) for k, v in inputs.items()}
        py_outputs = wrap_call(m, ctx, py_inputs)
        # pylint: disable=protected-access
        return {k: v._c for k, v in py_outputs.items()}


class AutoModuleMeta(abc.ABCMeta):
    """Metaclass to auto-capture input names."""

    def __new__(cls, name, bases, attrs):
        # _method_inputs and _method_types should contain information for every method.
        # _method_outputs only contains information for methods that have return type
        # annotations.
        attrs["_method_inputs"]: Dict[str, List[str]] = {}
        attrs["_method_outputs"]: Dict[str, List[str]] = {}
        attrs["_method_types"]: Dict[str, ExaMethodOutputType] = {}
        for attr_name, attr in attrs.items():
            # Handle exported methods.
            if isinstance(attr, ExportDecoratorBase):
                sig = inspect.signature(attr)
                # Store the input names, ignoring self.
                attrs["_method_inputs"][attr_name] = list(sig.parameters.keys())[1:]
                # Check the return annotation.
                ret_ann = sig.return_annotation
                if ret_ann == inspect.Signature.empty:
                    if attr._outputs is None:
                        raise ValueError(
                            f"Method [{attr_name}] must have a return annotation or "
                            "outputs argument to export"
                        )
                    attrs["_method_types"][attr_name] = ExaMethodOutputType.VALUE_DICT
                    continue
                # Store the output types and value names.
                if is_typeddict(ret_ann):
                    attrs["_method_outputs"][attr_name] = list(
                        ret_ann.__annotations__.keys()
                    )
                    attrs["_method_types"][attr_name] = ExaMethodOutputType.VALUE_DICT
                # tuple for 3.7+, Tuple for 3.6.
                elif getattr(ret_ann, "__origin__", None) in (tuple, Tuple):
                    if any(arg == Ellipsis for arg in ret_ann.__args__):
                        raise ValueError(
                            f"Method [{attr_name}] cannot have a tuple return type "
                            "with ellipsis"
                        )
                    attrs["_method_outputs"][attr_name] = list(
                        f"_tuple_value_{i}" for i in range(len(ret_ann.__args__))
                    )
                    attrs["_method_types"][attr_name] = ExaMethodOutputType.VALUE_TUPLE
                else:
                    attrs["_method_outputs"][attr_name] = ["_value"]
                    attrs["_method_types"][attr_name] = ExaMethodOutputType.VALUE

        return super().__new__(cls, name, bases, attrs)


class AutoModule(AutoModuleBase, BaseModule, metaclass=AutoModuleMeta):
    """Base class for Exafunction PyModules with convenience API."""

    # pylint: disable=no-member
    def _run_method(
        self,
        ctx: MethodContext,
        method_name: str,
        inputs: Dict[str, _C.Value],
    ) -> Dict[str, _C.Value]:
        m = getattr(self, method_name)
        py_inputs = {k: Value(v).get() for k, v in inputs.items()}
        py_outputs = wrap_call(m, **py_inputs)
        # Convert the outputs to correct type.
        if (
            getattr(self, "_method_types")[method_name]
            == ExaMethodOutputType.VALUE_DICT
        ):
            # pylint: disable=protected-access
            return {k: ctx.convert_to_value(v)._c for k, v in py_outputs.items()}
        if (
            getattr(self, "_method_types")[method_name]
            == ExaMethodOutputType.VALUE_TUPLE
        ):
            # pylint: disable=protected-access
            return {
                k: ctx.convert_to_value(v)._c
                for k, v in zip(
                    getattr(self, "_method_outputs")[method_name], py_outputs
                )
            }
        # pylint: disable=protected-access
        return {
            getattr(self, "_method_outputs")[method_name][0]: ctx.convert_to_value(
                py_outputs
            )._c
        }


def _export(
    inputs: Optional[Sequence[str]] = None, outputs: Optional[Sequence[str]] = None
):
    class ExportDecorator(ExportDecoratorBase):
        def __init__(self, fn):
            self._fn = fn
            self._inst = None
            self._outputs = outputs
            # Update ExportDecorator to look like fn.
            functools.update_wrapper(self, fn)

        def __set_name__(self, owner, name):
            _inputs = inputs or getattr(owner, "_method_inputs", {}).get(name, [])
            _outputs = outputs or getattr(owner, "_method_outputs", {}).get(name, [])
            if not hasattr(owner, "_methods"):
                owner._methods = {}
            if name in owner._methods:
                raise ValueError(f"Already registered method {name} for export")
            owner._methods[name] = (tuple(_inputs), tuple(_outputs))

        def __call__(self, *args, **kwargs):
            # Define __call__ so that the decorated function is callable.
            if self._inst is None:
                raise ValueError("Cannot call unbound method.")
            return self._fn(self._inst, *args, **kwargs)

        def __get__(self, instance, _):
            # Use __get__ to pass the instance to the decorated function.
            self._inst = instance
            return self

    return ExportDecorator


def export(
    fn: Optional[Callable[..., Any]] = None,
    *,
    inputs: Optional[Sequence[str]] = None,
    outputs: Optional[Sequence[str]] = None,
):
    """Decorator to export a method, enabling it to be run remotely.

    This function can be used in two ways:
    - As a decorator directly which requires the decorated function to have an explicit
        return type annotation of type TypedDict
    - As a function that returns a decorator, allowing the user to specify the input
        and output value names of the decorated function explicitly.
    """
    if fn is not None:
        return _export()(fn)
    return _export(inputs, outputs)
