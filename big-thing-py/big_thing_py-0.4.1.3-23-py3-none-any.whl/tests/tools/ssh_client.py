from big_thing_py.tests.tools.elements import *

import paramiko


class SoPSSHClient:
    def __init__(self, device: SoPDeviceElement) -> None:
        self.client = paramiko.SSHClient()

        self.device = device
        self.connected = False

        self.device.available_port_list = []

    def update_available_port(self):
        available_ports = list(range(10000, 65535))

        # 사용 중인 포트 목록을 얻음
        command_result: str = self.send_command('netstat -an')
        lines = command_result
        used_ports = []
        for line in lines:
            if 'tcp' in line:
                parts = line.split()
                local_address = parts[3]
                forign_address = parts[4]
                port_status = parts[5]
                if 'TIME_WAIT' == port_status or 'ESTABLISHED' == port_status or 'CONNECTED' == port_status or 'LISTEN' == port_status:
                    local_port = int(local_address.split(':')[-1])
                    used_ports.append(local_port)

        # 사용 중인 포트 목록과 사용 가능한 포트 목록을 비교하여 사용중이지 않은 포트 목록을 생성
        available_ports = [
            port for port in available_ports if port not in used_ports]
        self.device.available_port_list = available_ports

    def get_duplicate_proc_pid(self, proc_name: str, user: str = None,
                               local_ip: str = None, local_port: int = None, foreign_ip: str = None, foreign_port: int = None,
                               args: Union[List[str], str] = ''):

        def get_proc_info():
            netstat_result = None
            ps_ef_result = None

            if not self.connected:
                netstat_result: List[str] = os.popen(
                    f'netstat -nap 2>/dev/null | grep {proc_name}').read().split('\n')
                ps_ef_result: List[str] = os.popen(
                    f'ps -ef 2>/dev/null | grep {proc_name}').read().split('\n')
            else:
                netstat_result: List[str] = self.send_command(
                    f'netstat -nap 2>/dev/null | grep {proc_name}', False)
                ps_ef_result: List[str] = self.send_command(
                    f'ps -ef 2>/dev/null | grep {proc_name}', False)

            return ps_ef_result, netstat_result

        def parse_ps_ef_line(line: str):
            line = line.split()
            if len(line) < 1:
                return False
            else:
                return {
                    'user': line[0],
                    'pid': int(line[1]),
                    'proc_name': line[7].lstrip('./'),
                    'args': line[8:],
                }

        def parse_netstat_line(line: str):
            line = line.split()
            if len(line) < 1 or 'tcp6' in line:
                return False
            elif 'tcp' in line:
                return {
                    'local_ip': line[3].split(':')[0],
                    'local_port': int(line[3].split(':')[1]),
                    'foreign_ip': line[4].split(':')[0],
                    'foreign_port': int(line[4].split(':')[1]) if '*' not in line[4].split(':')[1] else 0,
                    'proc_name': '/'.join(line[6].split('/')[1:]).lstrip('./'),
                    'pid': int(line[6].split('/')[0])
                }

        ps_ef_result, netstat_result = get_proc_info()
        target_pid_list_netstat = []
        target_pid_list_ps_ef = []

        for line in ps_ef_result:
            parse_result = parse_ps_ef_line(line)
            if parse_result:
                proc_name_check = proc_name in parse_result['proc_name'].split(
                    '/')[-1]
                args_check = args in ' '.join(parse_result['args'])
                if proc_name_check and args_check:
                    target_pid_list_ps_ef.append(parse_result['pid'])

        for line in netstat_result:
            parse_result = parse_netstat_line(line)
            if parse_result:
                proc_name_check = proc_name in parse_result['proc_name']

                local_ip_check = local_ip == parse_result['local_ip']
                local_port_check = local_port == parse_result[
                    'local_port'] or local_port == parse_result['foreign_port']
                foreign_ip_check = foreign_ip == parse_result['foreign_ip']
                foreign_port_check = foreign_port == parse_result['foreign_port']

                local_address_check = local_ip_check and local_port_check
                foreign_address_check = foreign_ip_check and foreign_port_check
                address_check = local_address_check or foreign_address_check

                if proc_name_check and address_check:
                    target_pid_list_netstat.append(parse_result['pid'])

        if not proc_name == 'python':
            target_pid_list = list(
                set(target_pid_list_netstat).intersection(target_pid_list_ps_ef))
        else:
            target_pid_list = list(set(target_pid_list_ps_ef))
        return target_pid_list

    def send_command(self, command: Union[List[str], str], ignore_result: bool = False, background: bool = False) -> Union[bool, List[str]]:
        if isinstance(command, str):
            command = [command]

        for item in command:
            if self.connected:
                if background:
                    transport = self._ssh_client.get_transport()
                    channel = transport.open_session()
                    channel.exec_command(item)
                else:
                    try:
                        stdin, stdout, stderr = self._ssh_client.exec_command(
                            item)
                    except Exception as e:
                        # TODO: `Secsh channel 89 open FAILED: open failed: Connect failed` 에러가 발생하여 연결을 다시 수립하는 방식으로 해결
                        # TODO: 그러나 해당 방법이 제대로 된 해결법인지는 잘 모르겠음
                        # 반복적으로 send_command가 실행되면 생기는 것으로 보이나 while문으로 똑같은 명령을 반복했을 때는 문제가 생기지 않고 run_middleware를
                        # 반복적으로 실행하면 문제가 생김

                        # mosquitto, middelware를 실행시킬때 백그라운드로 안 시켜서 ssh 세션을 계속 유지하는 것이 문제였다.

                        SOPTEST_LOG_DEBUG(f'Send_command error: {e}', -1)
                        self._ssh_client.close()
                        self.connected = False
                        self.connect()
                        stdin, stdout, stderr = self._ssh_client.exec_command(
                            item)
                # SOPTEST_LOG_DEBUG(f'command execute -> {item}', 0)
                if ignore_result:
                    return True
                else:
                    stdout_result = stdout.readlines()
                    return [line.strip() for line in stdout_result]
            else:
                result = os.popen(item)
                # SOPTEST_LOG_DEBUG(f'command execute -> {item}', 0)
                if ignore_result:
                    return True
                else:
                    return result.read().split('\n')

    # '/home/thsvkd/Workspace/big-thing-py/big_thing_py/tests/configurable_simulation'
    def send_file(self, local_path: str, remote_path: str):
        if self.connected:
            sftp = self._ssh_client.open_sftp()
            sftp.put(local_path, remote_path)
            sftp.close()
            # self._ssh_client.open_sftp().put(local_path, remote_path)
            # SOPTEST_LOG_DEBUG(f'send file {local_path} -> {remote_path}', 0)
        else:
            SOPTEST_LOG_DEBUG('Connect to host before send file', 1)

    def connect(self) -> paramiko.SSHClient:
        if not self.connected:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            if self.device.host != None and self.device.ssh_port != None and self.device.user != None and self.device.password != None:
                try:
                    self.client.connect(self.device.host, port=self.device.ssh_port,
                                        username=self.device.user.split('/')[-1], password=self.device.password)
                    self._ssh_client = self.client
                    self.connected = True
                except paramiko.SSHException as e:
                    print_error(e)
                    raise e
            else:
                raise SOPTEST_LOG_DEBUG(
                    'Please set the user, host, port, password before connect to ssh host', -1)
        else:
            SOPTEST_LOG_DEBUG('Already connected to host', 1)
            return self.client
