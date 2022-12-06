from __future__ import annotations

from typing import TYPE_CHECKING, Union

import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb

from ..utils import Utils
from .feature_ref import FeatureRef

if TYPE_CHECKING:  # Only imports the below statements during type checking
    from .feature import Feature


class TransformationFunctionMetadata:
    def __init__(self, transformation_function_proto: pb.TransformationFunction):
        self._transformation_function = transformation_function_proto

    @property
    def function_name(self):
        return self._transformation_function.function_name

    @property
    def supported_input_types(self):
        return self._transformation_function.supported_input_types

    @property
    def output_type(self):
        return self._transformation_function.output_type

    def apply(self, feature: Union[Feature, FeatureRef]):
        return TransformationFunction(self.function_name).apply(feature)

    def __repr__(self):
        return Utils.pretty_print_proto(self._transformation_function)


class TransformationFunction:
    def __init__(self, function_name: str):
        self._function_name = function_name

    @property
    def function_name(self):
        return self._function_name

    def apply(self, feature: Union[Feature, FeatureRef]):
        return TransformedFeature(self, feature)

    def __repr__(self):
        return self._function_name


class TransformedFeature:
    def __init__(
        self,
        transformation: TransformationFunction,
        feature: Union[Feature, FeatureRef],
    ):
        self.transformation = transformation
        self.feature = feature if isinstance(feature, FeatureRef) else feature._reference()
