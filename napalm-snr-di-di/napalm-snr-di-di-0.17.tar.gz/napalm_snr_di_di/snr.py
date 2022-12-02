"""NAPALM driver for Raisecom"""

from napalm.base import NetworkDriver

import re
import collections
from napalm_snr_di_di.utils import to_seconds
from napalm.base.exceptions import ConnectionException
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


class NapalmSnrDriver(NetworkDriver):
    platform = 'snr_di_di'

    def __init__(self, hostname, username, password, timeout=None, optional_args=None):
        self.device = {
            "device_type": "cisco_ios_telnet",
            "host": hostname,
            "username": username,
            "password": password,
            "secret": "cisco",
        }
        self.hostname = hostname

    def open(self):
        pass

    def close(self):
        pass

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
                telnet.send_command('terminal length 0')
                for command in commands:
                    output = telnet.send_command(command, read_timeout=read_timeout)
                    result[command] = output
            return result
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            raise ConnectionException(f"Could not connect to {self.device['host']} - [{error!r}]")

    def get_facts(self):
        """uptime in seconds"""
        commands = self.send_show_command(self.device, ["sh run | i hostname", 'sh ver'])
        try:
            hostname = commands['sh run | i hostname']
            hostname = re.search(r'hostname(.+)', hostname)
            if hostname:
                hostname = hostname[1].strip()
            else:
                hostname = ''

            result = commands['sh ver']
            # print('********')
            # print(result)
            # print('********')

            model = re.search(r'(SNR.+) Device', result)
            if model:
                model = model[1].strip()
            else:
                model = ''

            serial_number = re.search(r'Serial No\.:([a-zA-Z0-9]+)', result)

            if serial_number:
                serial_number = serial_number[1].strip()
            else:
                serial_number = ''

            os_version = re.search(r'Soft[W,w]are Version (.+)', result)

            if os_version:
                os_version = os_version[1].strip()
            else:
                os_version = ''

            uptime = re.search(r'Uptime is (.+)', result)

            if uptime:
                uptime = uptime[1].strip()
                uptime = uptime.replace(' ', '').replace(',', '').replace('days', 'd').replace('hours', 'h').replace(
                    'minutes', 'm').replace('weeks', 'w')
                uptime = to_seconds(uptime)
            else:
                uptime = ''

            return {
                'hostname': hostname,
                'model': model,
                'vendor': 'SNR',
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
            commands = self.send_show_command(self.device, ["sh cpu utilization", "sh memory usage"])

            try:
                cpu = commands['sh cpu utilization']
                cpu = re.search('Last +5 second CPU USAGE: *(\d+)', cpu)[1].strip()
                environment['cpu']['Last 5 second'] = {'%usage': cpu}
            except Exception as e:
                environment['cpu'] = {}

            try:
                memory = commands['sh memory usage']
                memory_free = re.search('free\s+(\d+)', memory)[1].strip()
                memory_free = str(int(memory_free) //1024)

                memory_usage = re.search('usage is\s+(\d+)', memory)[1].strip()

            except Exception as e:
                memory_free = None

            environment['memory'] = {'available_ram': memory_free + ' kb', 'used_ram': memory_usage + '%'}

            return environment
        except Exception as e:
            pass

    def get_lldp_neighbors_detail(self):
        try:
            response_lldp_command = self.send_show_command_onfull(self.device, ["sh lld neighbors brief"])[
                "sh lld neighbors brief"]
            lldp_full = re.split('\n', response_lldp_command)

            res_dict = collections.defaultdict(list)
            for i in lldp_full[2:]:
                i = re.split(' {1,}', i)
                if i == ['']:
                    continue

                name_port = i[0]

                res_dict[name_port].append({
                    'parent_interface': 'None',
                    'remote_chassis_id': i[1],
                    'remote_port': i[3],
                    'remote_port_description': i[4],
                    'remote_system_capab': '',
                    'remote_system_description': '',
                    'remote_system_enable_capab': '',
                    'remote_system_name': i[6].replace('.', '_')
                }
                )
            return dict(res_dict)

        except Exception as e:
            return {'error': str(e)}

    def get_interfaces(self):
        try:
            interfaces_command = self.send_show_command_onfull(self.device, ["sh run | i nterface"], read_timeout=60)[
                "sh run | i nterface"]

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
            config_command = self.send_show_command_onfull(self.device, ["sh run"], read_timeout=200)["sh run"]
            configs['running'] = config_command
            return configs

        except Exception as e:
            return {'error': str(e)}
