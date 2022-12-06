from big_thing_py.tests.tools.elements import *
from big_thing_py.tests.tools.event_handler import *
from tabulate import tabulate
import numpy as np
import csv


class SoPSimulator:

    def __init__(self, smulation_file_path: str = None, debug: bool = False) -> None:
        self.smulation_file_path = smulation_file_path
        self.simulation_start_time = None

        self.simulation_event_timeline: List[SoPEvent] = []
        self.simulation_env: SoPMiddlewareElement = None

        self.event_handler = SoPEventHandler()

        self.event_log: List[SoPEvent] = []
        self.debug = debug

        self.load_simulation(self.smulation_file_path)

    def load_simulation(self, smulation_folder_path: str):
        simulation_data = json_file_read(smulation_folder_path)
        self.simulation_env = SoPMiddlewareElement().load(
            simulation_data['component'])
        self.event_timeline_list = simulation_data['event_timeline']

        self.event_handler = SoPEventHandler(
            self.simulation_env, self.event_log, self.simulation_start_time)
        self.event_handler.update_middleware_device_list()
        self.event_handler.init_ssh_client_list()
        self.event_handler.init_mqtt_client_list()
        self.event_handler.event_listener_start()

        self.generate_middleware_file(self.simulation_env)
        self.generate_thing_file(self.simulation_env)

        self.simulation_event_timeline = [SoPEvent(event_type=SoPEventType.get(event['event_type']),
                                                   element=find_element_by_name_recursive(
                                                       self.simulation_env, event['element'])[0],
                                                   timestamp=event['timestamp'],
                                                   duration=event['duration'],
                                                   delay=event['delay']) for event in simulation_data['event_timeline']]

    @exception_wrapper
    def start(self, user_interaction=True):
        self.simulation_start_time = time.time()

        self.event_handler.remove_all_remote_simulation_file()
        self.send_middleware_file(self.simulation_env)
        self.send_thing_file(self.simulation_env)
        self.event_handler.kill_all_simulation_instance()

        for event in self.simulation_event_timeline:
            self.event_handler.event_trigger(event)
            time.sleep(0.1)

        self.event_handler.kill_all_simulation_instance()
        evaluator = SoPEvaluator(self.simulation_env, self.event_log)

        if user_interaction:
            evaluator.print_result()
            evaluator.save_result()
        else:
            evaluator.save_result()

    def generate_middleware_file(self, simulation_env: SoPMiddlewareElement):
        middleware_list: List[SoPMiddlewareElement] = get_middleware_list_recursive(
            simulation_env)
        for middleware in middleware_list:
            middleware.generate_cfg()
            middleware.generate_mosquitto_conf()
            middleware.generate_int_script()

            middleware.middleware_cfg_file_path = f'{os.path.dirname(self.smulation_file_path)}/{os.path.basename(middleware.middleware_config_path)}/{middleware.name}_middleware.cfg'
            middleware.mosquitto_conf_file_path = f'{os.path.dirname(self.smulation_file_path)}/{os.path.basename(middleware.middleware_config_path)}/{middleware.name}_mosquitto.conf'
            middleware.init_script_file_path = f'{os.path.dirname(self.smulation_file_path)}/{os.path.basename(middleware.middleware_config_path)}/{middleware.name}_init.sh'
            middleware.remote_middleware_cfg_file_path = f'{middleware.remote_middleware_config_path}/{middleware.name}_middleware.cfg'
            middleware.remote_mosquitto_conf_file_path = f'{middleware.remote_middleware_config_path}/{middleware.name}_mosquitto.conf'
            middleware.remote_init_script_file_path = f'{middleware.remote_middleware_config_path}/{middleware.name}_init.sh'
            write_file(middleware.middleware_cfg_file_path,
                       middleware.middleware_cfg)
            write_file(middleware.mosquitto_conf_file_path,
                       middleware.mosquitto_conf)
            write_file(middleware.init_script_file_path,
                       middleware.init_script)

    def generate_thing_file(self, simulation_env: SoPMiddlewareElement):
        thing_list: List[SoPThingElement] = get_thing_list_recursive(
            simulation_env)

        for thing in thing_list:
            write_file(
                thing.thing_file_path, thing.code)

    def send_middleware_file(self, simulation_env: SoPMiddlewareElement):
        middleware_list: List[SoPMiddlewareElement] = get_middleware_list_recursive(
            simulation_env)
        for middleware in middleware_list:
            ssh_client = self.event_handler.find_ssh_client(middleware)
            result = ssh_client.send_command(
                [f'mkdir -p {middleware.remote_middleware_config_path}'])
            result = ssh_client.send_file(
                os.path.abspath(middleware.middleware_cfg_file_path), middleware.remote_middleware_cfg_file_path)
            result = ssh_client.send_file(
                os.path.abspath(middleware.mosquitto_conf_file_path), middleware.remote_mosquitto_conf_file_path)
            result = ssh_client.send_file(
                os.path.abspath(middleware.init_script_file_path), middleware.remote_init_script_file_path)

    def send_thing_file(self, simulation_env: SoPMiddlewareElement):
        thing_list: List[SoPThingElement] = get_thing_list_recursive(
            simulation_env)
        for thing in thing_list:
            _, middleware = find_element_recursive(self.simulation_env, thing)
            ssh_client = self.event_handler.find_ssh_client(middleware)
            result = ssh_client.send_command(
                [f'mkdir -p {os.path.dirname(thing.remote_thing_file_path)}'])
            # TODO: 자꾸 OSError가 나는데 이유를 모르겠다
            # result = ssh_client.send_file(
            #     os.path.abspath(thing.thing_file_path), thing.remote_thing_file_path)
            os.system(
                f'sshpass -p "{ssh_client.device.password}" scp -o StrictHostKeyChecking=no -P {ssh_client.device.ssh_port} {os.path.abspath(thing.thing_file_path)} {ssh_client.device.user}@{ssh_client.device.host}:{thing.remote_thing_file_path} > /dev/null 2>&1 &')
            SOPTEST_LOG_DEBUG(
                f'Send file {os.path.basename(thing.thing_file_path)}', 0)


class SoPEvaluator:

    MIDDLEWARE_EVENT = [SoPEventType.MIDDLEWARE_RUN,
                        SoPEventType.MIDDLEWARE_KILL,
                        SoPEventType.THING_REGISTER,
                        SoPEventType.THING_UNREGISTER,
                        SoPEventType.THING_KILL,
                        SoPEventType.FUNCTION_EXECUTE,
                        SoPEventType.SCENARIO_VERIFY,
                        SoPEventType.SCENARIO_ADD,
                        SoPEventType.SCENARIO_RUN,
                        SoPEventType.SCENARIO_STOP,
                        SoPEventType.SCENARIO_UPDATE,
                        SoPEventType.SCENARIO_DELETE,
                        SoPEventType.SUPER_FUNCTION_EXECUTE,
                        SoPEventType.SUPER_SCHEDULE,
                        SoPEventType.SUB_FUNCTION_EXECUTE,
                        SoPEventType.SUB_SCHEDULE]
    THING_EVENT = [SoPEventType.THING_REGISTER,
                   SoPEventType.THING_UNREGISTER,
                   SoPEventType.THING_KILL,
                   SoPEventType.FUNCTION_EXECUTE,
                   SoPEventType.SUPER_FUNCTION_EXECUTE,
                   SoPEventType.SUPER_SCHEDULE]
    SCENARIO_EVENT = [SoPEventType.THING_REGISTER,
                      SoPEventType.THING_UNREGISTER,
                      SoPEventType.THING_KILL,
                      SoPEventType.FUNCTION_EXECUTE,
                      SoPEventType.SUPER_FUNCTION_EXECUTE,
                      SoPEventType.SUPER_SCHEDULE,
                      SoPEventType.SCENARIO_VERIFY,
                      SoPEventType.SCENARIO_ADD,
                      SoPEventType.SCENARIO_RUN,
                      SoPEventType.SCENARIO_STOP,
                      SoPEventType.SCENARIO_UPDATE,
                      SoPEventType.SCENARIO_DELETE]

    def __init__(self, simulation_env: SoPMiddlewareElement, event_log: List[SoPEvent]) -> None:
        self.simulation_env = simulation_env
        self.event_log = event_log

        self.classify_event_log()
        self.evaluate_service()
        self.evaluate_scenario()

    def save_result(self):
        pass

    def print_result(self):
        pass

    def classify_event_log(self):
        for event in self.event_log:
            if event.event_type in SoPEvaluator.MIDDLEWARE_EVENT:
                middleware, _ = find_element_recursive(
                    event.middleware_element)
                middleware: SoPMiddlewareElement
                middleware.event_log.append(event)
            elif event.event_type in SoPEvaluator.THING_EVENT:
                thing, _ = find_element_recursive(event.thing_element)
                thing: SoPThingElement
                thing.event_log.append(event)
            elif event.event_type in SoPEvaluator.SCENARIO_EVENT:
                scenario, _ = find_element_recursive(event.scenario_element)
                scenario: SoPScenarioElement
                scenario.event_log.append(event)

    def evaluate_service():
        def calculate_utilization_and_energy(self):
            self._total_simulation_time = self._event_log[-1].timestamp - \
                self._event_log[0].timestamp

            for middleware in self._middleware_list:
                for thing in middleware._thing_list:
                    for function in thing._function_list:
                        function['utilization'] = function['total_duration'] / \
                            self._total_simulation_time
                        thing._total_energy_consumption += function['total_energy_consumption']

        def calculate_energy_score(self):
            function_energy_info = {}
            for middleware in self._middleware_list:
                for thing in middleware._thing_list:
                    for function in thing._function_list:
                        if function['name'] not in function_energy_info:
                            function_energy_info[function['name']] = [
                                function['energy'], ]
                        else:
                            function_energy_info[function['name']].append(
                                function['energy'])

                score = 0
                cnt = 0
                for event in middleware._event_log:
                    if event.function_name in function_energy_info:
                        energy_list = sorted(
                            function_energy_info[event.function_name])
                        for i, energy in enumerate(energy_list):
                            if energy == event.energy:
                                energy_score = 100 / (i + 1)
                                score += energy_score
                                cnt += 1
                middleware._energy_score = score / cnt

        def calculate_qos_score(self):
            for middleware in self._middleware_list:
                cnt = 0
                execute_event_list = [
                    event for event in middleware._event_log if event.event_type == EventType.FUNCTION_EXECUTE]
                for event in execute_event_list:
                    if event.result == SoPErrorType.NO_ERROR:
                        cnt += 1
                middleware._qos_score = (cnt / len(execute_event_list)) * 100.0

    def evaluate_scenario():

        def find_pattern(event_list: List[EventHolder]):
            for i in range(1, len(event_list)):
                if [event.function_name for event in event_list[:i]] == [event.function_name for event in event_list[i:i+i]]:
                    return event_list[:i]
            return event_list

        def calculate_scenario_cycle_avg(self):
            for middleware in self._middleware_list:
                for scenario in middleware._scenario_list:
                    # capture execute pattern
                    scenario_latency_list = []
                    loop_check = True
                    if 'super' in scenario._name:
                        execute_event_list: List[EventHolder] = [
                            event for event in scenario._event_log if event.event_type in [EventType.SUPER_FUNCTION_EXECUTE]]
                    else:
                        execute_event_list: List[EventHolder] = [
                            event for event in scenario._event_log if event.event_type in [EventType.FUNCTION_EXECUTE]]
                    execute_pattern = find_pattern(execute_event_list)

                    for i in range(0, len(execute_event_list), len(execute_pattern)):
                        if i + len(execute_pattern) - 1 >= len(execute_event_list):
                            break
                        elif not execute_event_list[i + len(execute_pattern) - 1].duration:
                            break

                        cycle_start_time = execute_event_list[i].timestamp
                        cycle_end_time = execute_event_list[i + len(
                            execute_pattern) - 1].timestamp + execute_event_list[i + len(execute_pattern) - 1].duration
                        cycle_duration = cycle_end_time - cycle_start_time

                        if cycle_duration > scenario._period / 1000:
                            loop_check = False
                        scenario_latency_list.append(cycle_duration)

                    scenario._loop_check = loop_check
                    if len(scenario_latency_list) > 0:
                        scenario._avg_latency = sum(
                            scenario_latency_list) / len(scenario_latency_list)
                    else:
                        scenario._avg_latency = 0
                        scenario._loop_check = False
                        SOPTEST_LOG_DEBUG(
                            f'scenario was failed!!!. scenario: {scenario._name}', -1)

    def convert_return_type(self, return_type):
        if return_type.value == -1:
            return_type = 'UNDEFINED'
        else:
            return_type = return_type
        return return_type

    def convert_execute_result(self, execute_result):
        if execute_result.value == 0:
            return 'NO_ERROR'
        elif execute_result.value == -1:
            return 'FAILED'
        elif execute_result.value == -2:
            return 'TIMEOUT'
        elif execute_result.value == -3:
            return 'NO_PARALLEL'
        elif execute_result.value == -4:
            return 'DUPLICATE'
        elif execute_result.value == -5:
            return 'UNDEFINED'

    def print_table(self, table, header, scenario_name: str = None):
        title_filler = '-'
        table = tabulate(table, headers=header, tablefmt='fancy_grid')

        if scenario_name:
            print(
                f"{f' scenario {scenario_name} ':{title_filler}^{len(table.split()[0])}}")
        print(table)

    def print_simulation_result(self, target_middleware: SoPMiddlewareElement, user_interaction: bool):

        def check_service_contain_in_scenario(target_middleware: SoPMiddlewareElement, function_name: str):
            for scenario in target_middleware.scenario_list:
                if f'.{function_name}' in scenario.code:
                    return True

            return False

        def make_service_utilization_table(target_middleware: SoPMiddlewareElement):
            header = ['thing(is_parallel)', 'service(call count)',
                      'energy consumption', 'utilization']
            table = []
            for thing in target_middleware.thing_list:
                for function in thing.service_list:
                    # service_postfix = '*' if not check_service_contain_in_scenario(
                    #     target_middleware, function['name']) else ''
                    service_postfix = ''
                    utilization = function['utilization']
                    call_count = function['call_count']
                    total_energy_consumption = function['total_energy_consumption']
                    if utilization > 0:
                        table.append(
                            [f'{thing.name}({thing._is_parallel})', f"{function['name']}({call_count}){service_postfix}", total_energy_consumption, f'{utilization * 100:.2f}%'])
            return table, header

        def make_scenario_score_table(target_middleware: SoPMiddlewareElement):
            header = ['scenario', 'avg latency', 'period', 'deadline meet']
            table = []
            for scenario in target_middleware.scenario_list:
                table.append(
                    [scenario.name, f'{scenario._avg_latency:.2f}s', f'{(scenario.period / 1000):.2f}s', scenario._loop_check])
            return table, header

        def make_whole_timeline_table(target_middleware: SoPMiddlewareElement):
            header = ['time', 'duration', 'event_type', 'level', 'middleware', 'thing',
                      'service(delay)', 'scenario(period)', 'result', 'return_value', 'return_type']
            table = []
            for event in target_middleware.event_log:
                if event.event_type == SoPEventType.FUNCTION_EXECUTE and not event.duration:
                    continue
                table.append([event.timestamp, event.duration, event.event_type.value, event.level, event.middleware_name,
                              event.thing_name, event.function_name, event.scenario_name, self.convert_execute_result(event.result), event.return_value, self.convert_return_type(event.return_type)])
            return table, header

        while user_interaction:
            print()
            print('0: Service Utilization\n'
                  '1: Scenario Score\n'
                  '2: Whole Timeline\n')
            # print('0: Middleware score\n'
            #       '1: Thing Utilization\n'
            #       '2: Service Utilization\n'
            #       '3: Scenario Score\n'
            #       '4: Whole Timeline\n')
            user_input = input(
                'Select Menu (press \'q\' to select middleware): ')

            if user_input == 'q' or not user_input.isdigit():
                break

            user_input = int(user_input)

            # if user_input == 0:
            #     # print middleware score
            #     print(f'== Middleware {target_middleware._name} Score == ')
            #     header = ['energy_score', 'qos_score']
            #     table = []
            #     for scenario in target_middleware._scenario_list:
            #         table.append([target_middleware._energy_score,
            #                       target_middleware._qos_score])
            #         self.print_table(table, header)
            # elif user_input == 1:
            #     # print thing utilization
            #     print(f'== Thing Utilization ==')
            #     header = ['thing', 'utilization']
            #     table = []
            #     for k, i in target_middleware._thing_utilization_info.items():
            #         table.append([k, f'{i * 100:.2f}%'])
            #     self.print_table(table, header)
            if user_input == 0:
                # print service utilization
                print(f'== Service Utilization ==')
                table, header = make_service_utilization_table(
                    target_middleware)
                self.print_table(table, header)
            elif user_input == 1:
                # print scenario score
                print(f'== Scenario Score ==')
                table, header = make_scenario_score_table(target_middleware)
                self.print_table(table, header)
            elif user_input == 2:
                # print scenario timeline
                print(f'== Whole Timeline ==')
                table, header = make_whole_timeline_table(target_middleware)
                self.print_table(table, header)
        else:
            table = []
            table.append([f'{target_middleware.name}'])
            table.append(['Service Utilization'])
            service_utilization_table, header = make_service_utilization_table(
                target_middleware)
            table.append(header)
            for line in service_utilization_table:
                table.append(line)
            table.append(['Scenario Score'])
            scenario_score_table, header = make_scenario_score_table(
                target_middleware)
            table.append(header)
            for line in scenario_score_table:
                table.append(line)
            table.append(['Whole Timeline'])
            whole_timeline_table, header = make_whole_timeline_table(
                target_middleware)
            table.append(header)
            for line in whole_timeline_table:
                table.append(line)

            return table

    def export_simulation_result(self):
        simulation_result_table = []
        simulation_result_table.append(['middleware name', 'service utilization deviation(local)', 'service duration avg(local)', 'service utilization deviation(super)',
                                        'service duration avg(super)', 'scenario duty ratio(local)', 'scenario success(local)', 'scenario duty ratio(super)', 'scenario success(super)'])
        for middleware in self.simulation_env:
            middleware_result = [middleware.name]

            # export service utilization info
            service_utilization_deviation_table = []
            service_duration_avg_table = []
            super_service_utilization_deviation_table = []
            super_service_duration_avg_table = []
            for thing in middleware.thing_list:
                if thing.is_super:
                    for function in thing.service_list:
                        utilization = function['utilization']
                        duration = function['total_duration'] / \
                            function['call_count'] if function['call_count'] != 0 else 0
                        if utilization > 0:
                            super_service_duration_avg_table.append(duration)
                            super_service_utilization_deviation_table.append(
                                utilization)
                else:
                    for function in thing.service_list:
                        utilization = function['utilization']
                        duration = function['total_duration'] / \
                            function['call_count'] if function['call_count'] != 0 else 0
                        if utilization > 0:
                            service_duration_avg_table.append(duration)
                            service_utilization_deviation_table.append(
                                utilization)

            middleware_result.append(
                np.var(service_utilization_deviation_table) if np.var(service_utilization_deviation_table) != 'nan' else '')
            middleware_result.append(
                np.average(service_duration_avg_table))
            middleware_result.append(np.var(super_service_utilization_deviation_table) if len(
                super_service_utilization_deviation_table) > 0 else '')
            middleware_result.append(np.average(super_service_duration_avg_table) if len(
                super_service_duration_avg_table) > 0 else '')

            # export scenario score info
            scenario_duty_ratio_table = []
            scenario_fail_table = []
            super_scenario_duty_ratio_table = []
            super_scenario_fail_table = []
            for scenario in middleware.scenario_list:
                if scenario._thing_list[0].is_super:
                    super_scenario_duty_ratio_table.append(
                        scenario._avg_latency * 1000 / scenario.period)
                    super_scenario_fail_table.append(scenario._loop_check)
                else:
                    scenario_duty_ratio_table.append(
                        scenario._avg_latency * 1000 / scenario.period)
                    scenario_fail_table.append(scenario._loop_check)

            middleware_result.append(np.average(scenario_duty_ratio_table))
            middleware_result.append(
                False if False in scenario_fail_table else True)
            middleware_result.append('' if (len(super_scenario_duty_ratio_table) == 0) else np.average(
                super_scenario_duty_ratio_table))
            middleware_result.append(
                False if False in super_scenario_fail_table else '' if (len(super_scenario_fail_table) == 0) else True)

            simulation_result_table.append(middleware_result)

            # export whole timeline info
            # whole_timeline_table = []
            # for event in middleware._event_log:
            #     if event.event_type == EventType.FUNCTION_EXECUTE and not event.duration:
            #         continue
            #     whole_timeline_table.append([event.timestamp, event.duration, event.event_type.value, event.level, event.middleware_name,
            #                                  event.thing_name, event.function_name, event.scenario_name, self.convert_execute_result(event.result), event.return_value, self.convert_return_type(event.return_type)])

        csv_file_path = f'{os.path.dirname(self.smulation_folder_path)}/{os.path.basename(self.smulation_folder_path)}_result.csv'
        f = open(csv_file_path, 'w')
        wr = csv.writer(f)
        for row in simulation_result_table:
            print(row)
            wr.writerow(row)

        def cal_avg(simulation_result_table, index):
            return f'{np.average([result[index] for result in simulation_result_table[1:] if result[index] not in [0.0, ""]]):0.5f}'

        def cal_success(simulation_result_table, index):
            return all([result[index] for result in simulation_result_table[1:] if result[index] not in [0.0, ""]])

        simulation_config_name = self.smulation_folder_path.split('/')[-3]

        # ['middleware name', 'service utilization deviation(local)', 'service duration avg(local)', 'service utilization deviation(super)',
        # 'service duration avg(super)', 'scenario duty ratio(local)', 'scenario success(local)', 'scenario duty ratio(super)', 'scenario success(super)'])
        total_service_utilization_deviation_avg = cal_avg(
            simulation_result_table, 1)
        total_service_duration_avg = cal_avg(simulation_result_table, 2)
        total_super_service_utilization_deviation_avg = cal_avg(
            simulation_result_table, 3)
        total_super_service_duration_avg = cal_avg(simulation_result_table, 4)
        total_scenario_duty_ratio_avg = cal_avg(simulation_result_table, 5)
        total_scenario_success = cal_success(simulation_result_table, 6)
        total_super_scenario_duty_ratio_avg = cal_avg(
            simulation_result_table, 7)
        total_super_scenario_success = cal_success(simulation_result_table, 8)
        wr.writerow([])
        wr.writerow(['middleware name', 'total service utilization deviation(local)', 'total service duration avg(local)', 'total service utilization deviation(super)',
                     'total service duration avg(super)', 'total scenario duty ratio(local)', 'total scenario success(local)', 'total scenario duty ratio(super)', 'total scenario success(super)'])
        wr.writerow([simulation_config_name,
                     total_service_utilization_deviation_avg,
                     total_service_duration_avg,
                     total_super_service_utilization_deviation_avg,
                     total_super_service_duration_avg,
                     total_scenario_duty_ratio_avg,
                     total_scenario_success,
                     total_super_scenario_duty_ratio_avg,
                     total_super_scenario_success])
        f.close()
        return csv_file_path

    def show_simulation_result(self, user_interaction: bool = True):
        csv_file_path = self.export_simulation_result()

        while user_interaction:
            for i, middleware in enumerate(self.simulation_env):
                print(f'{i:<2}: {middleware.name}')
            else:
                user_input = int(input('select middleware: ') or -1)

            if user_input == -1:
                print(
                    f'please select correct middleware number. (0 ~ {len(self.simulation_env) - 1})')
            middleware = self.simulation_env[user_input]

            self.print_simulation_result(middleware, user_interaction)
        else:
            f = open(csv_file_path, 'a')
            wr = csv.writer(f)
            wr.writerow([])
            wr.writerow(['==== middleware_results ===='])
            wr.writerow([])

            for middleware in self.simulation_env:
                middleware_result_table = self.print_simulation_result(
                    middleware, user_interaction)
                wr.writerows(middleware_result_table)


if __name__ == '__main__':
    pass
