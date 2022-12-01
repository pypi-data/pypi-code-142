import typing
from zorge import contracts as zorge_contracts


class DependencyRegistry:
    def register_connection_context(
        self,
        open_callback: typing.Callable,
        close_callback: typing.Callable,
        contract: zorge_contracts.DependencyBindingContract
    ) -> typing.NoReturn: ...

    def register_data_vendor(
        self,
        instance: zorge_contracts.DependencyBindingInstance,
        contract: zorge_contracts.DependencyBindingContract
    ) -> typing.NoReturn: ...

    def register_repository(
        self,
        instance: zorge_contracts.DependencyBindingInstance,
        scope: typing.Literal['instance', 'global'] = 'instance'
    ) -> typing.NoReturn: ...

    def register_view(
        self,
        instance: zorge_contracts.DependencyBindingInstance,
        contract: zorge_contracts.DependencyBindingContract | None = None,
        scope: typing.Literal['instance', 'global'] = 'instance'
    ): ...

    def get_container(
        self
    ) -> zorge_contracts.DependencyContainer:
        ...
