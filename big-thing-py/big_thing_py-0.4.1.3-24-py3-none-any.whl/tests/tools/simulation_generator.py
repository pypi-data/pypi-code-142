from big_thing_py.tests.tools.simulator import *
from big_thing_py.tests.tools.config import *

import random
import requests
import shutil


class SoPSimulationGenerator:

    BAN_WORD_LIST = ['if', 'else', 'and', 'or', 'loop', 'wait_until', 'msec',
                     'sec', 'min', 'hour', 'day', 'month', 'all', 'single', 'random']

    def __init__(self, config_path: str) -> None:
        self.config_path: str = config_path
        self.config_name: str = ''
        self.device_config, self.middleware_config, self.thing_config, self.service_config, self.scenario_config = self.load_config(
            self.config_path)

        self.middleware_generator = SoPMiddlewareGenerator(
            self.middleware_config, self.device_config)
        self.service_generator = SoPServiceGenerator(self.service_config)
        self.thing_generator = SoPThingGenerator(
            self.thing_config, self.middleware_config, self.service_config)
        self.scenario_generator = SoPScenarioGenerator(
            self.scenario_config, self.middleware_config)

    def generate_simulation(self):
        self.smulation_folder_path = f'{self.config_path}/simulation_{self.config_name}_{get_current_time(TimeFormat.DATETIME2)}'
        base_thing_folder_path = f'{self.smulation_folder_path}/{self.thing_config.base.thing_folder_path}'
        super_thing_folder_path = f'{self.smulation_folder_path}/{self.thing_config.super.thing_folder_path}'
        remote_base_thing_folder_path = f'{self.thing_config.base.remote_thing_folder_path}'
        remote_super_thing_folder_path = f'{self.thing_config.super.remote_thing_folder_path}'

        # simulation generator가 thing 파일을 만드는 것이 아니라 모든 정보가 들어있는 simulation_dump.json 파일을 만들어서
        # simulatior가 simulation_dump.json 파일을 읽은후 해당 정보를 바탕으로 thing을 만들어서 simulation을 실행하도록 변경

        # for path in [base_thing_folder_path, super_thing_folder_path]:
        #     if os.path.exists(path):
        #         shutil.rmtree(path)
        #     os.makedirs(path, exist_ok=True)

        # base service, base thing을 먼저 생성한다.
        simulation_env = self.middleware_generator.dump()
        base_service_pool = self.service_generator.dump()
        self.thing_generator.dump(
            simulation_env, base_service_pool, base_thing_folder_path, remote_base_thing_folder_path)

        # 이후 생성된 base element를 가지고 super service, super thing을 생성한다.
        super_service_pool = self.service_generator.dump_super(
            simulation_env)
        self.thing_generator.dump_super(
            super_service_pool, simulation_env, super_thing_folder_path, remote_super_thing_folder_path)
        # self.thing_generator.dump_file(simulation_env)

        # 시나리오 생성 부분
        self.scenario_generator.dump(simulation_env)
        self.scenario_generator.dump_super(simulation_env)
        # self.scenario_generator.dump_file(simulation_env)

        simulation_dump = self.dump(simulation_env)
        smulation_file_path = self.dump_file(
            simulation_dump, self.smulation_folder_path)
        return smulation_file_path

    def load(self, simulation_dump: dict):
        return SoPMiddlewareElement().load(simulation_dump['component'])

    def dump(self, simulation_env: SoPMiddlewareElement):
        # generate simulation env
        component = simulation_env.dump()
        middleware_list: List[SoPMiddlewareElement] = get_middleware_list_recursive(
            simulation_env)
        thing_list: List[SoPThingElement] = get_thing_list_recursive(
            simulation_env)
        scenario_list: List[SoPScenarioElement] = get_scenario_list_recursive(
            simulation_env)

        # generate simulation event timeline
        event_timeline = []
        event_timeline.extend([middleware.dump_event(
            SoPEventType.MIDDLEWARE_RUN, 0.0).dump() for middleware in middleware_list])
        event_timeline.extend(
            [thing.dump_event(SoPEventType.THING_RUN, 0.0).dump() for thing in sorted(thing_list, key=lambda x: x.is_super, reverse=False)])
        event_timeline.append(
            SoPEvent(delay=3.0, event_type=SoPEventType.DELAY).dump())
        event_timeline.extend([scenario.dump_event(
            SoPEventType.SCENARIO_ADD, 0.0).dump() for scenario in sorted(scenario_list, key=lambda x: all([service.is_super for service in x.service_list]), reverse=True)])
        event_timeline.append(
            SoPEvent(delay=3.0, event_type=SoPEventType.DELAY).dump())
        event_timeline.extend([scenario.dump_event(
            SoPEventType.SCENARIO_RUN, 0.0).dump() for scenario in sorted(scenario_list, key=lambda x: all([service.is_super for service in x.service_list]), reverse=True)])
        event_timeline.append(SoPEvent(event_type=SoPEventType.END).dump())
        simulation_dump = dict(component=component,
                               event_timeline=event_timeline)
        return simulation_dump

    def dump_file(self, simulation_dump: dict, smulation_folder_path: str):
        os.makedirs(smulation_folder_path, exist_ok=True)
        write_file(f'{smulation_folder_path}/simulation_data.json',
                   dict_to_json_string(simulation_dump))
        return f'{smulation_folder_path}/simulation_data.json'

    def load_config(self, path: str):
        if path:
            config_path = f'{path}/config.yml'
            config = load_yaml(config_path)
            self.config_name = os.path.basename(path)
            # self.config_path = path

            device_config = SoPDeviceConfig(config['device_config'])
            middleware_config = SoPMiddlewareConfig(
                config['middleware_config'], config_path=self.config_path)
            service_config = SoPServiceConfig(config['service_config'])
            thing_config = SoPThingConfig(
                config['thing_config'], config_path=self.config_path)
            scenario_config = SoPScenarioConfig(
                config['scenario_config'], config_path=self.config_path)
            return device_config, middleware_config,  thing_config, service_config, scenario_config
        else:
            raise SOPTEST_LOG_DEBUG(f'File not found: {path}', -1)


class SoPElementGenerator(metaclass=ABCMeta):

    def __init__(self, config: SoPConfig = None) -> None:
        self.config: SoPConfig = config

    @abstractmethod
    def dump(self):
        pass


class SoPMiddlewareGenerator(SoPElementGenerator):
    def __init__(self, config: SoPMiddlewareConfig = None, device_config: SoPDeviceConfig = None) -> None:
        super().__init__(config)

        self.config: SoPMiddlewareConfig
        self.device_config: SoPDeviceConfig = device_config

        self.device_pool: List[SoPDeviceElement] = []

        for device in self.device_config.device_list:
            device: SoPDeviceConfig.DeviceInfo
            device_element = SoPDeviceElement(
                device.name, None, SoPElementType.DEVICE, device.host, device.ssh_port, device.user, device.password)
            self.device_pool.append(device_element)

    def generate_middleware(self, height: int, index: int, upper_middleware: SoPMiddlewareElement = None) -> dict:
        device: SoPDeviceElement = random.choice(self.device_pool)

        if upper_middleware:
            upper_middleware_index = '_'.join(
                upper_middleware.name.split('_')[1:])
            name = f'middleware_{upper_middleware_index}__level{height}_{index}'
        else:
            name = f'middleware_level{height}_{index}'

        middleware = SoPMiddlewareElement(name=name,
                                          level=height,
                                          element_type=SoPElementType.MIDDLEWARE,
                                          thing_list=[],
                                          scenario_list=[],
                                          child_middleware_list=[],
                                          device=device,
                                          middleware_config_path=self.config.middleware_config_path,
                                          remote_middleware_path=self.config.remote_middleware_path,
                                          remote_middleware_config_path=self.config.remote_middleware_config_path,
                                          mqtt_port=None,
                                          ssl_mqtt_port=None,
                                          web_socket_port=None,
                                          ssl_web_socket_port=None,
                                          local_server_port=None)
        return middleware

    def dump(self):
        root_middleware: SoPMiddlewareElement = self.generate_middleware(
            self.config.height, 0, None)

        def dump_recursive(height: int, child_per_node: int, upper_middleware: SoPMiddlewareElement):
            upper_middleware.child_middleware_list.extend([self.generate_middleware(
                height - 1, i, upper_middleware) for i in range(random.randint(child_per_node[0], child_per_node[1]))])
            if height - 1 > 1:
                for child_middleware in upper_middleware.child_middleware_list:
                    dump_recursive(height - 1, child_per_node,
                                   child_middleware)

            return upper_middleware

        dump_recursive(self.config.height,
                       self.config.child_per_node, root_middleware)

        return root_middleware


class SoPServiceGenerator(SoPElementGenerator):

    BAN_WORD_LIST = ['if', 'else', 'and', 'or', 'loop', 'wait_until', 'msec', 'list', 'base', 'super',
                     'sec', 'min', 'hour', 'day', 'month', 'all', 'single', 'random']

    FAIL_SERVICE_TEMPLATE = '''\
def %s() -> int:
    SOPLOG_DEBUG(f'function {get_current_function_name()} or %s is run...')
    raise Exception('fail service')  
'''

    SERVICE_TEMPLATE = '''\
def %s() -> int:
    SOPLOG_DEBUG(f'function {get_current_function_name()} run... return %s')
    time.sleep(%s)
    return %s
'''
    SUPER_FUNCTION_TEMPLATE = '''\
def %s(self, key) -> int:
    SOPLOG_DEBUG(
        f'super function {get_current_function_name()} run...')
    results = []

    %s

    result_sum = 0
    for result in results:
        for subresult in result:
            return_value = subresult['return_value']
            result_sum += return_value

    return result_sum   
'''
    SUBFUNCTION_TEMPLATE = '''\
results += [self.req(key, subfunction_name='%s', tag_list=%s, arg_list=(), service_type=SoPServiceType.FUNCTION, policy=SoPPolicy.%s)]'''
    SERVICE_INSTANCE_TEMPLATE = '''\
SoPFunction(func=%s, return_type=SoPType.INTEGER, tag_list=[%s], arg_list=[], exec_time=%s, energy=%s)'''
    SUPER_FUNCTION_INSTANCE_TEMPLATE = '''\
SoPSuperFunction(func=self.%s, return_type=SoPType.INTEGER, tag_list=[%s], arg_list=[], exec_time=%s, energy=%s)'''

    def __init__(self, config: SoPServiceConfig = None) -> None:
        super().__init__(config)
        self.config: SoPServiceConfig

        self.tag_name_pool = generate_random_words(
            self.config.tag_type_num, ban_word_list=self.BAN_WORD_LIST)
        self.service_pool: List[SoPServiceElement] = []
        self.super_service_pool: List[SoPServiceElement] = []

        self.service_name_pool = generate_random_words(
            self.config.base.service_type_num * 10, ban_word_list=self.BAN_WORD_LIST)
        self.picked_service_name_pool = random.sample(
            self.service_name_pool, self.config.base.service_type_num)
        self.super_service_name_pool = generate_random_words(
            self.config.super.service_type_num * 10, ban_word_list=self.BAN_WORD_LIST)
        self.picked_super_service_name_pool = random.sample(
            self.service_name_pool, self.config.super.service_type_num)

    def generate_subfunction_req_lines(self, candidate_service_list: List[SoPServiceElement]) -> Tuple[List[str], List[SoPServiceElement]]:
        req_lines: List[str] = []
        picked_subfunction_list: List[SoPServiceElement] = random.sample(
            candidate_service_list, random.randint(self.config.subfunction_per_super_service[0],
                                                   self.config.subfunction_per_super_service[1]))

        for picked_subfunction in picked_subfunction_list:
            subfunction_name = f'{picked_subfunction.name}'
            picked_tag_list = random.sample(picked_subfunction.tag_list, random.randint(
                1, len(picked_subfunction.tag_list)))
            policy = random.choice(['ALL', 'SINGLE'])
            req_lines.append(self.SUBFUNCTION_TEMPLATE %
                             (subfunction_name, picked_tag_list, policy))

        return req_lines, picked_subfunction_list

    def dump(self):
        self.service_pool = []
        for service_name in self.picked_service_name_pool:
            service_name = f'function_{service_name}'
            tag_list = random.sample(self.tag_name_pool, random.randint(
                self.config.tag_per_service[0], self.config.tag_per_service[1]))
            energy = random.randint(
                self.config.base.energy[0], self.config.base.energy[1])
            execute_time = random.uniform(
                self.config.base.execute_time[0], self.config.base.execute_time[1])
            return_value = random.randint(0, 1000)

            tag_code = ', '.join([f'SoPTag("{tag}")' for tag in tag_list])
            service_instance_code = self.SERVICE_INSTANCE_TEMPLATE % (
                service_name, tag_code, execute_time + self.config.base.execute_time_margin, energy)
            service_code = self.SERVICE_TEMPLATE % (
                service_name, return_value, execute_time, return_value)
            self.service_pool.append(SoPServiceElement(name=service_name,
                                                       level=None,
                                                       element_type=SoPElementType.SERVICE,
                                                       tag_list=tag_list,
                                                       is_super=False,
                                                       energy=energy,
                                                       execute_time=execute_time,
                                                       code=service_code,
                                                       instance_code=service_instance_code))
        return self.service_pool

    # TODO: 지금은 top level의 미들웨어에만 super service를 넣는다. 나중에는 모든 미들웨어에 넣을 수 있도록 수정해야 한다.
    def dump_super(self, root_middleware: SoPMiddlewareElement):

        def get_all_candidate_service_list(root_middleware: SoPMiddlewareElement):
            candidate_service_list = []
            for thing in root_middleware.thing_list:
                candidate_service_list.extend(thing.service_list)
            for middleware in root_middleware.child_middleware_list:
                candidate_service_list.extend(
                    get_all_candidate_service_list(middleware))

            return candidate_service_list

        candidate_service_list = get_all_candidate_service_list(
            root_middleware)

        for super_service_name in self.picked_super_service_name_pool:
            super_service_name = f'super_function_{super_service_name}'
            tags = random.sample(self.tag_name_pool, random.randint(
                self.config.tag_per_service[0], self.config.tag_per_service[1]))
            energy = random.randint(
                self.config.super.energy[0], self.config.super.energy[1])

            # TODO: subfunction을 기반으로 생성
            req_lines, subfunction_list = self.generate_subfunction_req_lines(
                candidate_service_list)

            execute_time = 0
            for subfunction in subfunction_list:
                execute_time += subfunction.execute_time
            execute_time += self.config.super.execute_time_margin

            execute_time = random.uniform(
                self.config.super.execute_time[0], self.config.super.execute_time[1])

            tag_code = ', '.join([f'SoPTag("{tag}")' for tag in tags])
            super_function_instance_code = self.SUPER_FUNCTION_INSTANCE_TEMPLATE % (super_service_name,
                                                                                    tag_code,
                                                                                    execute_time,
                                                                                    energy)
            req_lines_code = '\n\t'.join(req_lines)
            super_function_code = self.SUPER_FUNCTION_TEMPLATE % (
                super_service_name, req_lines_code)
            # write_file('./test_config/test.py', super_function_code)

            self.super_service_pool.append(SoPServiceElement(name=super_service_name,
                                                             level=None,
                                                             element_type=SoPElementType.SERVICE,
                                                             tag_list=tags,
                                                             is_super=True,
                                                             energy=energy,
                                                             execute_time=execute_time,
                                                             code=super_function_code,
                                                             instance_code=super_function_instance_code))
        return self.super_service_pool


class SoPThingGenerator(SoPElementGenerator):

    THING_TEMPLATE = '''\
from big_thing_py.big_thing import *

import time
import random
import argparse

%s

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", '-n', action='store', type=str,
                        required=False, default='%s', help="thing name")
    parser.add_argument("--host", '-ip', action='store', type=str,
                        required=False, default='%s', help="host name")
    parser.add_argument("--port", '-p', action='store', type=int,
                        required=False, default=%s, help="port")
    parser.add_argument("--alive_cycle", '-ac', action='store', type=int,
                        required=False, default=%s, help="refresh_cycle")
    parser.add_argument("--refresh_cycle", '-rc', action='store', type=int,
                        required=False, default=%s, help="refresh_cycle")
    parser.add_argument("--append_mac", '-am', action='%s',                         # store_true, store_false
                        required=False, help="append mac address to thing name")
    args, unknown = parser.parse_known_args()
    return args


def main():
    args = arg_parse()
    function_list = \\
        [%s]
    value_list = []
    thing = SoPBigThing(name=args.name, service_list=function_list + value_list,
                        alive_cycle=args.alive_cycle, is_super=False, is_parallel=%s, ip=args.host, port=args.port,
                        ssl_ca_path=None, ssl_enable=None, append_mac_address=False, log_name='%s', log_mode=SoPPrintMode.FULL)
    thing.setup(avahi_enable=False)
    thing.run()


if __name__ == '__main__':
    main()

'''
    SUPER_THING_TEMPLATE = '''\
from big_thing_py.super_thing import *

import argparse


class SoPBasicSuperThing(SoPSuperThing):

    def __init__(self, name: str, service_list: List[SoPService] = ..., alive_cycle: float = 60, is_super: bool = False, is_parallel: bool = True,
                 ip: str = None, port: int = None, ssl_ca_path: str = None, ssl_enable: bool = False, log_name: str = None, log_enable: bool = True, log_mode: SoPPrintMode = SoPPrintMode.ABBR, append_mac_address: bool = True,
                 refresh_cycle: float = 10):
        value_list = []
        function_list = \\
            [%s]

        service_list = value_list + function_list
        super().__init__(name, service_list, alive_cycle, is_super, is_parallel, ip, port,
                         ssl_ca_path, ssl_enable, log_name, log_enable, log_mode, append_mac_address, refresh_cycle)

%s


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", '-n', action='store', type=str,
                        required=False, default='%s', help="thing name")
    parser.add_argument("--host", '-ip', action='store', type=str,
                        required=False, default='%s', help="host name")
    parser.add_argument("--port", '-p', action='store', type=int,
                        required=False, default=%s, help="port")
    parser.add_argument("--alive_cycle", '-ac', action='store', type=int,
                        required=False, default=%s, help="alive cycle")
    parser.add_argument("--refresh_cycle", '-rc', action='store', type=int,
                        required=False, default=%s, help="refresh cycle")
    parser.add_argument("--auto_scan", '-as', action='%s',
                        required=False, help="middleware auto scan enable")
    parser.add_argument("--log", action='store_true',
                        required=False, help="log enable")
    parser.add_argument("--log_mode", action='store',
                        required=False, default=SoPPrintMode.FULL, help="log mode")
    parser.add_argument("--append_mac", '-am', action='store_true',                         # store_true, store_false
                        required=False, help="append mac address to thing name")
    args, unknown = parser.parse_known_args()

    return args


def generate_thing(args):
    super_thing = SoPBasicSuperThing(name=args.name, ip=args.host, port=args.port, is_super=True, is_parallel=%s, ssl_ca_path=None, ssl_enable=None,
                                     alive_cycle=args.alive_cycle, refresh_cycle=args.refresh_cycle, append_mac_address=False, log_name='%s', log_mode=SoPPrintMode.FULL)
    return super_thing


if __name__ == '__main__':
    args = arg_parse()
    thing = generate_thing(args)
    thing.setup(avahi_enable=args.auto_scan)
    thing.run()

'''

    def __init__(self, config: SoPThingConfig = None, middleware_config: SoPMiddlewareConfig = None, service_config: SoPServiceConfig = None) -> None:
        super().__init__(config)

        self.config: SoPThingConfig
        self.middleware_config = middleware_config
        self.service_config = service_config

        self.thing_pool: List[SoPThingElement] = []

        self.super_service_type_num = self.service_config.super.service_type_num
        self.service_per_thing = self.config.base.service_per_thing
        self.super_service_per_thing = self.config.super.service_per_thing
        self.error_rate = self.config.super.error_rate
        self.super_error_rate = self.config.super.error_rate

    def dump(self, simulation_env: SoPMiddlewareElement, service_list: List[SoPServiceElement], base_thing_folder_path: str, remote_base_thing_folder_path: str):
        self.service_list = service_list

        def make_thing_name(index: int, is_fail: bool, middleware: SoPMiddlewareElement):
            middleware_index = '_'.join(
                middleware.name.split('_')[1:])  # levelN_M
            if is_fail:
                name = f'base_thing_fail_{middleware_index}_{index}'
            else:
                name = f'base_thing_{middleware_index}_{index}'.replace(
                    ' ', '_')

            return name

        def dump_recursive(middleware: SoPMiddlewareElement):
            base_thing_num = random.randint(self.middleware_config.base.thing_per_middleware[0],
                                            self.middleware_config.base.thing_per_middleware[1])
            for i in range(base_thing_num):
                is_fail = random.choices([True, False], weights=[
                                         self.config.base.error_rate, 1 - self.config.base.error_rate])[0]
                thing_name = make_thing_name(i, is_fail, middleware)

                picked_service_list = random.sample(self.service_list, k=random.randint(self.service_per_thing[0],
                                                                                        self.service_per_thing[1]))
                if is_fail:
                    service_code = '\n'.join(
                        [SoPServiceGenerator.FAIL_SERVICE_TEMPLATE % (service.name, thing_name) for service in picked_service_list])
                else:
                    service_code = '\n'.join(
                        [service.code for service in picked_service_list])

                service_instance_code = ',\n\t\t'.join(
                    [service.instance_code for service in picked_service_list])
                thing_code = self.THING_TEMPLATE % (service_code,
                                                    thing_name,
                                                    '127.0.0.1',
                                                    1883,
                                                    60,
                                                    60,
                                                    'store_true',
                                                    service_instance_code,
                                                    True,
                                                    f'./log/{thing_name}.log')

                thing = SoPThingElement(name=thing_name,
                                        level=middleware.level,
                                        element_type=SoPElementType.THING,
                                        service_list=picked_service_list,
                                        is_super=False,
                                        alive_cycle=60,
                                        device=middleware.device,
                                        thing_file_path=f'{base_thing_folder_path}/{thing_name}.py',
                                        remote_thing_file_path=f'{remote_base_thing_folder_path}/{thing_name}.py',
                                        code=thing_code)
                for service in thing.service_list:
                    service.level = middleware.level
                middleware.thing_list.append(thing)

            for child_middleware in middleware.child_middleware_list:
                dump_recursive(child_middleware)

        dump_recursive(simulation_env)

    def dump_super(self, super_service_list: List[SoPServiceElement], root_middleware: SoPMiddlewareElement, super_thing_folder_path: str, remote_super_thing_folder_path: str):
        self.super_service_list = super_service_list

        super_thing_num = random.randint(self.middleware_config.super.thing_per_middleware[0],
                                         self.middleware_config.super.thing_per_middleware[1])
        for i in range(super_thing_num):
            middleware_index = '_'.join(
                root_middleware.name.split('_')[1:])  # levelN_M
            super_thing_name = f'super_thing_{middleware_index}_{i}'.replace(
                ' ', '_')

            if self.super_service_type_num < self.super_service_per_thing[0]:
                raise Exception(
                    f'super.service_type_num is less than range of super.service_per_thing: {self.super_service_type_num} < [{self.super_service_per_thing[0]}:{self.super_service_per_thing[1]}]')
            picked_super_service_list = random.sample(self.super_service_list, k=random.randint(self.super_service_per_thing[0],
                                                                                                self.super_service_per_thing[1]))

            super_service_code = append_indent('\n'.join(
                [super_service.code for super_service in picked_super_service_list]).replace('\n', '\t\n')).replace('\t', '    ')
            super_service_instance_code = ',\n\t\t\t'.join(
                [service.instance_code for service in picked_super_service_list])
            super_thing_code = self.SUPER_THING_TEMPLATE % (super_service_instance_code,
                                                            super_service_code,
                                                            super_thing_name,
                                                            '127.0.0.1',
                                                            1883,
                                                            60,
                                                            60,
                                                            'store_true',
                                                            True,
                                                            f'./log/{super_thing_name}.log')
            super_thing = SoPThingElement(name=super_thing_name,
                                          level=root_middleware.level,
                                          element_type=SoPElementType.THING,
                                          service_list=picked_super_service_list,
                                          is_super=True,
                                          alive_cycle=60,
                                          device=root_middleware.device,
                                          thing_file_path=f'{super_thing_folder_path}/{super_thing_name}.py',
                                          remote_thing_file_path=f'{remote_super_thing_folder_path}/{super_thing_name}.py',
                                          code=super_thing_code)
            for service in super_thing.service_list:
                service.level = root_middleware.level
            root_middleware.thing_list.append(super_thing)

    def dump_file(self, root_middleware: SoPMiddlewareElement):

        def dump_file_recursive(middleware: SoPMiddlewareElement):
            for thing in middleware.thing_list:
                write_file(thing.thing_file_path, thing.code)

            for middleware in middleware.child_middleware_list:
                dump_file_recursive(middleware)

        dump_file_recursive(root_middleware)


class SoPScenarioGenerator(SoPElementGenerator):

    SCENARIO_TEMPLATE = '''loop(%s) {
%s}
'''

    def __init__(self, config: SoPScenarioConfig = None, middleware_config: SoPMiddlewareConfig = None) -> None:
        super().__init__(config)

        self.config: SoPScenarioConfig
        self.middleware_config: SoPMiddlewareConfig = middleware_config

        self.scenario_pool: List[SoPScenarioElement] = []
        self.super_scenario_pool: List[SoPScenarioElement] = []

        self.service_per_scenario = self.config.base.service_per_scenario
        self.period_overhead = self.config.base.period_overhead
        self.super_service_per_scenario = self.config.super.service_per_scenario
        self.super_period_overhead = self.config.super.period_overhead

        self.scenario_per_middleware = self.middleware_config.base.scenario_per_middleware
        self.super_scenario_per_middleware = self.middleware_config.super.scenario_per_middleware

    def dump(self, simulation_env: SoPMiddlewareElement):

        def make_scenario_name(index: int, middleware: SoPMiddlewareElement):
            middleware_index = '_'.join(
                middleware.name.split('_')[1:])  # levelN_M
            name = f'base_scenario_{middleware_index}_{index}'.replace(
                ' ', '_')

            return name

        def dump_recursive(middleware: SoPMiddlewareElement):
            whole_service_list: List[SoPServiceElement] = []
            for thing in middleware.thing_list:
                if thing.is_super:
                    continue
                whole_service_list += thing.service_list

            for i in range(random.randint(self.scenario_per_middleware[0], self.scenario_per_middleware[1])):
                while True:
                    service_per_scenario = random.randint(self.service_per_scenario[0],
                                                          self.service_per_scenario[1])
                    if len(whole_service_list) < service_per_scenario:
                        SOPTEST_LOG_DEBUG(
                            f'len(whole_service_list) < service_per_scenario_num: {len(whole_service_list)} < {service_per_scenario}. pick again...', 1)
                    else:
                        break

                picked_service_list: List[SoPServiceElement] = random.sample(
                    whole_service_list, k=service_per_scenario)

                scenario_name = make_scenario_name(i, middleware)
                scenario_service_code = ''
                scenario_period = 0
                for service in picked_service_list:
                    tag_code = f'(#{" #".join([tag for tag in [tag for tag in random.sample(service.tag_list, k=random.randint(1, len(service.tag_list)))]])})'
                    service_line = f'{tag_code}.{service.name}()' + '\n'
                    scenario_service_code += service_line
                    scenario_period += service.execute_time

                scenario_period += random.uniform(
                    self.period_overhead[0], self.period_overhead[1])

                scenario_code = (self.SCENARIO_TEMPLATE % (f'{(scenario_period * 1000):.0f} MSEC',
                                                           append_indent(scenario_service_code.rstrip())))

                scenario = SoPScenarioElement(name=scenario_name,
                                              level=middleware.level,
                                              element_type=SoPElementType.SCENARIO,
                                              service_list=picked_service_list,
                                              period=scenario_period,
                                              code=scenario_code)
                middleware.scenario_list.append(scenario)

            for child_middleware in middleware.child_middleware_list:
                dump_recursive(child_middleware)

        dump_recursive(simulation_env)

    def dump_super(self, middleware: SoPMiddlewareElement):
        self.super_scenario_pool = []
        whole_super_service_list: List[SoPServiceElement] = []
        for thing in middleware.thing_list:
            if not thing.is_super:
                continue
            whole_super_service_list += thing.service_list

        for i in range(random.randint(self.super_scenario_per_middleware[0], self.super_scenario_per_middleware[1])):
            while True:
                super_service_per_scenario = random.randint(self.super_service_per_scenario[0],
                                                            self.super_service_per_scenario[1])
                if len(whole_super_service_list) < super_service_per_scenario:
                    SOPTEST_LOG_DEBUG(
                        f'len(whole_service_list) < service_per_scenario_num: {len(whole_super_service_list)} < {super_service_per_scenario}. pick again...', 1)
                else:
                    break

            # TODO: 가끔식 whole_super_service_list개수 보다 랜덤으로 결정한 super_service_per_scenario수가 더 커서 문제가 되는 경우가 있다.
            picked_super_service_list: List[SoPServiceElement] = random.sample(
                whole_super_service_list, k=super_service_per_scenario)

            middleware_index = '_'.join(
                middleware.name.split('_')[1:])  # levelN_M
            scenario_name = f'super_scenario_{middleware_index}_{i}'
            scenario_service_code = ''
            scenario_period = 0
            for service in picked_super_service_list:
                tag_code = f'(#{" #".join([tag for tag in [tag for tag in random.sample(service.tag_list, k=random.randint(1, len(service.tag_list)))]])})'
                service_line = f'{tag_code}.{service.name}()' + '\n'
                scenario_service_code += service_line
                scenario_period += service.execute_time

            scenario_period += random.uniform(
                self.period_overhead[0], self.period_overhead[1])

            scenario_code = (self.SCENARIO_TEMPLATE % (f'{(scenario_period * 1000):.0f} MSEC',
                                                       append_indent(scenario_service_code.rstrip())))

            scenario = SoPScenarioElement(name=scenario_name,
                                          level=middleware.level,
                                          element_type=SoPElementType.SCENARIO,
                                          service_list=picked_super_service_list,
                                          period=scenario_period,
                                          code=scenario_code)
            middleware.scenario_list.append(scenario)
            self.scenario_pool.append(scenario)
        return self.scenario_pool

    # def dump_file(self, root_middleware: SoPMiddlewareElement):

    #     def dump_file_recursive(middleware: SoPMiddlewareElement):
    #         for scenario in middleware.scenario_list:
    #             write_file(scenario.scenario_file_path, scenario.code)

    #         for middleware in middleware.child_middleware_list:
    #             dump_file_recursive(middleware)

    #     dump_file_recursive(root_middleware)
