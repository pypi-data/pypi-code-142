import warnings

from .kernels import (
    handlers as kernels_handlers,
    websocket as kernels_websocket,
)
from .kernels.connection.channels import ZMQChannelsWebsocketConnection
from .kernels.connection.base import BaseKernelWebsocketConnection
from .kernels.kernelmanager import AsyncMappingKernelManager, MappingKernelManager
from .kernelspecs import handlers as kernelspecs_handlers
from .gateway import handlers as gateway_handlers
from .sessions import handlers as sessions_handlers
from .sessions.sessionmanager import SessionManager

from jupyter_server.extension.application import ExtensionApp
from jupyter_server.transutils import _i18n
from traitlets import Bool, Float, Type, Unicode, default, observe


class KernelsExtensionApp(ExtensionApp):

    name = "jupyter_server_kernels"

    kernel_websocket_connection_class = Type(
        default_value=ZMQChannelsWebsocketConnection,
        klass=BaseKernelWebsocketConnection,
        config=True,
        help=_i18n("The kernel websocket connection class to use."),
    )

    kernel_ws_protocol = Unicode(
        allow_none=True,
        config=True,
        help=_i18n("DEPRECATED. Use ZMQChannelsWebsocketConnection.kernel_ws_protocol"),
    )

    kernel_manager_class = Type(
        klass=AsyncMappingKernelManager,
        config=True,
        help=_i18n("The kernel manager class to use."),
    )

    @default("kernel_manager_class")
    def _default_kernel_manager_class(self):
        #if self.gateway_config.gateway_enabled:
        #    return "jupyter_server.gateway.managers.GatewayMappingKernelManager"
        return AsyncMappingKernelManager

    @observe("kernel_ws_protocol")
    def _deprecated_kernel_ws_protocol(self, change):
        self._warn_deprecated_config(change, "ZMQChannelsWebsocketConnection")

    limit_rate = Bool(
        allow_none=True,
        config=True,
        help=_i18n("DEPRECATED. Use ZMQChannelsWebsocketConnection.limit_rate"),
    )

    @observe("limit_rate")
    def _deprecated_limit_rate(self, change):
        self._warn_deprecated_config(change, "ZMQChannelsWebsocketConnection")

    iopub_msg_rate_limit = Float(
        allow_none=True,
        config=True,
        help=_i18n("DEPRECATED. Use ZMQChannelsWebsocketConnection.iopub_msg_rate_limit"),
    )

    @observe("iopub_msg_rate_limit")
    def _deprecated_iopub_msg_rate_limit(self, change):
        self._warn_deprecated_config(change, "ZMQChannelsWebsocketConnection")

    iopub_data_rate_limit = Float(
        allow_none=True,
        config=True,
        help=_i18n("DEPRECATED. Use ZMQChannelsWebsocketConnection.iopub_data_rate_limit"),
    )

    @observe("iopub_data_rate_limit")
    def _deprecated_iopub_data_rate_limit(self, change):
        self._warn_deprecated_config(change, "ZMQChannelsWebsocketConnection")

    rate_limit_window = Float(
        allow_none=True,
        config=True,
        help=_i18n("DEPRECATED. Use ZMQChannelsWebsocketConnection.rate_limit_window"),
    )

    @observe("rate_limit_window")
    def _deprecated_rate_limit_window(self, change):
        self._warn_deprecated_config(change, "ZMQChannelsWebsocketConnection")

    session_manager_class = Type(
        config=True,
        help=_i18n("The session manager class to use."),
    )

    @default("session_manager_class")
    def _default_session_manager_class(self):
        # if self.gateway_config.gateway_enabled:
        #    return "jupyter_server.gateway.managers.GatewaySessionManager"
        return SessionManager

    kernels_available = False

    def initialize_settings(self):
        self.initialize_configurables()

        kernel_manager = self.kernel_manager_class(
                parent=self.serverapp,
                log=self.settings["log"],
                connection_dir=self.serverapp.runtime_dir,
                kernel_spec_manager=self.serverapp.kernel_spec_manager,
        )

        self.settings.update(dict(
            kernels_available=True,
            kernel_manager=kernel_manager,
            kernel_manager_class=self.kernel_manager_class,
            kernel_websocket_connection_class=self.kernel_websocket_connection_class,
            kernel_ws_protocol=self.kernel_ws_protocol,
            limit_rate=self.limit_rate,
            iopub_msg_rate_limit=self.iopub_msg_rate_limit,
            iopub_data_rate_limit=self.iopub_data_rate_limit,
            rate_limit_window=self.rate_limit_window,
            session_manager_class=self.session_manager_class,
        ))

    def initialize_configurables(self):
        self.serverapp.kernel_manager_class = self.kernel_manager_class
        if not issubclass(self.kernel_manager_class, AsyncMappingKernelManager):
            warnings.warn(
                "The synchronous MappingKernelManager class is deprecated and will not be supported in Jupyter Server 3.0",
                DeprecationWarning,
                stacklevel=2,
            )

    def initialize_handlers(self):
        self.handlers.extend(kernels_websocket.default_handlers)
        self.handlers.extend(kernels_handlers.default_handlers)
        self.handlers.extend(kernelspecs_handlers.default_handlers)
        self.handlers.extend(sessions_handlers.default_handlers)
        # TODO: gateway
        self.serverapp.web_app.settings["kernels_available"] = self.settings[
            "kernels_available"
        ]
