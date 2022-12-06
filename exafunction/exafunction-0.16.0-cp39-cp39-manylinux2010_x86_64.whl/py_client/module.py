# Copyright Exafunction, Inc.
"""Defines the Module class."""

import inspect
import pickle
from typing import Callable, Dict, List, NamedTuple, Optional, Set, Tuple, Type

import numpy as np
from typing_extensions import is_typeddict  # type: ignore

from exa import _C
from exa.common_pb.common_pb2 import MethodInfo
from exa.common_pb.common_pb2 import ValueMetadata
from exa.py_value.value import Value
from exa.types import AutoModuleBase
from exa.types import BaseModuleBase
from exa.types import ExaMethodOutputType
from exa.types import ExportDecoratorBase
from exa.types import MethodOutput  # pylint: disable=unused-import
from exa.types import Picklable
from exa.types import ValueLike


class _MethodInfo(NamedTuple):
    """Information about a module method."""

    type: ExaMethodOutputType
    inputs: List[str]


class Module:
    """
    The Module class represents a remote module in the Exafunction system.

    Each remote module exposes one or more methods, which take in and return
    Exafunction values. Modules are created by Exafunction session, using the
    methods like Session.new_module.
    """

    def __init__(self, c: _C.Module, module_cls: Optional[Type[BaseModuleBase]] = None):
        self._c = c
        self._value_callback: Optional[Callable[[Value], None]] = None
        self._method_infos: Dict[str, _MethodInfo] = {}

        if module_cls is not None and issubclass(module_cls, AutoModuleBase):
            for attr_name, attr in module_cls.__dict__.items():
                # Handle exported methods.
                if not isinstance(attr, ExportDecoratorBase):
                    continue
                # Check for reserved name collision.
                if attr_name in self._reserved_attribute_names():
                    raise ValueError(f"Module method [{attr_name}] is reserved.")
                # Get the method signature.
                sig = inspect.signature(attr)
                # Get the method input names, ignoring self.
                method_inputs = []
                for parameter_name, parameter in tuple(sig.parameters.items())[1:]:
                    if parameter.default != inspect.Parameter.empty:
                        raise ValueError(
                            f"Invalid parameter [{parameter.name}] for exported method "
                            f"[{attr_name}]. Default values are not supported."
                        )
                    if parameter.kind != inspect.Parameter.POSITIONAL_OR_KEYWORD:
                        raise ValueError(
                            f"Invalid parameter [{parameter.name}] for exported method "
                            f"[{attr_name}]. All parameters must support both "
                            "positional and keyword arguments."
                        )
                    method_inputs.append(parameter_name)
                # Get the method output type.
                ret_ann = sig.return_annotation
                if ret_ann == inspect.Signature.empty or is_typeddict(ret_ann):
                    method_type = ExaMethodOutputType.VALUE_DICT
                # tuple for 3.7+, Tuple for 3.6.
                elif getattr(ret_ann, "__origin__", None) in (tuple, Tuple):
                    method_type = ExaMethodOutputType.VALUE_TUPLE
                else:
                    method_type = ExaMethodOutputType.VALUE
                self._method_infos[attr_name] = _MethodInfo(
                    type=method_type, inputs=method_inputs
                )

    def _reserved_attribute_names(self) -> Set[str]:
        """Get list of reserved names that cannot be used for methods."""
        return (set(Module.__dict__.keys()) | set(self.__dict__.keys())) - {"run"}

    def __getattr__(self, name: str):  # -> Callable[..., MethodOutput]:
        """
        Returns a method of the module.

        :param name: The name of the method.
        :return: A callable that can be used to invoke the method.
        """
        self._check_valid()

        if not name in self._method_infos:
            raise AttributeError(f"Module does not export method [{name}]")

        def method(
            *arg_inputs: ValueLike,
            raw_inputs: Optional[Dict[str, ValueLike]] = None,
            **inputs: ValueLike,
        ):  # -> MethodOutput:
            return self.run_method(name, *arg_inputs, raw_inputs=raw_inputs, **inputs)

        return method

    def _check_valid(self):
        if not self._c.is_valid():
            raise ValueError("Module is not valid (was the session closed?)")

    def module_id(self) -> int:
        """
        Returns the module id.

        :return: The module id.
        """
        self._check_valid()
        return self._c.module_id()

    def _convert_to_value(self, val: ValueLike) -> Value:
        if isinstance(val, Value):
            return val
        if isinstance(val, np.ndarray):
            return self._from_numpy(val)
        if isinstance(val, bytes):
            return self._from_bytes(val)
        try:
            return self._from_picklable(val)
        except pickle.PicklingError as e:
            raise ValueError(f"Cannot convert {type(val)} to Value") from e

    def _convert_output(
        self, method_name: str, output_dict: Dict[str, Value]
    ):  # -> MethodOutput:
        # pylint: disable=protected-access
        if (
            method_name not in self._method_infos
            or self._method_infos[method_name].type == ExaMethodOutputType.VALUE_DICT
        ):
            return output_dict
        # pylint: disable=protected-access
        if self._method_infos[method_name].type == ExaMethodOutputType.VALUE_TUPLE:
            return tuple(
                output_dict[f"_tuple_value_{i}"] for i in range(len(output_dict))
            )
        # pylint: disable=protected-access
        if self._method_infos[method_name].type == ExaMethodOutputType.VALUE:
            return output_dict["_value"]
        raise ValueError("Unknown method output type")

    def run_method(
        self,
        method_name: str,
        *arg_inputs: ValueLike,
        raw_inputs: Optional[Dict[str, ValueLike]] = None,
        **inputs: ValueLike,
    ):  # -> MethodOutput:
        """
        Runs a method on the remote module.

        :param method_name: The name of the method to run.
        :param arg_inputs: The inputs to the method as positional arguments.
        :param raw_inputs: A dictionary of inputs to the method. This can be used over
            `inputs` if an input name requires special characters, such as grouped
            inputs.
        :param inputs: The inputs to the method as keyword arguments.
        :return: The outputs of the method.
        """
        self._check_valid()
        input_names = (
            self._method_infos[method_name].inputs
            if method_name in self._method_infos
            else []
        )
        # pylint: disable=protected-access
        cc_inputs = {
            k: self._convert_to_value(inp)._c for k, inp in zip(input_names, arg_inputs)
        }
        for k, inp in inputs.items():
            if k in cc_inputs:
                raise ValueError(f"Duplicate input [{k}] for method [{method_name}]")
            # pylint: disable=protected-access
            cc_inputs[k] = self._convert_to_value(inp)._c
        if raw_inputs is None:
            raw_inputs = {}
        for k, inp in raw_inputs.items():
            if k in cc_inputs:
                raise ValueError(f"Duplicate input [{k}] for method [{method_name}]")
            # pylint: disable=protected-access
            cc_inputs[k] = self._convert_to_value(inp)._c
        cc_outputs = self._c.run_method(method_name, cc_inputs)
        ret_dict = {k: Value(out) for k, out in cc_outputs.items()}
        if self._value_callback is not None:
            for v in ret_dict.values():
                self._value_callback(v)  # pylint: disable=not-callable
        return self._convert_output(method_name, ret_dict)

    def run(
        self,
        *arg_inputs: ValueLike,
        raw_inputs: Optional[Dict[str, ValueLike]] = None,
        **inputs: ValueLike,
    ):  # -> MethodOutput:
        """
        Runs the module.

        :param arg_inputs: The inputs to the module as positional arguments.
        :param raw_inputs: A dictionary of inputs to the module. This can be used over
            `inputs` if an input name requires special characters, such as grouped
            inputs.
        :param inputs: The inputs to the module as keyword arguments.
        :return: The outputs of the module.
        """
        return self.run_method("run", *arg_inputs, raw_inputs=raw_inputs, **inputs)

    def ensure_local_valid(self, values: Dict[str, Value]):
        """
        Equivalent to calling ensure_local_valid on each value in the ValueMap
        to fetch its value. Using this function will generally reduce latency
        compared to fetching each value individually.

        :param values: The values to fetch.
        """

        self._check_valid()
        # pylint: disable=protected-access
        cc_values = {k: inp._c for k, inp in values.items()}
        self._c.ensure_local_valid(cc_values)

    def get_method_info(self, method_name: str = "run") -> MethodInfo:
        """
        Get information about a method, including its input and output types.

        If no method name is provided, the information for the "run" method
        is returned.

        :param method_name: The name of the method to get information about.
        :return: The method information.
        """
        self._check_valid()
        serialized_info = self._c.get_method_info(method_name)
        mi = MethodInfo()
        mi.ParseFromString(serialized_info)
        return mi

    def checkpoint(self):
        """
        Checkpoints the state of a stateful module locally. This allows the
        client and service to free up values required to recover the current
        state and also speeds up the recovery process. Checkpoints should not
        be taken too frequently if they are computationally expensive or have
        substantial network bandwidth overhead.
        """
        self._c.checkpoint()

    @property
    def id(self):
        """Returns the module ID.

        :return: The module ID.
        """
        return self._c.module_id

    def _allocate_value(self, metadata: ValueMetadata):
        ser_metadata = metadata.SerializeToString()
        val = Value(self._c.allocate_value(ser_metadata))
        return val

    def _from_bytes(self, val: bytes) -> Value:
        self._check_valid()
        metadata = ValueMetadata()
        metadata.size = len(val)
        metadata.bytes.SetInParent()
        v = self._allocate_value(metadata)
        v.set_bytes(val)
        if self._value_callback is not None:
            self._value_callback(v)  # pylint: disable=not-callable
        return v

    def _from_numpy(self, val: np.ndarray) -> Value:
        self._check_valid()
        # pylint: disable=protected-access
        metadata = Value._get_tensor_metadata(val.dtype, val.shape)
        v = self._allocate_value(metadata)
        v.numpy()[:] = val
        if self._value_callback is not None:
            self._value_callback(v)  # pylint: disable=not-callable
        return v

    def _from_picklable(self, val: Picklable) -> Value:
        self._check_valid()
        pickled_val = pickle.dumps(val)
        metadata = ValueMetadata()
        metadata.size = len(pickled_val)
        metadata.picklable.SetInParent()
        v = self._allocate_value(metadata)
        v.set_bytes(pickled_val)
        if self._value_callback is not None:
            self._value_callback(v)  # pylint: disable=not-callable
        return v
