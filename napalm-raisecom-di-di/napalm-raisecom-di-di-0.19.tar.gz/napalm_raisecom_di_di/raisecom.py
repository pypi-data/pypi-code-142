"""NAPALM driver for Raisecom"""

from napalm.base import NetworkDriver

import re
import collections
from napalm_raisecom_di_di.utils import to_seconds
from napalm.base.exceptions import ConnectionException
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


class NapalmRaisecomDriver(NetworkDriver):
    platform = 'raisecom_di_di'

    def __init__(self, hostname, username, password, timeout=None, optional_args=None):
        self.device = {
            "device_type": "cisco_ios_telnet",
            "host": hostname,
            "username": username,
            "password": password,
            "secret": "cisco",
        }
        self.hostname = hostname
        self.check_enable_mode()

    def open(self):
        pass

    def close(self):
        pass

    def check_enable_mode(self):
        try:
            with ConnectHandler(**self.device) as telnet:
                telnet.enable()
        except ValueError as e:
            if str(e) == "Failed to enter enable mode. Please ensure you pass the 'secret' argument to ConnectHandler.":
                self.device['secret'] = 'raisecom'

    # def send_show_command(self, device, command, read_timeout=20):
    #     try:
    #         with ConnectHandler(**device) as telnet:
    #             telnet.enable()
    #             command = command[0]
    #             result = telnet.send_command(command, read_timeout=read_timeout)
    #         return result
    #     except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
    #         raise ConnectionException(f"Could not connect to {self.device['host']} - [{error!r}]")

    def send_show_command(self, device, commands, read_timeout=20):
        result = {}
        try:
            with ConnectHandler(**device) as telnet:
                telnet.enable()
                for command in commands:
                    output = telnet.send_command(command, read_timeout=read_timeout)
                    result[command] = output
            return result
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            raise ConnectionException(f"Could not connect to {self.device['host']} - [{error!r}]")


    def send_show_command_onfull(self, device, commands, read_timeout=20):
        result = {}
        try:
            with ConnectHandler(**device) as telnet:
                telnet.enable()
                telnet.send_command('terminal page-break disable')
                for command in commands:
                    output = telnet.send_command(command, read_timeout=read_timeout)
                    result[command] = output
                telnet.send_command('terminal page-break enable')
            return result
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            raise ConnectionException(f"Could not connect to {self.device['host']} - [{error!r}]")

    def get_facts(self):
        """uptime in seconds"""
        commands = self.send_show_command(self.device, ["sh run | i hostname", 'sh ver'])
        try:
            hostname = re.search(r'hostname.*', commands['sh run | i hostname'])
            if hostname:
                hostname = hostname[0].replace('hostname ', '').strip()
            else:
                hostname = ''
            result = commands['sh ver']
            # print('********')
            # print(result)
            # print('********')
            model = re.search(r'Product [N,n]ame: (.+)', result)
            if model:
                model = model[1].strip()
            else:
                model = ''

            serial_number = re.search(r'Serial number: [a-zA-Z0-9]+', result)

            if serial_number:
                serial_number = serial_number[0].replace('Serial number: ', '').strip()
            else:
                serial_number = ''

            os_version = re.search(r'((Soft[W,w]are Version: .+)|(ROS +Version:? .+))', result)

            if os_version:
                os_version = re.sub(r'(Soft[W,w]are Version: )|(ROS +Version:? )', '', os_version[0]).strip()
            else:
                os_version = ''

            uptime = re.search(r'uptime is .+', result)

            if uptime:
                uptime = uptime[0].replace('uptime is ', '')
                uptime = uptime.replace(' ', '').replace(',', '').replace('days', 'd').replace('hours', 'h').replace(
                    'minutes',
                    'm')
                uptime = to_seconds(uptime)
            else:
                uptime = ''

            return {
                'hostname': hostname,
                'model': model,
                'vendor': 'Raisecom',
                'os_version': os_version,
                'serial_number': serial_number,
                'uptime': uptime,
            }
        except Exception as e:
            return {'error': str(e)}

    def get_environment(self):
        try:
            # environment = {
            #     'fans': {},
            #     'temperature': {},
            #     'power': {},
            #     'cpu': {},
            #     'memory': {
            #         'available_ram': 0,
            #         'used_ram': 0,
            #     },
            # }
            environment = {
                'cpu': {},
                'memory': {
                    'available_ram': {},
                    'used_ram': {},
                },
            }
            # commands = ['sh cpu-utilization', 'sh process cpu']
            #
            # for command in commands:
            #     cpu = self.send_show_command(self.device, [command])
            #     try:
            #         cpu = re.search('Last +5 seconds* CPU utilization: *(\d+)', cpu)[1].strip()
            #         environment['cpu']['Last 5 second'] = {'%usage': cpu}
            #         if cpu:
            #             break
            #     except Exception as e:
            #         continue
            commands = self.send_show_command(self.device, ['sh cpu-utilization', 'show memory'])
            try:
                cpu = commands['sh cpu-utilization']
                cpu = re.search('Last +5 seconds* CPU utilization: *(\d+)', cpu)[1].strip()
                environment['cpu']['Last 5 second'] = {'%usage': cpu}
            except Exception as e:
                environment['cpu'] = {}

            try:
                memory = commands['show memory']
                free_memory = re.search('MemFree', memory)
                if free_memory:
                    memory_full = re.split('\n', memory)
                    list_value = re.split(' +', memory_full[8])
                    environment['memory'] = {'available_ram': list_value[1] + ' kb', 'used_ram': list_value[2] + ' kb'}

                else:
                    free_memory = re.search('free\s+(\d+)', memory)[1].strip()
                    available_ram = str(int(free_memory)//1024)  # Вывод в байтах, переводим в килобайты
                    try:
                        used_ram = re.search('The Memory utilization:\s*([0-9.]+)', memory)[1].strip()

                    except Exception:
                        used_ram = None

                    environment['memory'] = {'available_ram': available_ram + ' kb', 'used_ram': used_ram + '%'}
            except Exception as e:
                environment['memory'] = {}

            return environment
        except Exception as e:
            pass

    def get_lldp_neighbors_detail(self):
        try:
            headlines = {'port': None,
                         'chassisid': None,
                         'portid': None,
                         'sysname': None,
                         'mgtaddress': None
                         }

            response_lldp_command = self.send_show_command_onfull(self.device, ["sh lldp remote"])["sh lldp remote"]

            lldp_full = re.split('\n', response_lldp_command)
            lldp = lldp_full[0].split()

            for i in range(len(lldp)):
                try:
                    headlines[lldp[i].lower()] = i
                except KeyError:
                    continue

            res_dict = collections.defaultdict(list)
            for i in lldp_full[2:]:
                i = re.split(' {3,}', i)

                for _ in [1]:
                    name_port = re.search('GE(\d+\/\d+\/\d+)', i[headlines['port']])
                    if name_port:
                        name_port = 'gigaethernet ' + name_port[1]
                        break

                    name_port = re.search('port(\d+)', i[headlines['port']])

                    if name_port:
                        name_port = 'port ' + name_port[1]
                        break

                    name_port = re.search('P(\d+)', i[headlines['port']])

                    if name_port:
                        name_port = 'port ' + name_port[1]
                        break

                    name_port = i[headlines['port']]

                res_dict[name_port].append({
                    'parent_interface': 'None',
                    'remote_chassis_id': i[headlines['chassisid']],
                    'remote_port': i[headlines['portid']],
                    'remote_port_description': i[headlines['mgtaddress']],
                    'remote_system_capab': '',
                    'remote_system_description': '',
                    'remote_system_enable_capab': '',
                    'remote_system_name': i[headlines['sysname']].replace('.', '_')
                }
                )
            return dict(res_dict)

        except Exception as e:
            return {'error': str(e)}

    def get_interfaces(self):
        try:
            interfaces_command = self.send_show_command_onfull(self.device, ["sh run | i nterface"], read_timeout=60)["sh run | i nterface"]

            # print('**************************')
            # print(interfaces_command)
            # print('**************************')

            interfaces = re.sub('!.+', '', interfaces_command)
            interfaces = re.findall('[i,I]nterface.+', interfaces)
            interfaces = list(map(lambda x: ' '.join(x.split()[1:]), interfaces))

            return interfaces
        except Exception as e:
            return {'error': str(e)}

    def get_config(self):
        try:
            configs = {'running': '', 'candidate': '', 'startup': ''}
            config_command = self.send_show_command_onfull(self.device, ["sh run"], read_timeout=200)['sh run']
            configs['running'] = config_command
            return configs

        except Exception as e:
            return {'error': str(e)}
