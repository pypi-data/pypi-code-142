import typing

from zorge.di.container import DependencyContainer
from zorge import contracts as zorge_contracts
from ..definitions import contracts
from ..identity.factory import UUIDIdentifierFactory
from ..interaction.factory import InteractionFactory
from ..interaction.registration import EventRegistrator


class DependencyRegistry:
    def __init__(
        self,
        dc: zorge_contracts.DependencyContainer | None = None,
        identifier_factory: contracts.IdentifierFactory = UUIDIdentifierFactory,
        interaction_factory: contracts.InteractionFactory = InteractionFactory,
    ):
        self._dc = dc or DependencyContainer()
        self._dc.register_contractual_dependency(
            instance=identifier_factory,
            contract=contracts.IdentifierFactory
        )
        self._dc.register_contractual_dependency(
            instance=interaction_factory,
            contract=contracts.InteractionFactory
        )

    def register_event_registrator(
        self,
        data_vendor: type[contracts.DataVendor],
        instance: zorge_contracts.DependencyBindingInstance = EventRegistrator,
        frame_name: contracts.EventRegistratorFrameName = 'events'
    ):
        self._dc.register_global_singleton(
            instance=frame_name,
            contract=contracts.EventRegistratorFrameName
        )
        self._dc.register_contractual_dependency(
            instance=instance,
            contract=contracts.EventRegistrator
        )
        self.register_data_vendor(
            instance=data_vendor,
            contract=contracts.EventRegistratorDataVendor
        )

    def register_connection_context(
        self,
        open_callback: typing.Callable,
        close_success_callback: typing.Callable,
        close_failure_callback: typing.Callable,
        contract: zorge_contracts.DependencyBindingContract
    ):
        self._dc.register_instance_singleton(
            instance=open_callback,
            contract=contract,
        )
        self._dc.register_shutdown_callback(
            success_callback=close_success_callback,
            failure_callback=close_failure_callback,
            contract=contract,
        )

    def register_registry(
        self,
        instance: zorge_contracts.DependencyBindingInstance,
        contract: zorge_contracts.DependencyBindingContract
    ):
        self._dc.register_global_singleton(
            instance=instance,
            contract=contract
        )

    def register_data_vendor(
        self,
        instance: zorge_contracts.DependencyBindingInstance,
        contract: zorge_contracts.DependencyBindingContract
    ):
        self._dc.register_contractual_dependency(
            instance=instance,
            contract=contract
        )

    def register_message_context(
        self,
        instance: zorge_contracts.DependencyBindingInstance,
        contract: zorge_contracts.DependencyBindingContract
    ):
        self._dc.register_contractual_dependency(
            instance=instance,
            contract=contract
        )

    def register_repository(
        self,
        instance: zorge_contracts.DependencyBindingInstance,
        scope: typing.Literal['instance', 'global'] = 'instance'
    ):
        _map = {
            'instance': zorge_contracts.DependencyBindingScope.INSTANCE,
            'global': zorge_contracts.DependencyBindingScope.GLOBAL
        }
        self._dc.register_selfish_dependency(
            instance=instance,
            singleton_scope=_map[scope]
        )

    def register_view(
        self,
        instance: zorge_contracts.DependencyBindingInstance,
        contract: zorge_contracts.DependencyBindingContract | None = None,
        scope: typing.Literal['instance', 'global'] = 'instance'
    ):
        if not contract:
            self._dc.register_selfish_dependency(
                instance=instance,
                singleton_scope={
                    'instance': zorge_contracts.DependencyBindingScope.INSTANCE,
                    'global': zorge_contracts.DependencyBindingScope.GLOBAL
                }[scope]
            )
        else:
            {
                'instance': self._dc.register_global_singleton,
                'global': self._dc.register_global_singleton
            }[scope](
                instance=instance,
                contract=contract
            )

    def get_container(self) -> DependencyContainer:
        return self._dc
