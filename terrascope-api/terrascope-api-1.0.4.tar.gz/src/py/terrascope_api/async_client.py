# Copyright 2017-2021 Orbital Insight Inc., all rights reserved.
# Contains confidential and trade secret information.
# Government Users:  Commercial Computer Software - Use governed by
# terms of Orbital Insight commercial license agreement.


# TODO: figure out reuse sync client. async and sync client almost same
import os

import grpc
import json
from terrascope_api import models
from terrascope_api import stubs
from terrascope_api.async_interceptors import (
    ContextInjectorUnaryUnary, ContextInjectorStreamUnary, ContextInjectorUnaryStream, ContextInjectorStreamStream
)

API_TOKEN = 'TERRASCOPE_API_TOKEN'


class TerrascopeAsyncClient:
    def __init__(self, oi_papi_url, port=443, secure=True, api_token=None):
        self.api = TerrascopeAsyncApi(oi_papi_url, port, secure, api_token=api_token)
        self.models = models


class TerrascopeAsyncApi:
    def __init__(self, oi_papi_url, port=443, secure=True, api_token=None):
        self._oi_papi_url = oi_papi_url
        self._port = port
        if api_token is None:
            api_token = os.environ.get(API_TOKEN)
            if api_token is None:
                homedir = os.environ.get('HOME', '/')
                token_filename = f'{homedir}/.orbital/api_token'
                try:
                    with open(token_filename) as fd:
                        api_token = fd.read()
                except FileNotFoundError:
                    pass
        if api_token is not None:
            api_token = api_token.strip()
        self.api_token = api_token
        if not secure and api_token is not None:
            raise ValueError('API token cannot be passed over an unsecure connection')
            # grpc will not transmit the Authorization header over an unsecured channel, which
            #  makes sense since it would be easy to hijack
        self.context_injecting_interceptors = [
            # materialize distributed context from request headers
            ContextInjectorUnaryUnary(), ContextInjectorUnaryStream(),
            ContextInjectorStreamUnary(), ContextInjectorStreamStream()
        ]
        self.options = [('grpc.max_send_message_length', -1),
                        ('grpc.max_receive_message_length', -1)]
        service_config_json = json.dumps({
            "methodConfig": [{
                "name": [{}],  # Apply retry to all methods by using [{}]
                "retryPolicy": {
                    "maxAttempts": 5,
                    "initialBackoff": "1.0s",
                    "maxBackoff": "60s",
                    "backoffMultiplier": 2,
                    "retryableStatusCodes": ["UNAVAILABLE"],
                },
            }]
        })
        self.options.append(("grpc.service_config", service_config_json))
        self._channel = self._get_secure_channel() if secure else self._get_insecure_channel()
        self.algorithm = stubs.algorithm.AlgorithmApiStub(self._channel)
        self.algorithm_version = stubs.algorithm_version.AlgorithmVersionApiStub(self._channel)
        self.algorithm_config = stubs.algorithm_config.AlgorithmConfigApiStub(self._channel)
        self.aoi = stubs.aoi.AOIApiStub(self._channel)
        self.aoi_collection = stubs.aoi_collection.AOICollectionApiStub(self._channel)
        self.aoi_version = stubs.aoi_version.AOIVersionApiStub(self._channel)
        self.aoi_transaction = stubs.aoi_transaction.AOITransactionApiStub(self._channel)
        self.algorithm_computation = stubs.algorithm_computation.AlgorithmComputationApiStub(self._channel)
        self.analysis = stubs.analysis.AnalysisApiStub(self._channel)
        self.analysis_version = stubs.analysis_version.AnalysisVersionApiStub(self._channel)
        self.credit = stubs.credit.CreditApiStub(self._channel)
        self.result = stubs.result.ResultApiStub(self._channel)
        self.analysis_config = stubs.analysis_config.AnalysisConfigApiStub(self._channel)
        self.analysis_computation = stubs.analysis_computation.AnalysisComputationApiStub(self._channel)
        self.system = stubs.system.SystemApiStub(self._channel)
        self.toi = stubs.toi.TOIApiStub(self._channel)
        self.permission = stubs.permission.PermissionApiStub(self._channel)
        self.user = stubs.user.UserApiStub(self._channel)
        self.user_collection = stubs.user_collection.UserCollectionApiStub(self._channel)
        self.token = stubs.token.TokenApiStub(self._channel)
        self.visualization = stubs.visualization.VisualizationApiStub(self._channel)

        self.data_source = stubs.data_source.DataSourceAPIStub(self._channel)
        self.data_type = stubs.data_type.DataTypeAPIStub(self._channel)

    def _get_insecure_channel(self):
        return grpc.aio.insecure_channel(f"{self._oi_papi_url}:{self._port}",
                                         options=self.options,
                                         interceptors=self.context_injecting_interceptors)

    def _get_secure_channel(self):
        ssl_creds = grpc.ssl_channel_credentials(root_certificates=None, private_key=None, certificate_chain=None)
        # note: with all defaults, gRPC will search for cert as described here:
        #  https://github.com/grpc/grpc/blob/7a63bd5407d5e14b30f19a5aaf4b6cd1b80f00e1/include/grpc/grpc_security.h#L287
        if self.api_token is not None:
            token_creds = grpc.access_token_call_credentials(self.api_token)
            creds = grpc.composite_channel_credentials(ssl_creds, token_creds)
        else:
            creds = ssl_creds
        return grpc.aio.secure_channel(f"{self._oi_papi_url}:{self._port}",
                                       creds,
                                       options=self.options,
                                       compression=None,
                                       interceptors=self.context_injecting_interceptors)

    # TODO: async destructor
    def __adel__(self):
        self._channel.close()
