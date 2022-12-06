from big_thing_py.tests.tools.ssh_client import *
from big_thing_py.tests.tools.mqtt_client import *


class SoPEventHandler:

    def __init__(self, simulation_env: SoPMiddlewareElement = None, event_log: List[SoPEvent] = [], simulation_start_time: float = None) -> None:
        self.simulation_env = simulation_env
        self.device_list: List[SoPDeviceElement] = []
        self.middleware_list: List[SoPMiddlewareElement] = []

        self.mqtt_client_list: List[SoPMQTTClient] = []
        self.ssh_client_list: List[SoPSSHClient] = []

        self.event_listener_event = Event()
        self.event_listener_thread: SoPThread = SoPThread(
            name='event_listener', func=self.event_listener, arg_list=(self.event_listener_event, ))

        # simulator와 같은 인스턴스를 공유한다.
        self.simulation_start_time = simulation_start_time
        self.event_log: List[SoPEvent] = event_log

    def add_mqtt_client(self, mqtt_client: SoPMQTTClient):
        self.mqtt_client_list.append(mqtt_client)

    def add_ssh_client(self, ssh_client: SoPSSHClient):
        self.ssh_client_list.append(ssh_client)

    def update_middleware_device_list(self):
        middleware_list: List[SoPMiddlewareElement] = get_middleware_list_recursive(
            self.simulation_env)
        device_list: List[SoPDeviceElement] = [
            middleware.device for middleware in middleware_list]
        for device in device_list:
            if device in self.device_list:
                continue
            self.device_list.append(device)

        for middleware in middleware_list:
            for device in self.device_list:
                if device == middleware.device:
                    middleware.device = device
        self.middleware_list = middleware_list

    def init_ssh_client_list(self):
        for device in self.device_list:
            ssh_client = SoPSSHClient(device)
            ssh_client.connect()
            ssh_client.update_available_port()
            self.add_ssh_client(ssh_client)

    def init_mqtt_client_list(self):
        for middleware in self.middleware_list:
            picked_port_list = random.sample(
                middleware.device.available_port_list, 5)
            middleware.set_port(*tuple(picked_port_list))
            for picked_port in picked_port_list:
                middleware.device.available_port_list.remove(picked_port)

            mqtt_client = SoPMQTTClient(middleware)
            self.add_mqtt_client(mqtt_client)

    def find_ssh_client(self, middleware: SoPMiddlewareElement) -> SoPSSHClient:
        for ssh_client in self.ssh_client_list:
            if ssh_client.device == middleware.device:
                return ssh_client

    def find_mqtt_client(self, middleware: SoPMiddlewareElement) -> SoPMQTTClient:
        for mqtt_client in self.mqtt_client_list:
            if mqtt_client.middleware == middleware:
                return mqtt_client

    def find_mqtt_client_by_client_id(self, client_id: str) -> SoPMQTTClient:
        for mqtt_client in self.mqtt_client_list:
            if mqtt_client.get_client_id() == client_id:
                return mqtt_client

    def event_listener_start(self):
        self.event_listener_thread.start()

    def event_trigger(self, event: SoPEvent):
        if event.event_type == SoPEventType.DELAY:
            SOPTEST_LOG_DEBUG(f'Delay {event.delay} Sec start...', 0)
            self.event_log.append(event)
            time.sleep(event.delay)
        else:
            # wait until timestamp is reached
            if event.timestamp:
                while time.time() - self.simulation_start_time < event.timestamp:
                    time.sleep(THREAD_TIME_OUT)

            if event.event_type == SoPEventType.MIDDLEWARE_RUN:
                if not isinstance(event.element, SoPMiddlewareElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPMiddlewareElement.__name__}')
                target_middleware: SoPMiddlewareElement = event.element

                # self.run_middleware(target_middleware)
                SoPThread(name=f'{event.event_type.value}_{event.element.name}',
                          func=self.run_middleware, arg_list=(target_middleware, )).start()
            elif event.event_type == SoPEventType.MIDDLEWARE_KILL:
                # TODO: implement kill middleware
                pass
            elif event.event_type == SoPEventType.THING_RUN:
                if not isinstance(event.element, SoPThingElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPThingElement.__name__}')
                target_thing = event.element

                # wait until all middleware is online
                while not self.check_all_middleware_online():
                    time.sleep(THREAD_TIME_OUT)

                # self.run_thing(target_thing)
                SoPThread(name=f'{event.event_type.value}_{event.element.name}',
                          func=self.run_thing, arg_list=(target_thing, )).start()
            elif event.event_type == SoPEventType.THING_KILL:
                if not isinstance(event.element, SoPThingElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPThingElement.__name__}')
                # TODO: implement kill thing
                pass
            elif event.event_type == SoPEventType.SCENARIO_VERIFY:
                if not isinstance(event.element, SoPScenarioElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPScenarioElement.__name__}')
                target_scenario: SoPScenarioElement = event.element
                self.verify_scenario(target_scenario)
                # SoPThread(name=f'{event.event_type.value}_{event.element.name}',
                #           func=self.verify_scenario, arg_list=(target_scenario, )).start()
            elif event.event_type == SoPEventType.SCENARIO_ADD:
                if not isinstance(event.element, SoPScenarioElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPScenarioElement.__name__}')
                target_scenario: SoPScenarioElement = event.element
                self.add_scenario(target_scenario)
                # SoPThread(name=f'{event.event_type.value}_{event.element.name}',
                #           func=self.add_scenario, arg_list=(target_scenario, )).start()
            elif event.event_type == SoPEventType.SCENARIO_RUN:
                if not isinstance(event.element, SoPScenarioElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPScenarioElement.__name__}')
                target_scenario: SoPScenarioElement = event.element
                self.run_scenario(target_scenario)
                # SoPThread(name=f'{event.event_type.value}_{event.element.name}',
                #           func=self.run_scenario, arg_list=(target_scenario, )).start()
            elif event.event_type == SoPEventType.SCENARIO_STOP:
                # TODO: 시나리오의 상태를 먼저 확인해야하는 로직을 추가해아함
                if not isinstance(event.element, SoPScenarioElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPScenarioElement.__name__}')
                target_scenario: SoPScenarioElement = event.element
                self.stop_scenario(target_scenario)
                # SoPThread(name=f'{event.event_type.value}_{event.element.name}',
                #           func=self.stop_scenario, arg_list=(target_scenario, )).start()
            elif event.event_type == SoPEventType.SCENARIO_UPDATE:
                if not isinstance(event.element, SoPScenarioElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPScenarioElement.__name__}')
                target_scenario: SoPScenarioElement = event.element
                self.update_scenario(target_scenario)
                # SoPThread(name=f'{event.event_type.value}_{event.element.name}',
                #           func=self.update_scenario, arg_list=(target_scenario, )).start()
            elif event.event_type == SoPEventType.SCENARIO_DELETE:
                # TODO: 시나리오의 상태를 먼저 확인해야하는 로직을 추가해아함
                if not isinstance(event.element, SoPScenarioElement):
                    raise Exception(
                        f'Event type is {event.event_type}, but target element is not {SoPScenarioElement.__name__}')
                target_scenario: SoPScenarioElement = event.element
                self.delete_scenario(target_scenario)
                # SoPThread(name=f'{event.event_type.value}_{event.element.name}',
                #           func=self.delete_scenario, arg_list=(target_scenario, )).start()

    def event_listener(self, stop_event: Event):
        recv_msg = None

        try:
            while not stop_event.wait(THREAD_TIME_OUT):
                for mqtt_client in self.mqtt_client_list:
                    try:
                        recv_msg = mqtt_client.recv_message_queue.get(
                            timeout=THREAD_TIME_OUT)
                        self.on_recv_message(recv_msg)
                    except Empty:
                        recv_msg = None

        except Exception as e:
            stop_event.set()
            print_error(e)
            return False

    ####  middleware   #############################################################################################################

    def run_mosquitto(self, middleware: SoPMiddlewareElement, ssh_client: SoPSSHClient):
        cur_time = 0

        while True:
            target_mosquitto_pid_list = ssh_client.send_command(
                f'netstat -lpn | grep :{middleware.mqtt_port}')
            if len(target_mosquitto_pid_list) > 0:
                break
            else:
                if get_current_time() - cur_time > 1:
                    SOPTEST_LOG_DEBUG(
                        f'retry to run mosquitto on {middleware.name}-{middleware.device.host}:{middleware.mqtt_port} ... check it', 1)
                    ssh_client.send_command(
                        f'/sbin/mosquitto -c {middleware.remote_mosquitto_conf_file_path} -v 2> {middleware.remote_middleware_config_path}/{middleware.name}_mosquitto.log &', ignore_result=True)
                    cur_time = get_current_time()
                else:
                    time.sleep(0.1)

    def init_middleware(self, middleware: SoPMiddlewareElement, ssh_client: SoPSSHClient):
        cur_time = 0

        ssh_client.send_command(
            f'chmod +x {middleware.remote_init_script_file_path}')
        ssh_client.send_command(
            f'bash {middleware.remote_init_script_file_path}')

        while True:
            file_list: List[str] = ssh_client.send_command(
                f'ls {middleware.remote_middleware_config_path}')
            time.sleep(0.1)
            if f'{middleware.name}_Main.db' in file_list:
                break
            else:
                if get_current_time() - cur_time > 1:
                    SOPTEST_LOG_DEBUG(
                        'db file was not created... check it', 1)
                    cur_time = get_current_time()
                else:
                    time.sleep(0.1)

    def run_middleware(self, middleware: SoPMiddlewareElement, timeout: float = 10):
        ssh_client = self.find_ssh_client(middleware)
        mqtt_client = self.find_mqtt_client(middleware)
        _, parent_middleware = find_element_recursive(
            self.simulation_env, middleware)
        parent_middleware: SoPMiddlewareElement

        while parent_middleware and not parent_middleware.online:
            time.sleep(0.5)
            SOPTEST_LOG_DEBUG(
                f'wait for parent middleware {parent_middleware.name} online', 1)

        self.run_mosquitto(middleware, ssh_client)
        self.init_middleware(middleware, ssh_client)
        mqtt_client.run()

        # 미들웨어가 켜지는 것을 확실히 하면 parent를 굳이 확인하지 않아도 된다.
        # self.check_parent_online()

        remote_home_dir = ssh_client.send_command('cd ~ && pwd')[0]
        cd_command = f'cd {os.path.dirname(middleware.remote_middleware_config_path)}'
        middleware_run_command = f'{middleware.remote_middleware_path.replace("~", remote_home_dir)}/src/middleware/sopiot_middleware -f {middleware.remote_middleware_cfg_file_path.replace("~", remote_home_dir)} > /dev/null 2>&1 &'
        ssh_client.send_command(
            f'{cd_command}; {middleware_run_command}', ignore_result=True)

        def check_online(mqtt_client: SoPMQTTClient, timeout: float = 10):
            topic, payload, timestamp = self.publish_and_expect(
                middleware,
                encode_MQTT_message(SoPProtocolType.WebClient.EM_REFRESH.value % (
                    mqtt_client.get_client_id()), '{}'),
                SoPProtocolType.WebClient.ME_RESULT_SERVICE_LIST.value % (
                    mqtt_client.get_client_id()),
                auto_subscribe=True,
                auto_unsubscribe=False,
                timeout=timeout)
            if payload is not None:
                SOPTEST_LOG_DEBUG(
                    f'Middleware {middleware.name} on {middleware.device.host}:{middleware.mqtt_port} was online!', 0)
                middleware.online = True
                return True
            else:
                SOPTEST_LOG_DEBUG(
                    f'Middleware {middleware.name} on {middleware.device.host}:{middleware.mqtt_port} was not online!', 1)
                return False

        def check_online_with_timeout(mqtt_client: SoPMQTTClient, timeout: int = 10, check_interval: float = 0.5):
            while timeout > 0:
                if check_online(mqtt_client=mqtt_client, timeout=check_interval):
                    return True
                else:
                    timeout -= check_interval
                    time.sleep(check_interval)
            else:
                raise SOPTEST_LOG_DEBUG(
                    f'[TIMEOUT] Running middleware {middleware.name} was failed...', -1)

        check_online_with_timeout(mqtt_client, timeout=timeout)

    ####  thing   #############################################################################################################

    def check_thing_register(self, thing: SoPThingElement, mqtt_client: SoPMQTTClient, timeout: float = 10):
        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, thing)

        topic, payload, timestamp = self.expect(
            thing,
            target_topic=SoPProtocolType.Base.TM_REGISTER.value % thing.name,
            auto_subscribe=True,
            auto_unsubscribe=False,
            timeout=timeout)

        if payload is not None:
            topic, payload, timestamp = self.expect(
                thing,
                target_topic=SoPProtocolType.Base.MT_RESULT_REGISTER.value % thing.name,
                auto_subscribe=True,
                auto_unsubscribe=False,
                timeout=timeout)
            if int(payload['error']) in [0, -4]:
                return True
            else:
                SOPTEST_LOG_DEBUG(
                    f'Register was failed... error code: {payload["error"]}', -1)
                return False
        else:
            SOPTEST_LOG_DEBUG(
                f'TM_REGISTER was not detected...', -1)
            return False

    def subscribe_thing_topic(self, thing: SoPThingElement, middleware: SoPMiddlewareElement, mqtt_client: SoPMQTTClient):
        for service in thing.service_list:
            mqtt_client.subscribe([SoPProtocolType.Base.MT_EXECUTE.value % (service.name, thing.name, '+', '#'),
                                   (SoPProtocolType.Base.MT_EXECUTE.value % (
                                       service.name, thing.name, '', '')).rstrip('/'),
                                   SoPProtocolType.Base.TM_RESULT_EXECUTE.value % (
                service.name, thing.name, '+', '#'),
                (SoPProtocolType.Base.TM_RESULT_EXECUTE.value % (service.name, thing.name, '', '')).rstrip('/')])
            if thing.is_super:
                mqtt_client.subscribe([
                    SoPProtocolType.Super.MS_EXECUTE.value % (
                        service.name, thing.name, middleware.name, '#'),
                    SoPProtocolType.Super.SM_EXECUTE.value % (
                        '+', '+', '+', thing.name),
                    SoPProtocolType.Super.MS_RESULT_EXECUTE.value % (
                        '+', '+', '+', thing.name),
                    SoPProtocolType.Super.SM_RESULT_EXECUTE.value % (
                        service.name, thing.name, middleware.name, '#'),
                    SoPProtocolType.Super.MS_SCHEDULE.value % (
                        service.name, thing.name, middleware.name, '#'),
                    SoPProtocolType.Super.SM_SCHEDULE.value % (
                        '+', '+', '+', thing.name),
                    SoPProtocolType.Super.MS_RESULT_SCHEDULE.value % (
                        '+', '+', '+', thing.name),
                    SoPProtocolType.Super.SM_RESULT_SCHEDULE.value % (
                        service.name, thing.name, middleware.name, '#')])
        # for value in self._value_list:
        #     mqtt_client.subscribe([SoPProtocolType.Default.TM_VALUE_PUBLISH.value % (thing.name, value['name']),
        #                                         SoPProtocolType.Default.TM_VALUE_PUBLISH_OLD.value % (thing.name, value['name'])])

    def run_thing(self, thing: SoPThingElement, timeout: float = 10):
        SOPTEST_LOG_DEBUG(f'Start run {thing.name}...', 0)
        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, thing)
        target_parent_middelware: SoPMiddlewareElement
        ssh_client = self.find_ssh_client(target_parent_middelware)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)

        target_topic_list = [SoPProtocolType.Base.TM_REGISTER.value % thing.name,
                             SoPProtocolType.Base.TM_UNREGISTER.value % thing.name,
                             SoPProtocolType.Base.MT_RESULT_REGISTER.value % thing.name,
                             SoPProtocolType.Base.MT_RESULT_UNREGISTER.value % thing.name]
        mqtt_client.subscribe(target_topic_list)

        result = ssh_client.send_command('cd ~ && pwd')
        thing_cd_command = f'cd {os.path.dirname(thing.remote_thing_file_path)}'
        thing_run_command = f'{thing_cd_command}; python {thing.remote_thing_file_path.replace("~", result[0])} -n {thing.name} -ip {mqtt_client.host} -p {mqtt_client.port} > /dev/null 2>&1 &'
        print(thing_run_command.split('>')[0].strip())
        ssh_client.send_command(thing_run_command, ignore_result=True)

        if self.check_thing_register(thing, mqtt_client, timeout=timeout):
            SOPTEST_LOG_DEBUG(
                f'Register complete thing {thing.name} on {target_parent_middelware.name}', 0)
            self.subscribe_thing_topic(
                thing, target_parent_middelware, mqtt_client)
        else:
            raise SOPTEST_LOG_DEBUG(
                f'Thing {thing.name} register failed...', -1)

    ####  scenario   #############################################################################################################

    # TODO: implement this
    def verify_scenario(self, scenario: SoPScenarioElement, timeout: float = 10):
        _, target_parent_middelware = find_element_recursive(scenario)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)

        trigger_topic = SoPProtocolType.WebClient.EM_VERIFY_SCENARIO.value % mqtt_client.get_client_id()
        trigger_payload = json_string_to_dict(
            dict(name=scenario.name, text=scenario.code))
        trigger_message = encode_MQTT_message(trigger_topic, trigger_payload)
        target_topic = SoPProtocolType.WebClient.ME_RESULT_VERIFY_SCENARIO.value % mqtt_client.get_client_id()

        mqtt_client.subscribe(trigger_topic)
        topic, payload, timestamp = self.publish_and_expect(
            scenario,
            trigger_message,
            target_topic,
            auto_unsubscribe=False,
            timeout=timeout)

        if check_result_payload(payload, SoPElementType.SCENARIO.value, scenario.name, SoPElementActionType.SCENARIO_VERIFY.value, True):
            return self
        else:
            raise Exception(
                f'{SoPElementType.SCENARIO.value} {scenario.name} {SoPElementActionType.SCENARIO_VERIFY.value} failed...')

    def add_scenario(self, scenario: SoPScenarioElement, timeout: float = 10, check_interval: float = 0.5):
        # 시나리오가 super service를 포함하고 있으면, check_super_thing_exist를 실행하여 super thing이 scenario 입장에서 보이는지 확인한다
        if not all([not service.is_super for service in scenario.service_list]):
            if not self.check_super_thing_exist(scenario):
                raise SOPTEST_LOG_DEBUG(
                    f'[{get_current_function_name()}] Check super thing exist check of {scenario.name} failed...', -1)

        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, scenario)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)

        trigger_topic = SoPProtocolType.WebClient.EM_ADD_SCENARIO.value % mqtt_client.get_client_id()
        trigger_payload = json_string_to_dict(
            dict(name=scenario.name, text=scenario.code))
        trigger_message = encode_MQTT_message(trigger_topic, trigger_payload)
        target_topic = SoPProtocolType.WebClient.ME_RESULT_ADD_SCENARIO.value % mqtt_client.get_client_id()

        mqtt_client.subscribe(trigger_topic)
        topic, payload, timestamp = self.publish_and_expect(
            scenario,
            trigger_message,
            target_topic,
            auto_subscribe=True,
            auto_unsubscribe=False,
            timeout=timeout)

        if check_result_payload(payload, SoPElementType.SCENARIO.value, scenario.name, SoPElementActionType.SCENARIO_ADD.value, True):
            while timeout > 0:
                scenario_info = self.get_scenario_info(
                    scenario)
                # 시나리오가 준비 되었는지 확인하고 넘어간다.
                if scenario_info.state not in [SoPScenarioStateType.INITIALIZED, SoPScenarioStateType.COMPLETED]:
                    SOPTEST_LOG_DEBUG(
                        f'Scenario {scenario.name} is scheduling... wait for schedule finish', 1)
                    # self.update_scenario(scenario)
                    time.sleep(check_interval)
                    timeout -= check_interval
                else:
                    SOPTEST_LOG_DEBUG(
                        f'Scenario {scenario.name} is initialized!!!', 0)
                    break
            else:
                raise SOPTEST_LOG_DEBUG(f'Scenario initialize failed...', -1)
            return self
        else:
            raise Exception(
                f'{SoPElementType.SCENARIO.value} {scenario.name} {SoPElementActionType.SCENARIO_ADD.value} failed...')

    def run_scenario(self, scenario: SoPScenarioElement, timeout: float = 10):
        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, scenario)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)

        trigger_topic = SoPProtocolType.WebClient.EM_RUN_SCENARIO.value % mqtt_client.get_client_id()
        trigger_payload = json_string_to_dict(
            dict(name=scenario.name, text=scenario.code))
        trigger_message = encode_MQTT_message(trigger_topic, trigger_payload)
        target_topic = SoPProtocolType.WebClient.ME_RESULT_RUN_SCENARIO.value % mqtt_client.get_client_id()

        mqtt_client.subscribe(trigger_topic)
        topic, payload, timestamp = self.publish_and_expect(
            scenario,
            trigger_message,
            target_topic,
            auto_subscribe=True,
            auto_unsubscribe=False,
            timeout=timeout)

        if check_result_payload(payload, SoPElementType.SCENARIO.value, scenario.name, SoPElementActionType.SCENARIO_RUN.value, True):
            return self
        else:
            raise Exception(
                f'{SoPElementType.SCENARIO.value} {scenario.name} {SoPElementActionType.SCENARIO_RUN.value} failed...')

    def stop_scenario(self, scenario: SoPScenarioElement, timeout: float = 10):
        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, scenario)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)

        trigger_topic = SoPProtocolType.WebClient.EM_STOP_SCENARIO.value % mqtt_client.get_client_id()
        trigger_payload = json_string_to_dict(
            dict(name=scenario.name, text=scenario.code))
        trigger_message = encode_MQTT_message(trigger_topic, trigger_payload)
        target_topic = SoPProtocolType.WebClient.ME_RESULT_STOP_SCENARIO.value % mqtt_client.get_client_id()

        mqtt_client.subscribe(trigger_topic)
        topic, payload, timestamp = self.publish_and_expect(
            scenario,
            trigger_message,
            target_topic,
            auto_subscribe=True,
            auto_unsubscribe=False,
            timeout=timeout)

        if check_result_payload(payload, SoPElementType.SCENARIO.value, scenario.name, SoPElementActionType.SCENARIO_STOP.value, True):
            (encode_MQTT_message(topic, payload))
            return self
        else:
            raise Exception(
                f'{SoPElementType.SCENARIO.value} {scenario.name} {SoPElementActionType.SCENARIO_STOP.value} failed...')

    def update_scenario(self, scenario: SoPScenarioElement, timeout: float = 10):
        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, scenario)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)

        trigger_topic = SoPProtocolType.WebClient.EM_UPDATE_SCENARIO.value % mqtt_client.get_client_id()
        trigger_payload = json_string_to_dict(
            dict(name=scenario.name, text=scenario.code))
        trigger_message = encode_MQTT_message(trigger_topic, trigger_payload)
        target_topic = SoPProtocolType.WebClient.ME_RESULT_UPDATE_SCENARIO.value % mqtt_client.get_client_id()

        mqtt_client.subscribe(trigger_topic)
        topic, payload, timestamp = self.publish_and_expect(
            scenario,
            trigger_message,
            target_topic,
            auto_subscribe=True,
            auto_unsubscribe=False,
            timeout=timeout)

        if check_result_payload(payload, SoPElementType.SCENARIO.value, scenario.name, SoPElementActionType.SCENARIO_UPDATE.value, True):
            return self
        else:
            raise Exception(
                f'{SoPElementType.SCENARIO.value} {scenario.name} {SoPElementActionType.SCENARIO_UPDATE.value} failed...')

    def delete_scenario(self, scenario: SoPScenarioElement, timeout: float = 10):
        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, scenario)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)

        trigger_topic = SoPProtocolType.WebClient.EM_DELETE_SCENARIO.value % mqtt_client.get_client_id()
        trigger_payload = json_string_to_dict(
            dict(name=scenario.name, text=scenario.code))
        trigger_message = encode_MQTT_message(trigger_topic, trigger_payload)
        target_topic = SoPProtocolType.WebClient.ME_RESULT_DELETE_SCENARIO.value % mqtt_client.get_client_id()

        mqtt_client.subscribe(trigger_topic)
        topic, payload, timestamp = self.publish_and_expect(
            scenario,
            trigger_message,
            target_topic,
            auto_subscribe=True,
            auto_unsubscribe=False,
            timeout=timeout)

        if check_result_payload(payload, SoPElementType.SCENARIO.value, scenario.name, SoPElementActionType.SCENARIO_DELETE.value, True):
            return self
        else:
            raise Exception(
                f'{SoPElementType.SCENARIO.value} {scenario.name} {SoPElementActionType.SCENARIO_DELETE.value} failed...')

    def get_scenario_info(self, scenario: SoPScenarioElement, timeout: float = 10) -> SoPScenarioInfo:
        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, scenario)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)
        retry_period = 0.5
        while timeout:
            topic, payload, timestamp = self.publish_and_expect(
                scenario,
                encode_MQTT_message(
                    SoPProtocolType.WebClient.EM_REFRESH.value % f'{mqtt_client.get_client_id()}_get_scenario_info@{scenario.name}', '{}'),
                SoPProtocolType.WebClient.ME_RESULT_SCENARIO_LIST.value % f'{mqtt_client.get_client_id()}_get_scenario_info@{scenario.name}',
                auto_subscribe=True,
                auto_unsubscribe=False,
                timeout=timeout)
            for scenario_info in payload['scenarios']:
                if scenario_info['name'] == scenario.name:
                    return SoPScenarioInfo(id=scenario_info['id'],
                                           name=scenario_info['name'],
                                           state=SoPScenarioStateType.get(
                                               scenario_info['state']),
                                           code=scenario_info['contents'],
                                           schedule_info=scenario_info['scheduleInfo'])
            else:
                SOPTEST_LOG_DEBUG(
                    f'Scenario {scenario.name} not found...', -1)
                timeout -= retry_period
                time.sleep(retry_period)
        else:
            raise SOPTEST_LOG_DEBUG(
                f'[{get_current_function_name()}] Update scenario state failed...', -1)

    def check_super_thing_exist(self, scenario: SoPScenarioElement, retry_period: float = 0.5, timeout: float = 10):
        _, target_parent_middelware = find_element_recursive(
            self.simulation_env, scenario)
        mqtt_client = self.find_mqtt_client(target_parent_middelware)
        target_parent_middelware: SoPMiddlewareElement

        while timeout:
            topic, payload, timestamp = self.publish_and_expect(
                scenario,
                encode_MQTT_message(
                    SoPProtocolType.WebClient.EM_REFRESH.value % f'{mqtt_client.get_client_id()}_check_super_thing_exist@{scenario.name}', '{}'),
                SoPProtocolType.WebClient.ME_RESULT_SERVICE_LIST.value % (
                    f'{mqtt_client.get_client_id()}_check_super_thing_exist@{scenario.name}'),
                auto_subscribe=True,
                auto_unsubscribe=False,
                timeout=timeout)
            if payload is not None:
                for super_service in [service for service in scenario.service_list if service.is_super]:
                    super_thing: SoPThingElement = None
                    thing_list: List[SoPThingElement] = get_thing_list_recursive(
                        self.simulation_env)
                    for thing in thing_list:
                        # TODO: 이름으로 비교하는게 아니라 인스턴스 자체의 __eq__를 호출해서 비교해야함
                        if super_service.name in [service.name for service in thing.service_list]:
                            super_thing = thing

                    for service in payload['services']:
                        thing_list = service['things']
                        if super_thing.name in [thing['id'] for thing in thing_list if bool(thing['is_super'])]:
                            SOPTEST_LOG_DEBUG(
                                f'Super thing {super_thing.name} detected on {target_parent_middelware.name}!', 0)
                            return True
                        else:
                            SOPTEST_LOG_DEBUG(
                                f'Thing {super_thing.name} is not detected. retry...', 1)
                            timeout -= retry_period
                            time.sleep(retry_period)
            else:
                raise SOPTEST_LOG_DEBUG(
                    'get thing list failed... payload is None', -1)
        else:
            return False

    #### kill ##########################################################################################################################

    def kill_all_mosquitto(self):
        for ssh_client in self.ssh_client_list:
            ssh_client.send_command('pidof mosquitto | xargs kill -9')

    def kill_all_middleware(self):
        for ssh_client in self.ssh_client_list:
            ssh_client.send_command('pidof sopiot_middleware | xargs kill -9')

    def kill_all_python(self):
        for ssh_client in self.ssh_client_list:
            ssh_client.send_command('pidof python | xargs kill -9')

    def kill_all_simulation_instance(self):
        self.kill_all_mosquitto()
        self.kill_all_middleware()
        self.kill_all_python()
        
    def remove_all_remote_simulation_file(self):
        middleware_list: List[SoPMiddlewareElement] = get_middleware_list_recursive(self.simulation_env)
        for middleware in middleware_list:
            ssh_client = self.find_ssh_client(middleware)
            ssh_client.send_command(f'rm -r {middleware.remote_middleware_config_path}')
            ssh_client.send_command(f'rm -r {middleware.remote_middleware_config_path}')
            for thing in middleware.thing_list:
                ssh_client.send_command(f'rm -r {os.path.dirname(thing.remote_thing_file_path)}')
                ssh_client.send_command(f'rm -r {os.path.dirname(os.path.dirname(thing.remote_thing_file_path))}')
        

    #### expect ##########################################################################################################################

    def expect(self, element: SoPElement, target_topic: str = None, auto_subscribe: bool = True, auto_unsubscribe: bool = False, timeout: int = 10) -> Union[Tuple[str, dict], str]:
        cur_time = time.time()
        if isinstance(element, SoPMiddlewareElement):
            target_middleware, _ = find_element_recursive(
                self.simulation_env, element)
        else:
            _, target_middleware = find_element_recursive(
                self.simulation_env, element)
        target_middleware: SoPMiddlewareElement
        mqtt_client = self.find_mqtt_client(target_middleware)

        if not mqtt_client.is_run:
            raise Exception(
                f'{target_middleware.name} mqtt_client is not running...')

        try:
            if auto_subscribe:
                mqtt_client.subscribe(target_topic)

            while True:
                if time.time() - cur_time > timeout:
                    raise Empty('Timeout')

                topic, payload, timestamp = decode_MQTT_message(
                    element.recv_queue.get(timeout=timeout))

                if target_topic:
                    topic_slice = topic.split('/')
                    target_topic_slice = target_topic.split('/')
                    for i in range(len(target_topic_slice)):
                        if target_topic_slice[i] not in ['#', '+'] and target_topic_slice[i] != topic_slice[i]:
                            break
                    else:
                        return topic, payload, timestamp
                else:
                    element.recv_queue.put(
                        encode_MQTT_message(topic, payload, timestamp))
        except Empty as e:
            SOPLOG_DEBUG(f'SoPMQTTClient Timeout for {target_topic}', 'red')
            return None, None, None
        except Exception as e:
            raise e
        finally:
            if auto_unsubscribe:
                if target_topic:
                    mqtt_client.unsubscribe(target_topic)

    def publish_and_expect(self, element: SoPElement, trigger_msg: mqtt.MQTTMessage = None, target_topic: str = None, auto_subscribe: bool = True, auto_unsubscribe: bool = False, timeout: int = 10):
        if isinstance(element, SoPMiddlewareElement):
            target_middleware, _ = find_element_recursive(
                self.simulation_env, element)
        else:
            _, target_middleware = find_element_recursive(
                self.simulation_env, element)
        target_middleware: SoPMiddlewareElement
        mqtt_client = self.find_mqtt_client(target_middleware)

        if not mqtt_client.is_run:
            mqtt_client.run()

        if auto_subscribe:
            mqtt_client.subscribe(target_topic)
        trigger_topic, trigger_payload, timestamp = decode_MQTT_message(
            trigger_msg, mode=str)
        mqtt_client.publish(trigger_topic, trigger_payload, retain=False)

        ret = self.expect(element, target_topic,
                          auto_subscribe, auto_unsubscribe, timeout)
        return ret

    def command_and_expect(self, element: SoPElement, trigger_command: Union[List[str], str] = None, target_topic: str = None,
                           auto_subscribe: bool = True, auto_unsubscribe: bool = False, timeout: int = 10):
        if isinstance(element, SoPMiddlewareElement):
            target_middleware, _ = find_element_recursive(
                self.simulation_env, element)
        else:
            _, target_middleware = find_element_recursive(
                self.simulation_env, element)
        target_middleware: SoPMiddlewareElement
        mqtt_client = self.find_mqtt_client(target_middleware)
        ssh_client = self.find_ssh_client(target_middleware)

        if not mqtt_client.is_run:
            mqtt_client.run()

        if auto_subscribe:
            mqtt_client.subscribe(target_topic)
        if isinstance(trigger_command, list):
            for command in trigger_command:
                ssh_client.send_command(command)
        else:
            ssh_client.send_command(trigger_command)
        ret = self.expect(element, target_topic,
                          auto_subscribe, auto_unsubscribe, timeout)
        return ret

    #### on_recv_message ##########################################################################################################################

    def on_recv_message(self, msg: mqtt.MQTTMessage):
        topic, payload, timestamp = decode_MQTT_message(msg)
        timestamp = time.time()

        return_type = SoPType.get(payload.get('return_type', None))
        return_value = payload.get('return_value', None)
        error_type = SoPErrorType.get(payload.get('error', None))

        if SoPProtocolType.WebClient.ME_RESULT_SERVICE_LIST.get_prefix() in topic:
            client_id = topic.split('/')[3]

            # for check_super_thing_exist
            if 'check_super_thing_exist' in client_id:
                scenario_name = client_id.split('@')[1]
                scenario, middleware = find_element_by_name_recursive(
                    self.simulation_env, scenario_name)
                scenario.recv_queue.put(msg)
            # for check middleware online
            else:
                mqtt_client = self.find_mqtt_client_by_client_id(client_id)
                mqtt_client.middleware.recv_queue.put(msg)
        elif SoPProtocolType.WebClient.ME_RESULT_SCENARIO_LIST.get_prefix() in topic:
            client_id = topic.split('/')[3]
            print(client_id)

            if 'get_scenario_info' in client_id:
                scenario_name = client_id.split('@')[1]
                scenario, middleware = find_element_by_name_recursive(
                    self.simulation_env, scenario_name)
                scenario.recv_queue.put(msg)
        elif SoPProtocolType.Base.TM_REGISTER.get_prefix() in topic:
            thing_name = topic.split('/')[2]

            thing, middleware = find_element_by_name_recursive(
                self.simulation_env, thing_name)
            thing.recv_queue.put(msg)
            self.event_log.append(SoPEvent(
                event_type=SoPEventType.THING_REGISTER, middleware_element=middleware, thing_element=thing, timestamp=timestamp, duration=0))
        elif SoPProtocolType.Base.MT_RESULT_REGISTER.get_prefix() in topic:
            thing_name = topic.split('/')[3]

            thing, middleware = find_element_by_name_recursive(
                self.simulation_env, thing_name)
            thing.recv_queue.put(msg)
            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.thing_element == thing and event.event_type == SoPEventType.THING_REGISTER:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    break
        elif SoPProtocolType.Base.TM_UNREGISTER.get_prefix() in topic:
            thing_name = topic.split('/')[2]

            thing, middleware = find_element_by_name_recursive(
                self.simulation_env, thing_name)
            thing.recv_queue.put(msg)
            self.event_log.append(SoPEvent(
                event_type=SoPEventType.THING_UNREGISTER, middleware_element=middleware, thing_element=thing, timestamp=timestamp, duration=0))
        elif SoPProtocolType.Base.MT_RESULT_UNREGISTER.get_prefix() in topic:
            thing_name = topic.split('/')[3]

            thing, middleware = find_element_by_name_recursive(
                self.simulation_env, thing_name)
            thing.recv_queue.put(msg)
            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.thing_element == thing and event.event_type == SoPEventType.THING_UNREGISTER:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    break
        elif SoPProtocolType.Base.MT_EXECUTE.get_prefix() in topic:
            function_name = topic.split('/')[2]
            thing_name = topic.split('/')[3]

            thing, middleware = find_element_by_name_recursive(
                self.simulation_env, thing_name)
            thing: SoPThingElement
            service: SoPServiceElement = thing.find_service_by_name(
                function_name)
            middleware: SoPMiddlewareElement
            if len(topic.split('/')) > 4:
                middleware_name = topic.split('/')[4]
                request_ID = topic.split('/')[5]

                requester_middleware_name = request_ID.split('@')[0]
                super_thing_name = request_ID.split('@')[1]
                super_function_name = request_ID.split('@')[2]
                subrequest_order = request_ID.split('@')[3]
            else:
                requester_middleware_name = None

            self.event_log.append(SoPEvent(
                event_type=SoPEventType.FUNCTION_EXECUTE, middleware_element=middleware, thing_element=thing, service_element=service, timestamp=timestamp, duration=0, requester_middleware_name=requester_middleware_name))
        elif SoPProtocolType.Base.TM_RESULT_EXECUTE.get_prefix() in topic:
            function_name = topic.split('/')[3]
            thing_name = topic.split('/')[4]
            scenario_name = payload.get('scenario', None)

            thing, middleware = find_element_by_name_recursive(
                self.simulation_env, thing_name)
            thing: SoPThingElement
            service: SoPServiceElement = thing.find_service_by_name(
                function_name)
            middleware: SoPMiddlewareElement
            if len(topic.split('/')) > 5:
                middleware_name = topic.split('/')[5]
                request_ID = topic.split('/')[6]

                requester_middleware_name = request_ID.split('@')[0]
                super_thing_name = request_ID.split('@')[1]
                super_function_name = request_ID.split('@')[2]
                subrequest_order = request_ID.split('@')[3]
            else:
                requester_middleware_name = None

            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.thing_element == thing and event.service_element == service and event.event_type == SoPEventType.FUNCTION_EXECUTE:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    event.return_type = return_type
                    event.return_value = return_value
                    event.requester_middleware_name = requester_middleware_name

                    SOPTEST_LOG_DEBUG(
                        f'[EXECUTE] thing: {thing_name} function: {function_name} scenario: {scenario_name} duration: {event.duration} return value:{return_value} - {return_type.value}', 0)
                    break
        elif SoPProtocolType.WebClient.EM_VERIFY_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement

            self.event_log.append(SoPEvent(
                event_type=SoPEventType.SCENARIO_VERIFY, middleware_element=middleware, scenario_element=scenario, timestamp=timestamp, duration=0))
        elif SoPProtocolType.WebClient.ME_RESULT_VERIFY_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement

            scenario.recv_queue.put(msg)
            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.scenario_element == scenario and event.event_type == SoPEventType.SCENARIO_VERIFY:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    SOPTEST_LOG_DEBUG(
                        f'[SCENE_VERIFY] scenario: {scenario_name} duration: {event.duration}', 1)
                    break
        elif SoPProtocolType.WebClient.EM_ADD_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)
            SOPTEST_LOG_DEBUG(f'EM_ADD_SCENARIO {scenario_name}', payload)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement
            self.event_log.append(SoPEvent(
                event_type=SoPEventType.SCENARIO_ADD, middleware_element=middleware, scenario_element=scenario, timestamp=timestamp, duration=0))
        elif SoPProtocolType.WebClient.ME_RESULT_ADD_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)
            SOPTEST_LOG_DEBUG(
                f'ME_RESULT_ADD_SCENARIO {scenario_name}', payload)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement

            scenario.recv_queue.put(msg)
            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.scenario_element == scenario and event.event_type == SoPEventType.SCENARIO_ADD:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    SOPTEST_LOG_DEBUG(
                        f'[SCENE_ADD] scenario: {scenario_name} duration: {event.duration}', 1)
                    break
        elif SoPProtocolType.WebClient.EM_RUN_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement
            self.event_log.append(SoPEvent(
                event_type=SoPEventType.SCENARIO_RUN, middleware_element=middleware, scenario_element=scenario, timestamp=timestamp, duration=0))
        elif SoPProtocolType.WebClient.ME_RESULT_RUN_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement

            scenario.recv_queue.put(msg)
            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.scenario_element == scenario and event.event_type == SoPEventType.SCENARIO_RUN:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    SOPTEST_LOG_DEBUG(
                        f'[SCENE_RUN] scenario: {scenario_name} duration: {event.duration}', 1)
                    break
        elif SoPProtocolType.WebClient.EM_STOP_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement
            self.event_log.append(SoPEvent(
                event_type=SoPEventType.SCENARIO_STOP, middleware_element=middleware, scenario_element=scenario, timestamp=timestamp, duration=0))
        elif SoPProtocolType.WebClient.ME_RESULT_STOP_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement

            scenario.recv_queue.put(msg)
            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.scenario_element == scenario and event.event_type == SoPEventType.SCENARIO_STOP:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    SOPTEST_LOG_DEBUG(
                        f'[SCENE_STOP] scenario: {scenario_name} duration: {event.duration}', 1)
                    break
        elif SoPProtocolType.WebClient.EM_UPDATE_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement
            self.event_log.append(SoPEvent(
                event_type=SoPEventType.SCENARIO_UPDATE, middleware_element=middleware, scenario_element=scenario, timestamp=timestamp, duration=0))
        elif SoPProtocolType.WebClient.ME_RESULT_UPDATE_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement

            scenario.recv_queue.put(msg)
            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.scenario_element == scenario and event.event_type == SoPEventType.SCENARIO_UPDATE:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    SOPTEST_LOG_DEBUG(
                        f'[SCENE_UPDATE] scenario: {scenario_name} duration: {event.duration}', 1)
                    break
        elif SoPProtocolType.WebClient.EM_DELETE_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement
            self.event_log.append(SoPEvent(
                event_type=SoPEventType.SCENARIO_DELETE, middleware_element=middleware, scenario_element=scenario, timestamp=timestamp, duration=0))
        elif SoPProtocolType.WebClient.ME_RESULT_DELETE_SCENARIO.get_prefix() in topic:
            scenario_name = payload.get('name', None)

            scenario, middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            scenario: SoPThingElement
            middleware: SoPMiddlewareElement

            scenario.recv_queue.put(msg)
            for event in list(reversed(self.event_log)):
                if event.middleware_element == middleware and event.scenario_element == scenario and event.event_type == SoPEventType.SCENARIO_DELETE:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    SOPTEST_LOG_DEBUG(
                        f'[SCENE_DELETE] scenario: {scenario_name} duration: {event.duration}', 1)
                    break
        elif SoPProtocolType.Super.MS_SCHEDULE.get_prefix() in topic:
            requester_middleware_name = topic.split('/')[5]
            super_middleware_name = topic.split('/')[4]
            super_thing_name = topic.split('/')[3]
            super_function_name = topic.split('/')[2]

            scenario_name = payload.get('scenario', None)

            super_thing, middleware = find_element_by_name_recursive(
                self.simulation_env, super_thing_name)
            scenario, requester_middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            super_thing: SoPThingElement
            super_service: SoPServiceElement = super_thing.find_service_by_name(
                super_function_name)
            middleware: SoPMiddlewareElement
            requester_middleware: SoPMiddlewareElement

            self.event_log.append(SoPEvent(
                event_type=SoPEventType.SUPER_SCHEDULE, middleware_element=middleware, thing_element=super_thing, service_element=super_service, scenario_element=scenario, timestamp=timestamp, duration=0))
            SOPTEST_LOG_DEBUG(
                f'[SUPER_SCHEDULE_START] super_middleware: {super_middleware_name} requester_middleware: {requester_middleware_name} super_thing: {super_thing_name} super_function: {super_function_name} scenario: {scenario_name}', 0)
        elif SoPProtocolType.Super.SM_SCHEDULE.get_prefix() in topic:
            pass
        elif SoPProtocolType.Super.MS_RESULT_SCHEDULE.get_prefix() in topic:
            pass
        elif SoPProtocolType.Super.SM_RESULT_SCHEDULE.get_prefix() in topic:
            requester_middleware_name = topic.split('/')[6]
            super_middleware_name = topic.split('/')[5]
            super_thing_name = topic.split('/')[4]
            super_function_name = topic.split('/')[3]

            scenario_name = payload.get('scenario', None)

            super_thing, middleware = find_element_by_name_recursive(
                self.simulation_env, super_thing_name)
            scenario, requester_middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            super_thing: SoPThingElement
            super_service: SoPServiceElement = super_thing.find_service_by_name(
                super_function_name)
            middleware: SoPMiddlewareElement

            for event in list(reversed(self.event_log)):
                if event.thing_element == super_thing and event.service_element == super_service and event.scenario_element == scenario and event.event_type == SoPEventType.SUPER_SCHEDULE:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    event.return_type = return_type
                    event.return_value = return_value

                    SOPTEST_LOG_DEBUG(
                        f'[SUPER_SCHEDULE_END] super_middleware: {super_middleware_name} requester_middleware: {requester_middleware_name} super_thing: {super_thing_name} super_function: {super_function_name} scenario: {scenario_name} duration: {event.duration} result: {event.error.value}', 0)
                    break

        ################################################################################################################################################################################################################################################

        elif SoPProtocolType.Super.MS_EXECUTE.get_prefix() in topic:
            super_function_name = topic.split('/')[2]
            super_thing_name = topic.split('/')[3]
            super_middleware_name = topic.split('/')[4]
            requester_middleware_name = topic.split('/')[5]

            scenario_name = payload.get('scenario', None)

            super_thing, middleware = find_element_by_name_recursive(
                self.simulation_env, super_thing_name)
            scenario, requester_middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            super_thing: SoPThingElement
            super_service: SoPServiceElement = super_thing.find_service_by_name(
                super_function_name)
            middleware: SoPMiddlewareElement

            self.event_log.append(SoPEvent(
                event_type=SoPEventType.SUPER_FUNCTION_EXECUTE, middleware_element=middleware, thing_element=super_thing, service_element=super_service, scenario_element=scenario, timestamp=timestamp, duration=0))
            SOPTEST_LOG_DEBUG(
                f'[SUPER_EXECUTE_START] super_middleware: {super_middleware_name} requester_middleware: {requester_middleware_name} super_thing: {super_thing_name} super_function: {super_function_name} scenario: {scenario_name}', 0)
        elif SoPProtocolType.Super.SM_EXECUTE.get_prefix() in topic:
            pass
        elif SoPProtocolType.Super.MS_RESULT_EXECUTE.get_prefix() in topic:
            pass
        elif SoPProtocolType.Super.SM_RESULT_EXECUTE.get_prefix() in topic:
            requester_middleware_name = topic.split('/')[6]
            super_middleware_name = topic.split('/')[5]
            super_thing_name = topic.split('/')[4]
            super_function_name = topic.split('/')[3]

            scenario_name = payload.get('scenario', None)

            super_thing, middleware = find_element_by_name_recursive(
                self.simulation_env, super_thing_name)
            scenario, requester_middleware = find_element_by_name_recursive(
                self.simulation_env, scenario_name)
            super_thing: SoPThingElement
            super_service: SoPServiceElement = super_thing.find_service_by_name(
                super_function_name)
            middleware: SoPMiddlewareElement

            for event in list(reversed(self.event_log)):
                if event.thing_element == super_thing and event.service_element == super_service and event.scenario_element == scenario and event.event_type == SoPEventType.SUPER_FUNCTION_EXECUTE:
                    event.duration = timestamp - event.timestamp
                    event.error = error_type
                    event.return_type = return_type
                    event.return_value = return_value
                    SOPTEST_LOG_DEBUG(
                        f'[SUPER_EXECUTE_END] super_middleware: {super_middleware_name} requester_middleware: {requester_middleware_name} super_thing: {super_thing_name} super_function: {super_function_name} scenario: {scenario_name} duration: {event.duration} result: {event.error.value} return value:{return_value} - {return_type.value}', 0)
                    break
        # elif SoPProtocolType.Default.TM_VALUE_PUBLISH.get_prefix() in topic:
        #     pass
        # elif SoPProtocolType.Default.TM_VALUE_PUBLISH_OLD.get_prefix() in topic:
        #     pass

    def check_all_middleware_online(self):
        for middleware in self.middleware_list:
            if not middleware.online:
                return False

        return True
