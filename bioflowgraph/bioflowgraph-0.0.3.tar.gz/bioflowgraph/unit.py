# coding=utf-8

from typing import Mapping
from exuse.extypings import Dict, List
from exuse.expath import filename, exists, dirname, abspath, join
from exuse import exio

from bioflowgraph.const import STDXXX_DIR

from .env import Env

LOADED_UNITS = {}


class Unit:

    def __init__(self, config: Mapping) -> None:
        """
        @param `config` unit config dict.
        """
        ## validate required members in config dict
        # required_keys = ('unit', 'executor', 'params')
        # for rk in required_keys:
        #     if rk not in config:
        #         raise KeyError(f'{rk} not in config')
        ## init
        self.raw: Mapping = config
        self.unit_name: str = self.raw['unit']
        self.input_defs: Mapping = self.raw.get('inputs', {})
        self.output_defs: Mapping = self.raw.get('outputs', {})
        # info of each param
        self.__params: Dict[str, Dict] = None

    #region __ methods

    def __str__(self) -> str:
        return f'Unit<{self.unit_name}>'

    def __parse_param_defs(self):
        "解析参数的原始定义"
        param_defs: List[Dict] = self.raw.get('parameters', self.raw.get('params'))
        if param_defs is None:
            raise f"parameters or params field not found in {self.unit_name} config"

        def set_flag(pd):
            # 参数未提供短标时，如果也未提供长标，则短标为 None，否则用长标填充短标
            # 短标为 None 时表明参数可能是一个位置参数
            if 'flag' not in pd or pd['flag'].strip() == '':
                if 'long_flag' not in pd or pd['long_flag'].strip() == '':
                    pd['flag'] = None
                else:
                    pd['flag'] = pd['long_flag']

        def set_type(pd):
            # type
            # 参数未提供类型时，参数类型为 str
            if 'type' not in pd: pd['type'] = 'str'
            pt = pd['type']

            if pt in ['str', 'string']:
                pd['type'] = 'str'

            elif pt in ['int', 'integer']:
                pd['type'] = 'int'

            # 布尔类型的参数必须提供短标或者长标，因为这个标志需要直接加入参数中
            elif pt in ['bool', 'boolean']:
                if pd['flag'] is None:
                    raise Exception(f'布尔类型的参数必须提供短标或者长标: {pd["name"]}')
                pd['type'] = 'bool'

            elif pt in ('list', 'mflist', 'mvlist'):
                pass

            elif pt == 'choices':
                if 'choices' not in pd or not isinstance(pd['choices'], list):
                    raise Exception(f"`choices` must be provided for choices-type parameter")

            else:
                raise Exception(f'Unit<{self.name}>: Unknown parameter type "{pd["type"]}"')

        params = {}
        stdout_overrided: str = None
        stderr_overrided: str = None

        parsed_param_names = []

        for pd in param_defs:

            assert pd['name'], 'param name cannot be null'
            assert pd['name'].strip(), 'param name cannot be null'
            assert pd['name'] not in parsed_param_names
            parsed_param_names.append(pd['name'])

            set_flag(pd)
            set_type(pd)

            if pd['flag'] == '>':
                if stdout_overrided:
                    raise (f'set {pd["name"]} to STDOUT failed, because stdout '
                           f'has been overrided by {stdout_overrided}')
                stdout_overrided = pd['name']

            if pd['flag'] == '2>':
                if stderr_overrided:
                    raise (f'set {pd["name"]} to STDERR failed, because stderr '
                           f'has been overrided by {stderr_overrided}')
                stderr_overrided = pd['name']

            params[pd['name']] = pd

        if stdout_overrided is None:
            params['STDOUT'] = {'name': 'STDOUT', 'flag': '>', 'type': 'str'}
            self.output_defs['STDOUT'] = '%s/${TaskName}.sh.out' % STDXXX_DIR

        if stderr_overrided is None:
            params['STDERR'] = {'name': 'STDERR', 'flag': '2>', 'type': 'str'}
            self.output_defs['STDERR'] = '%s/${TaskName}.sh.err' % STDXXX_DIR

        return params

    #endregion

    #region properties

    @property
    def name(self):
        return self.unit_name

    @property  # unit 标签
    def tags(self) -> List[str]:
        return self.raw.get('tags', [])

    @property
    def executor(self) -> str:
        return self.raw['executor']

    @property
    def sub_executor(self) -> str:
        return self.raw.get('sub_executor')

    @property  # 拼接执行器和子执行器
    def full_executor(self) -> str:
        """concatenate the executor and sub-executor (if exists)"""
        if self.sub_executor is None:
            return self.executor
        else:
            return f'{self.executor} {self.sub_executor}'

    @property
    def input_ports(self) -> List[str]:
        return list(self.input_defs.keys())

    @property
    def output_ports(self) -> List[str]:
        return list(self.output_defs.keys())

    @property
    def unique_input_port(self) -> str:
        ports = [p for p in self.input_ports if p not in ('STDOUT', 'STDERR')]
        if len(ports) != 1:
            raise Exception("cannot access property 'unique_input_port', "
                            f"because unit '{self.name}' has more than one input ports: "
                            ', '.join(self.input_ports))
        return self.input_ports[0]

    @property
    def unique_output_port(self) -> str:
        ports = [p for p in self.output_ports if p not in ('STDOUT', 'STDERR')]
        if len(ports) != 1:
            raise Exception("cannot access property 'unique_output_port', "
                            f"because unit '{self.name}' has more than one output ports: "
                            ', '.join(self.output_ports))
        return self.output_ports[0]

    @property
    def params(self) -> Dict[str, Dict]:
        "解析后的参数"
        if self.__params is None:
            self.__params = self.__parse_param_defs()
        return self.__params

    #endregion

    def is_input_port(self, key: str) -> bool:
        return key in self.input_ports

    def is_output_port(self, key: str) -> bool:
        return key in self.output_ports

    def get_input_default(self, key: str) -> str:
        if self.is_input_port(key):
            v = self.input_defs[key]
            if v is None or v == '':
                return None
            else:
                return v
        else:
            raise f"{key} is not an input port"

    def get_output_default(self, key: str) -> str:
        if self.is_output_port(key):
            return self.output_defs[key]
        else:
            raise f"{key} is not an output port"


def get_unit(config: Mapping) -> Unit:
    unit_name = config.get('unit', config.get('unit_name'))
    if unit_name is None:
        raise KeyError(f'unit or unit_name not provided in config: {config}')
    config2 = {**config, 'unit': unit_name}

    global LOADED_UNITS
    if unit_name in LOADED_UNITS:
        unit = LOADED_UNITS[unit_name]
    else:
        unit = Unit(config2)
        LOADED_UNITS[unit.unit_name] = unit

    return unit
