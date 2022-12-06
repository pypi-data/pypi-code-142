import ai.h2o.featurestore.api.v1.CoreService_pb2 as pb
import ai.h2o.featurestore.api.v1.FeatureSetProtoApi_pb2 as FeatureSetApi

from ..utils import Utils


class MLDatasetFeature:
    def __init__(self, internal_feature: pb.MLDatasetFeature):
        self._internal_feature = internal_feature

    @property
    def name(self):
        return self._internal_feature.name

    @property
    def feature_type(self):
        return FeatureSetApi.FeatureType.Name(self._internal_feature.feature_type)

    @property
    def data_type(self):
        return self._internal_feature.data_type

    @property
    def is_primary_key(self):
        return self._internal_feature.is_primary_key

    def __repr__(self):
        return Utils.pretty_print_proto(self._internal_feature)
