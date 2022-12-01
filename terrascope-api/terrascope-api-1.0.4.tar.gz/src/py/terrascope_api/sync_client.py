# Copyright 2017-2021 Orbital Insight Inc., all rights reserved.
# Contains confidential and trade secret information.
# Government Users:  Commercial Computer Software - Use governed by
# terms of Orbital Insight commercial license agreement.


# TODO:
# add retry
# handle exceptions
# add custom logic (request_id, ....)

import grpc

from terrascope_api import models
from terrascope_api.stubs import system_pb2_grpc as system_pb2_grpc
from terrascope_api.stubs import aoi_pb2_grpc as aoi_pb2_grpc
from terrascope_api.stubs import aoi_collection_pb2_grpc as aoi_collection_pb2_grpc
from terrascope_api.stubs import aoi_version_pb2_grpc as aoi_version_pb2_grpc
from terrascope_api.stubs import aoi_transaction_pb2_grpc as aoi_transaction_pb2_grpc
from terrascope_api.stubs import algorithm_computation_pb2_grpc as algorithm_computation_pb2_grpc
from terrascope_api.stubs import visualization_pb2_grpc as visualization_pb2_grpc
from terrascope_api.stubs import user_pb2_grpc as user_pb2_grpc
from terrascope_api.stubs import user_collection_pb2_grpc as user_collection_pb2_grpc
from terrascope_api.stubs import token_pb2_grpc as token_pb2_grpc
from terrascope_api.stubs import permission_pb2_grpc as permission_pb2_grpc
from terrascope_api.stubs import algorithm_pb2_grpc as algorithm_pb2_grpc
from terrascope_api.stubs import algorithm_version_pb2_grpc as algorithm_version_pb2_grpc
from terrascope_api.stubs import algorithm_config_pb2_grpc as algorithm_config_pb2_grpc
from terrascope_api.stubs import analysis_pb2_grpc as analysis_pb2_grpc
from terrascope_api.stubs import analysis_version_pb2_grpc as analysis_version_pb2_grpc
from terrascope_api.stubs import analysis_config_pb2_grpc as analysis_config_pb2_grpc
from terrascope_api.stubs import analysis_computation_pb2_grpc as analysis_computation_pb2_grpc
from terrascope_api.stubs import toi_pb2_grpc as toi_pb2_grpc
from terrascope_api.stubs import result_pb2_grpc as result_pb2_grpc
from terrascope_api.stubs import data_source_pb2_grpc as data_source_pb2_grpc
from terrascope_api.stubs import data_type_pb2_grpc as data_type_pb2_grpc
from terrascope_api.stubs import credit_pb2_grpc as credit_pb2_grpc


# todo bring up  to date with async client or drop

class TerrascopeSyncClient:
    def __init__(self, oi_papi_url, port=80, secure=False):
        self.api = TerrascopeSyncApi(oi_papi_url, port, secure)
        self.models = models


class TerrascopeSyncApi:
    def __init__(self, oi_papi_url, port=80, secure=False):
        self._oi_papi_url = oi_papi_url
        self._port = port
        self._channel = self._get_secure_channel() if secure else self._get_insecure_channel()
        self.system = system_pb2_grpc.SystemApiStub(self._channel)
        self.aoi = aoi_pb2_grpc.AOIApiStub(self._channel)
        self.aoi_collection = aoi_collection_pb2_grpc.AOICollectionApiStub(self._channel)
        self.aoi_version = aoi_version_pb2_grpc.AOIVersionApiStub(self._channel)
        self.aoi_transaction = aoi_transaction_pb2_grpc.AOITransactionApiStub(self._channel)
        self.computation = algorithm_computation_pb2_grpc.AlgorithmComputationApiStub(self._channel)
        self.visualization = visualization_pb2_grpc.VisualizationApiStub(self._channel)
        self.permission = permission_pb2_grpc.PermissionApiStub(self._channel)
        self.user = user_pb2_grpc.UserApiStub(self._channel)
        self.user_collection = user_collection_pb2_grpc.UserCollectionApiStub(self._channel)
        self.token = token_pb2_grpc.TokenApiStub(self._channel)
        self.algorithm = algorithm_pb2_grpc.AlgorithmApiStub(self._channel)
        self.algorithm_version = algorithm_version_pb2_grpc.AlgorithmVersionApiStub(self._channel)
        self.algorithm_config = algorithm_config_pb2_grpc.AlgorithmConfigApiStub(self._channel)
        self.analysis = analysis_pb2_grpc.AnalysisApiStub(self._channel)
        self.analysis_version = analysis_version_pb2_grpc.AnalysisVersionApiStub(self._channel)
        self.toi = toi_pb2_grpc.TOIApiStub(self._channel)
        self.result = result_pb2_grpc.ResultApiStub(self._channel)
        self.credit = credit_pb2_grpc.CreditApiStub(self._channel)
        self.analysis_config = analysis_config_pb2_grpc.AnalysisConfigApiStub(self._channel)
        self.analysis_computation = analysis_computation_pb2_grpc.AnalysisComputationApiStub(self._channel)
        self.data_source = data_source_pb2_grpc.DataSourceAPIStub(self._channel)
        self.data_type = data_type_pb2_grpc.DataTypeAPIStub(self._channel)

    def _get_insecure_channel(self):
        return grpc.insecure_channel(f"{self._oi_papi_url}:{self._port}",
                                     options=[('grpc.max_send_message_length', -1),
                                              ('grpc.max_receive_message_length', -1)]
                                     )

    def _get_secure_channel(self):
        creds = grpc.ssl_channel_credentials(root_certificates=None, private_key=None, certificate_chain=None)
        return grpc.secure_channel(f"{self._oi_papi_url}:{self._port}", creds, compression=None,
                                   options=[('grpc.max_send_message_length', -1),
                                            ('grpc.max_receive_message_length', -1)])

    def __del__(self):
        self._channel.close()
