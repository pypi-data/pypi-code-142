from big_thing_py.tests.tools.utils import *


class SoPEventType(Enum):
    UNDEFINED = 'undefined'

    DELAY = 'delay'
    END = 'end'

    MIDDLEWARE_RUN = 'middleware_run'
    MIDDLEWARE_KILL = 'middleware_kill'

    THING_RUN = 'thing_run'
    THING_KILL = 'thing_kill'
    THING_REGISTER = 'thing_register'
    THING_UNREGISTER = 'thing_unregister'

    THING_REGISTER_RESULT = 'thing_register_result'
    THING_UNREGISTER_RESULT = 'thing_unregister_result'

    FUNCTION_EXECUTE = 'function_execute'
    FUNCTION_EXECUTE_RESULT = 'function_execute_result'

    VALUE_PUBLISH = 'value_publish'

    SCENARIO_VERIFY = 'scenario_verify'
    SCENARIO_ADD = 'scenario_add'
    SCENARIO_RUN = 'scenario_run'
    SCENARIO_STOP = 'scenario_stop'
    SCENARIO_UPDATE = 'scenario_update'
    SCENARIO_DELETE = 'scenario_delete'

    SCENARIO_VERIFY_RESULT = 'scenario_verify_result'
    SCENARIO_ADD_RESULT = 'schedule_scenario_result'
    SCENARIO_RUN_RESULT = 'scenario_run_result'
    SCENARIO_STOP_RESULT = 'scenario_stop_result'
    SCENARIO_UPDATE_RESULT = 'schedule_scenario_result'
    SCENARIO_DELETE_RESULT = 'scenario_delete_result'

    SUPER_FUNCTION_EXECUTE = 'super_function_execute'
    SUPER_FUNCTION_EXECUTE_RESULT = 'super_function_execute_result'
    SUB_FUNCTION_EXECUTE = 'sub_function_execute'
    SUB_FUNCTION_EXECUTE_RESULT = 'sub_function_execute_result'
    SUB_SCHEDULE = 'sub_schedule'
    SUB_SCHEDULE_RESULT = 'sub_schedule_result'
    SUPER_SCHEDULE = 'super_schedule'
    SUPER_SCHEDULE_RESULT = 'super_schedule_result'

    @classmethod
    def get(cls, name: str):
        try:
            return cls[name.upper()]
        except Exception:
            return cls.UNDEFINED


class SoPElementType(Enum):
    UNDEFINED = 'undefined'
    DEVICE = 'device'
    MIDDLEWARE = 'middleware'
    THING = 'thing'
    SERVICE = 'service'
    SCENARIO = 'scenario'

    @classmethod
    def get(cls, name: str):
        try:
            return cls[name.upper()]
        except Exception:
            return cls.UNDEFINED


class SoPElementActionType(Enum):
    UNDEFINED = 'UNDEFINED'

    RUN = 'RUN'
    KILL = 'KILL'
    UNREGISTER = 'UNREGISTER'
    SCENARIO_VERIFY = 'SCENARIO_VERIFY'
    SCENARIO_ADD = 'SCENARIO_ADD'
    SCENARIO_RUN = 'SCENARIO_RUN'
    SCENARIO_STOP = 'SCENARIO_STOP'
    SCENARIO_UPDATE = 'SCENARIO_UPDATE'
    SCENARIO_DELETE = 'SCENARIO_DELETE'
    DELAY = 'DELAY'

    @classmethod
    def get(cls, name: str):
        try:
            return cls[name.upper()]
        except Exception:
            return cls.UNDEFINED


class SoPScenarioStateType(Enum):
    UNDEFINED = -1
    CREATED = 'created'
    SCHEDULING = 'scheduling'
    INITIALIZED = 'initialized'
    RUNNING = 'running'
    EXECUTING = 'executing'
    STUCKED = 'stucked'
    COMPLETED = 'completed'

    @classmethod
    def get(cls, name: str):
        try:
            return cls[name.upper()]
        except Exception:
            return cls.UNDEFINED


class SoPScenarioInfo:
    '''
        return dict(id=scenario_info['id'], 
        name=scenario_info['name'], 
        code=scenario_info['contents'],
        state=SoPScenarioStateType.get(scenario_info['state']), 
        schedule_info=scenario_info['scheduleInfo'])
    '''

    def __init__(self, id: int, name: str, code: str, state: SoPScenarioStateType, schedule_info: List[dict]) -> None:
        self.id = id
        self.name = name
        self.code = code
        self.state = state
        self.schedule_info = schedule_info


class SoPEvent:

    def __init__(self, event_type: SoPEventType, element: 'SoPElement' = None, middleware_element: 'SoPMiddlewareElement' = None, thing_element: 'SoPThingElement' = None, service_element: 'SoPServiceElement' = None, scenario_element: 'SoPScenarioElement' = None,
                 timestamp: float = None, duration: float = None, delay: float = None,
                 error: SoPErrorType = None, return_type: SoPType = None, return_value: Union[int, float, bool, str] = None,
                 requester_middleware_name: str = None) -> None:
        self.event_type = event_type

        self.middleware_element = middleware_element
        self.element = element
        self.thing_element = thing_element
        self.service_element = service_element
        self.scenario_element = scenario_element

        self.timestamp = timestamp
        self.duration = duration

        self.delay = delay

        self.error = error
        self.return_type = return_type
        self.return_value = return_value
        self.requester_middleware_name = requester_middleware_name

    def load(data: dict):
        pass

    def dump(self) -> dict:
        # TODO: self.element.name이 겹치는 경우 대책이 필요
        return dict(event_type=self.event_type.value,
                    element=self.element.name if self.element else None,
                    timestamp=self.timestamp,
                    duration=self.duration,
                    delay=self.delay)


class SoPElement(metaclass=ABCMeta):

    def __init__(self, name: str, level: int, element_type: SoPElementType) -> None:
        # basic info
        self.name = name
        self.level = level
        self.element_type = element_type

    def load(self, data: dict) -> None:
        self.name = data['name']
        self.level = data['level']
        self.element_type = SoPElementType.get(data['element_type'])

        return self

    def dump(self) -> dict:
        return dict(name=self.name,
                    level=self.level,
                    element_type=self.element_type.value)

    def dump_event(self, event_type: SoPEventType, timestamp: float) -> SoPEvent:
        return SoPEvent(element=self,
                        event_type=event_type,
                        timestamp=timestamp)


class SoPDeviceElement(SoPElement):
    def __init__(self, name: str = '', level: int = None, element_type: SoPElementType = None,
                 host: str = '', ssh_port: int = None, user: str = '', password: str = '') -> None:
        super().__init__(name, level, element_type)

        self.host = host
        self.user = user
        self.ssh_port = ssh_port
        self.password = password

        self.available_port_list: List[int] = []

    def __eq__(self, __o: object) -> bool:
        return self.host == __o.host and self.user == __o.user and self.ssh_port == __o.ssh_port and self.password == __o.password

    def load(self, data: dict) -> 'SoPDeviceElement':
        self.name = data['name']
        self.element_type = SoPElementType.get(data['element_type'])

        self.host = data['host']
        self.user = data['user']
        self.ssh_port = data['ssh_port']
        self.password = data['password']

        return self

    def dump(self):
        return dict(name=self.name,
                    element_type=self.element_type.value,
                    host=self.host,
                    user=self.user,
                    ssh_port=self.ssh_port,
                    password=self.password)


class SoPMiddlewareElement(SoPElement):

    CFG_TEMPLATE = '''%s
broker_uri = "tcp://%s:%d"

middleware_identifier = "%s"
socket_listening_port = %d
alive_checking_period = 60

main_db_file_path = "%s/%s_Main.db"
value_log_db_file_path = "%s/%s_ValueLog.db"

log_level = 5
log_file_path = "%s/%s_middleware.log"
log_max_size = 300
log_backup_num = 100'''

    MOSQUITTO_CONF_TEMPLATE = '''persistence true
persistence_location /var/lib/mosquitto/

include_dir /etc/mosquitto/conf.d

listener %d 0.0.0.0
protocol mqtt
allow_anonymous true

listener %d 0.0.0.0
protocol websockets
allow_anonymous true

listener %d 0.0.0.0
protocol mqtt
allow_anonymous true
cafile /etc/mosquitto/ca_certificates/ca.crt
certfile /etc/mosquitto/certs/host.crt
keyfile /etc/mosquitto/certs/host.key
require_certificate true

listener %d 0.0.0.0
protocol websockets
allow_anonymous true
cafile /etc/mosquitto/ca_certificates/ca.crt
certfile /etc/mosquitto/certs/host.crt
keyfile /etc/mosquitto/certs/host.key
require_certificate true'''

    INIT_SCRIPT_TEMPLATE = '''MAIN_DB=%s/%s_Main.db
VALUE_LOG_DB=%s/%s_ValueLog.db

if [ -f "$MAIN_DB" ]; then
    rm -f $MAIN_DB
fi
if [ -f "$VALUE_LOG_DB" ]; then
    rm -f $VALUE_LOG_DB
fi

sqlite3 $MAIN_DB < %s/src/middleware/MainDBCreate
sqlite3 $VALUE_LOG_DB < %s/src/middleware/ValueLogDBCreate'''

    def __init__(self, name: str = '', level: int = None, element_type: SoPElementType = None,
                 thing_list: List['SoPThingElement'] = [], scenario_list: List['SoPScenarioElement'] = [], child_middleware_list: List['SoPMiddlewareElement'] = [],
                 device: SoPDeviceElement = None,
                 middleware_config_path: str = '', remote_middleware_path: str = None, remote_middleware_config_path: str = None,
                 mqtt_port: int = None, ssl_mqtt_port: int = None, web_socket_port: int = None, ssl_web_socket_port: int = None, local_server_port: int = None) -> None:
        super().__init__(name, level, element_type)

        self.thing_list = thing_list
        self.scenario_list = scenario_list
        self.child_middleware_list = child_middleware_list

        self.device = device

        self.remote_middleware_path = remote_middleware_path
        self.remote_middleware_config_path = remote_middleware_config_path
        self.remote_middleware_cfg_file_path = ''
        self.remote_mosquitto_conf_file_path = ''
        self.remote_init_script_file_path = ''

        self.middleware_config_path = middleware_config_path
        self.middleware_cfg_file_path = ''
        self.mosquitto_conf_file_path = ''
        self.init_script_file_path = ''

        self.middleware_cfg = ''
        self.mosquitto_conf = ''
        self.init_script = ''

        self.mqtt_port = mqtt_port
        self.ssl_mqtt_port = ssl_mqtt_port
        self.web_socket_port = web_socket_port
        self.ssl_web_socket_port = ssl_web_socket_port
        self.local_server_port = local_server_port

        self.online = False
        self.event_log: List[SoPEvent] = []
        self.recv_queue: Queue = Queue()

    def load(self, data: dict):
        super().load(data)

        self.thing_list = [SoPThingElement().load(thing_info)
                           for thing_info in data['thing_list']]
        self.scenario_list = [SoPScenarioElement().load(
            scenario_info) for scenario_info in data['scenario_list']]
        self.child_middleware_list = [SoPMiddlewareElement().load(
            child_middleware_info) for child_middleware_info in data['child_middleware_list']]

        self.device = SoPDeviceElement().load(data['device'])

        self.middleware_config_path = data['middleware_config_path']
        self.remote_middleware_path = data['remote_middleware_path']
        self.remote_middleware_config_path = data['remote_middleware_config_path']

        return self

    def dump(self):
        '''
            element의 정보를 json 형식으로 반환하는 함수
        '''
        return dict(
            **super().dump(),
            thing_list=[thing.dump() for thing in self.thing_list],
            scenario_list=[scenario.dump() for scenario in self.scenario_list],
            child_middleware_list=[child_middleware.dump(
            ) for child_middleware in self.child_middleware_list],
            device=self.device.dump(),
            middleware_config_path=self.middleware_config_path,
            remote_middleware_path=self.remote_middleware_path,
            remote_middleware_config_path=self.remote_middleware_config_path,
            mqtt_port=self.mqtt_port,
            ssl_mqtt_port=self.ssl_mqtt_port,
            web_socket_port=self.web_socket_port,
            ssl_web_socket_port=self.ssl_web_socket_port,
            local_server_port=self.local_server_port)

    # TODO: implement
    def dump_event(self, event_type: SoPEventType, timestamp: float) -> SoPEvent:
        '''
            element가 취할 event에 대한 정보를 반환하는 함수
        '''
        return super().dump_event(event_type, timestamp)

    def set_port(self, mqtt_port: int, ssl_mqtt_port: int, web_socket_port: int, ssl_web_socket_port: int, local_server_port: int):
        self.mqtt_port = mqtt_port
        self.ssl_mqtt_port = ssl_mqtt_port
        self.web_socket_port = web_socket_port
        self.ssl_web_socket_port = ssl_web_socket_port
        self.local_server_port = local_server_port

    def generate_cfg(self):
        def generate_cfg_recursive(middleware: SoPMiddlewareElement, upper_middleware: SoPMiddlewareElement = None):
            if upper_middleware is None:
                parent_middleware_line = ''
            else:
                parent_middleware_line = f'parent_broker_uri = "tcp://{upper_middleware.device.host}:{upper_middleware.mqtt_port}'

            middleware.middleware_cfg = SoPMiddlewareElement.CFG_TEMPLATE % (parent_middleware_line,
                                                                             self.device.host,
                                                                             self.mqtt_port,
                                                                             self.name,
                                                                             self.local_server_port,
                                                                             self.remote_middleware_config_path,
                                                                             self.name,
                                                                             self.remote_middleware_config_path,
                                                                             self.name,
                                                                             self.middleware_config_path,
                                                                             self.name)
            for child_middleware in middleware.child_middleware_list:
                generate_cfg_recursive(child_middleware, middleware)

        generate_cfg_recursive(self, None)

    def generate_mosquitto_conf(self):
        def generate_mosquitto_conf_recursive(middleware: SoPMiddlewareElement):
            middleware.mosquitto_conf = middleware.MOSQUITTO_CONF_TEMPLATE % (self.mqtt_port,
                                                                              self.ssl_mqtt_port,
                                                                              self.web_socket_port,
                                                                              self.ssl_web_socket_port)
            for child_middleware in middleware.child_middleware_list:
                generate_mosquitto_conf_recursive(child_middleware)

        generate_mosquitto_conf_recursive(self)

    def generate_int_script(self):
        def generate_int_script_recursive(middleware: SoPMiddlewareElement):
            middleware.init_script = middleware.INIT_SCRIPT_TEMPLATE % (self.remote_middleware_config_path,
                                                                        self.name,
                                                                        self.remote_middleware_config_path,
                                                                        self.name,
                                                                        self.remote_middleware_path,
                                                                        self.remote_middleware_path)
            for child_middleware in middleware.child_middleware_list:
                generate_int_script_recursive(child_middleware)

        generate_int_script_recursive(self)


class SoPServiceElement(SoPElement):
    def __init__(self, name: str = '', level: int = None, element_type: SoPElementType = None,
                 tag_list: List[str] = [], is_super: bool = False, energy: float = 0, execute_time: float = 0,
                 code: str = '', instance_code: str = '') -> None:
        super().__init__(name, level, element_type)

        self.tag_list = tag_list
        self.is_super = is_super
        self.energy = energy
        self.execute_time = execute_time

        self.code = code
        self.instance_code = instance_code

    def load(self, data: dict) -> 'SoPServiceElement':
        super().load(data)

        self.tag_list = data['tag_list']
        self.is_super = data['is_super']
        self.energy = data['energy']
        self.execute_time = data['execute_time']

        return self

    def dump(self) -> dict:
        return dict(**super().dump(),
                    tag_list=self.tag_list,
                    is_super=self.is_super,
                    energy=self.energy,
                    execute_time=self.execute_time)

    def dump_event(self, event_type: SoPEventType, timestamp: float) -> SoPEvent:
        return super().dump_event(event_type, timestamp)


class SoPThingElement(SoPElement):
    def __init__(self, name: str = '', level: int = None, element_type: SoPElementType = None,
                 service_list: List['SoPServiceElement'] = [],  is_super: bool = False, alive_cycle: float = 0,
                 device: SoPDeviceElement = None,
                 thing_file_path: str = '', remote_thing_file_path: str = '', code: str = '',) -> None:
        super().__init__(name, level, element_type)

        self.service_list = service_list
        self.is_super = is_super
        self.alive_cycle = alive_cycle

        self.device = device

        self.thing_file_path = thing_file_path
        self.remote_thing_file_path = remote_thing_file_path
        self.code = code

        self.event_log: List[SoPEvent] = []
        self.recv_queue: Queue = Queue()

    def load(self, data: dict):
        super().load(data)

        self.service_list = [SoPServiceElement().load(service_info)
                             for service_info in data['service_list']]
        self.is_super = data['is_super']
        self.alive_cycle = data['alive_cycle']

        self.device = data['device']

        self.thing_file_path = data['thing_file_path']
        self.remote_thing_file_path = data['remote_thing_file_path']
        self.code = data['code']

        return self

    def dump(self):
        return dict(**super().dump(),
                    service_list=[service.dump()
                                  for service in self.service_list],
                    is_super=self.is_super,
                    alive_cycle=self.alive_cycle,
                    device=self.device.dump(),
                    thing_file_path=self.thing_file_path,
                    remote_thing_file_path=self.remote_thing_file_path,
                    code=self.code)

    def find_service_by_name(self, service_name: str) -> SoPServiceElement:
        for service in self.service_list:
            if service.name == service_name:
                return service


class SoPScenarioElement(SoPElement):
    def __init__(self, name: str = '', level: int = None, element_type: SoPElementType = None,
                 service_list: List[SoPServiceElement] = [], period: float = None,
                 code: str = '') -> None:
        super().__init__(name, level, element_type)

        self.service_list = service_list
        self.period = period

        self.code = code

        self.event_log: List[SoPEvent] = []
        self.recv_queue: Queue = Queue()

    def load(self, data: dict) -> None:
        super().load(data)

        self.service_list = [SoPServiceElement().load(service_info)
                             for service_info in data['service_list']]
        self.period = data['period']
        self.code = data['code']

        return self

    def dump(self) -> dict:
        return dict(**super().dump(),
                    service_list=[service.dump()
                                  for service in self.service_list],
                    period=self.period,
                    code=self.code)
