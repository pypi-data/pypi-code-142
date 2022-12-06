from __future__ import annotations

from dataclasses import dataclass
from collections import namedtuple
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

from isolate_cloud import flags

MACHINE_TYPES = ["XS", "S", "M", "GPU"]

CloudKeyCredentials = namedtuple("CloudKeyCredentials", ['key', 'key_id'])


@dataclass
class HostedRemoteBox(RemoteBox):
    """Run on an hosted isolate server."""
    machine_type: str = "S"
    auth_key: Optional[str] = None
    key_id: Optional[str] = None

    def __post_init__(self):
        if self.machine_type not in MACHINE_TYPES:
            raise RuntimeError(f"Machine type {self.machine_type} not supported. Use one of: {' '.join(MACHINE_TYPES)}")
        if self.auth_key and not self.key_id:
            raise RuntimeError("auth_key needs to be provided along with key_id")

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
            FalHostedServer(
                host=self.host,
                machine_type=self.machine_type,
                target_environments=target_list,
                creds=CloudKeyCredentials(self.auth_key, self.key_id))
        )


@dataclass
class FalHostedServer(IsolateServer):
    machine_type: str
    BACKEND_NAME: ClassVar[str] = "hosted-isolate-server"
    creds: Optional[CloudKeyCredentials] = None

    def open_connection(
        self,
        connection_key: List[EnvironmentDefinition],
    ) -> FalHostedServerConnection:
        return FalHostedServerConnection(self,
                                         self.host,
                                         connection_key,
                                         machine_type=self.machine_type,
                                         creds=self.creds)



@dataclass
class FalHostedServerConnection(IsolateServerConnection):
    machine_type: str = "S"
    creds: Optional[CloudKeyCredentials] = None

    def _acquire_channel(self) -> None:
        TOKEN_KEY = "auth-token"
        SECRET_KEY = "auth-key"
        SECRET_ID_KEY = "auth-key-id"

        root_cert = pkgutil.get_data(__name__, "ca.pem")

        class GrpcAuth(grpc.AuthMetadataPlugin):
            def __init__(self, key, value):
                self._key = key
                self._value = value

            def __call__(
                self,
                context: grpc.AuthMetadataContext,
                callback: grpc.AuthMetadataPluginCallback,
            ):
                # Add token to metadata before sending
                callback(((self._key, self._value),), None)

        if flags.TEST_MODE:
            channel_creds = grpc.local_channel_credentials()
        else:
            if self.creds and self.creds.key and self.creds.key_id:
                channel_creds = grpc.composite_channel_credentials(
                    grpc.ssl_channel_credentials(root_cert),
                    grpc.metadata_call_credentials(GrpcAuth(SECRET_KEY, self.creds.key)),
                    grpc.metadata_call_credentials(GrpcAuth(SECRET_ID_KEY, self.creds.key_id)),
                )
            else:
                channel_creds = grpc.composite_channel_credentials(
                    # Channel credentials
                    grpc.ssl_channel_credentials(root_cert),
                    # User credentials
                    # TODO: "access_key" for now, replace with user tokens later
                    grpc.metadata_call_credentials(GrpcAuth(TOKEN_KEY, auth.USER.access_token)),
                )

        options = (("grpc.ssl_target_name_override", "localhost"),)
        self._channel = grpc.secure_channel(self.host, channel_creds, options)


    def run(
        self,
        executable: BasicCallable,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self._acquire_channel()
        isolate_controller = IsolateControllerStub(self._channel)

        request = HostedRun(
            environments=self.definitions,
            machine_requirements=MachineRequirements(machine_type=self.machine_type),
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
