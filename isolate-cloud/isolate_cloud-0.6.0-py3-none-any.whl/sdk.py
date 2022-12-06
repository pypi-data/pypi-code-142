from __future__ import annotations

from dataclasses import dataclass
import pkgutil
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
)
from grpc import ChannelCredentials
import grpc

from isolate.backends import (
    BasicCallable,
)

from isolate.backends.settings import IsolateSettings
from isolate.server.definitions import (
    EnvironmentDefinition,
)
from isolate.backends.common import sha256_digest_of
from isolate.server import interface

from isolate_cloud.definitions import *
from isolate.interface import RemoteBox, BoxedEnvironment
from isolate.backends.remote import IsolateServer, IsolateServerConnection
import isolate_cloud.auth as auth

from isolate_controller import flags

@dataclass
class HostedRemoteBox(RemoteBox):
    """Run on an hosted isolate server."""
    creds: Optional[ChannelCredentials] = None 

    def wrap(
        self,
        definition: Dict[str, Any],
        settings: IsolateSettings,
    ) -> BoxedEnvironment:
        definition = definition.copy()

        # Extract the kind of environment to use.
        kind = definition.pop("kind", None)
        assert kind is not None, f"Corrupted definition: {definition}"

        target_list = [{"kind": kind, "configuration": definition}]

        # Create a remote environment.
        return BoxedEnvironment(
            FalHostedServer(host=self.host, target_environments=target_list,  creds=self.creds)
        )


@dataclass
class FalHostedServer(IsolateServer):
    BACKEND_NAME: ClassVar[str] = "hosted-isolate-server"
    creds: Optional[ChannelCredentials] = None 

    def open_connection(
        self,
        connection_key: List[EnvironmentDefinition],
    ) -> FalHostedServerConnection:
        return FalHostedServerConnection(self, self.host, connection_key, creds=self.creds)


@dataclass
class FalHostedServerConnection(IsolateServerConnection):
    creds: Optional[ChannelCredentials] = None 
    
    def _acquire_channel(self, channel_creds) -> None:
        TOKEN_KEY = "auth-token"

        root_cert = pkgutil.get_data(__name__, "ca.pem")

        class GrpcAuth(grpc.AuthMetadataPlugin):
            def __init__(self, key):
                self._key = key

            def __call__(
                self,
                context: grpc.AuthMetadataContext,
                callback: grpc.AuthMetadataPluginCallback,
            ):
                # Add token to metadata before sending
                callback(((TOKEN_KEY, self._key),), None)

        if flags.TEST_MODE:
            channel_creds = grpc.local_channel_credentials()
        else:                
            channel_creds = grpc.composite_channel_credentials(
                # Channel credentials
                grpc.ssl_channel_credentials(root_cert),
                # User credentials
                # TODO: "access_key" for now, replace with user tokens later
                grpc.metadata_call_credentials(GrpcAuth(auth.USER.access_token)),
            )

        options = (("grpc.ssl_target_name_override", "localhost"),)
        self._channel = grpc.secure_channel(self.host, channel_creds, options)


    def run(
        self,
        executable: BasicCallable,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self._acquire_channel(self.creds)
        isolate_controller = IsolateControllerStub(self._channel)

        request = HostedRun(
            environments=self.definitions,
            function=interface.to_serialized_object(
                executable,
                method="dill",
                was_it_raised=False,
            ),
        )
        
        return_value = []
        for result in isolate_controller.Run(request):
            for raw_log in result.logs:
                log = interface.from_grpc(raw_log)
                self.log(log.message, level=log.level, source=log.source)
            if result.return_value.definition:
                return_value.append(interface.from_grpc(result.return_value))
        return return_value[0]
