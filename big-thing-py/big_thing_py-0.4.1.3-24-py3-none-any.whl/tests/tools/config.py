from big_thing_py.tests.tools.utils import *


class SoPConfig(metaclass=ABCMeta):
    def __init__(self, data: dict) -> None:
        return self.load(data)

    @abstractmethod
    def load(self, data: dict):
        pass


class SoPDeviceConfig(SoPConfig):

    class DeviceInfo(SoPConfig):
        def __init__(self, data: dict) -> None:
            super().__init__(data)

            self.name: str
            self.host: str
            self.ssh_port: int
            self.user: str
            self.password: str

        def load(self, data: dict):
            self.name = data['name']
            self.host = data['host']
            self.ssh_port = data['ssh_port']
            self.user = data['user']
            self.password = data['password']

    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def load(self, data: dict):
        for device_name, device_info in data['device_list'].items():
            device_info['name'] = device_name
            if not hasattr(self, 'device_list'):
                self.device_list = []
            self.device_list.append(SoPDeviceConfig.DeviceInfo(device_info))


class SoPMiddlewareConfig(SoPConfig):

    class DetailConfig(SoPConfig):
        def __init__(self, data: dict) -> None:
            super().__init__(data)

            self.thing_per_middleware: Tuple[int, int]
            self.scenario_per_middleware: Tuple[int, int]

        def load(self, data: dict):
            self.thing_per_middleware = data['thing_per_middleware']
            self.scenario_per_middleware = data['scenario_per_middleware']

    def __init__(self, data: dict, config_path: str = '') -> None:
        super().__init__(data)

        self.config_path = config_path

        self.height: int
        self.child_per_node: Tuple[int, int]
        self.middleware_config_path: str
        self.remote_middleware_path: str
        self.remote_middleware_config_path: str

        self.middleware_tree: dict

        self.base: SoPMiddlewareConfig.DetailConfig
        self.super: SoPMiddlewareConfig.DetailConfig

    def load(self, data: dict):
        self.height = data['height']
        self.child_per_node = data['child_per_node']
        self.middleware_config_path = data['middleware_config_path']
        self.remote_middleware_path = data['remote_middleware_path']
        self.remote_middleware_config_path = data['remote_middleware_config_path']

        self.middleware_tree = data['middleware_tree']

        self.base = SoPMiddlewareConfig.DetailConfig(data['base'])
        self.super = SoPMiddlewareConfig.DetailConfig(data['super'])


class SoPServiceConfig(SoPConfig):

    class DetailConfig(SoPConfig):
        def __init__(self, data: dict) -> None:
            super().__init__(data)

            self.service_type_num: int
            self.energy: Tuple[float, float]
            self.execute_time: Tuple[float, float]
            self.execute_time_margin: float

        def load(self, data: dict):
            self.service_type_num = data['service_type_num']
            self.energy = data['energy']
            self.execute_time = data['execute_time']
            self.execute_time_margin: float = data['execute_time_margin']

    def __init__(self, data: dict) -> None:
        super().__init__(data)

        self.tag_type_num: int
        self.tag_per_service: Tuple[int, int]
        self.subfunction_per_super_service: Tuple[int, int]

        self.base: SoPServiceConfig.DetailConfig
        self.super: SoPServiceConfig.DetailConfig

    def load(self, data: dict):
        self.tag_type_num = data['tag_type_num']
        self.tag_per_service = data['tag_per_service']
        self.subfunction_per_super_service = data['subfunction_per_super_service']

        self.base = SoPServiceConfig.DetailConfig(data['base'])
        self.super = SoPServiceConfig.DetailConfig(data['super'])


class SoPThingConfig(SoPConfig):

    class DetailConfig(SoPConfig):
        def __init__(self, data: dict) -> None:
            super().__init__(data)

            self.thing_folder_path: str
            self.remote_thing_folder_path: str
            self.service_per_thing: Tuple[int, int]
            self.error_rate: float

        def load(self, data: dict):
            self.thing_folder_path = data['thing_folder_path']
            self.remote_thing_folder_path = data['remote_thing_folder_path']
            self.service_per_thing = data['service_per_thing']
            self.error_rate = data['error_rate']

    def __init__(self, data: dict, config_path: str = '') -> None:
        super().__init__(data)

        self.config_path = config_path

        self.base: SoPThingConfig.DetailConfig
        self.super: SoPThingConfig.DetailConfig

    def load(self, data: dict):
        self.base = SoPThingConfig.DetailConfig(data['base'])
        self.super = SoPThingConfig.DetailConfig(data['super'])


class SoPScenarioConfig(SoPConfig):

    class DetailConfig(SoPConfig):
        def __init__(self, data: dict) -> None:
            super().__init__(data)

            self.service_per_scenario: Tuple[int, int]
            self.period_overhead: Tuple[float, float]

        def load(self, data: dict):
            self.service_per_scenario = data['service_per_scenario']
            self.period_overhead = data['period_overhead']

    def __init__(self, data: dict, config_path: str = '') -> None:
        super().__init__(data)

        self.config_path = config_path

        self.base: SoPScenarioConfig.DetailConfig
        self.super: SoPScenarioConfig.DetailConfig

    def load(self, data: dict):
        self.base = SoPScenarioConfig.DetailConfig(data['base'])
        self.super = SoPScenarioConfig.DetailConfig(data['super'])
