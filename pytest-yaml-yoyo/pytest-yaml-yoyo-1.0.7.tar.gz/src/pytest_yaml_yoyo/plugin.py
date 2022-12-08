import types
import yaml
from pathlib import Path
from _pytest.python import Module
import pytest
from requests.adapters import HTTPAdapter
from . import http_session
from . import runner
from datetime import datetime


@pytest.fixture(scope="session")
def requests_session():
    """全局session 全部用例仅执行一次"""
    s = http_session.HttpSession()
    # max_retries=2 重试2次
    s.mount('http://', HTTPAdapter(max_retries=2))
    s.mount('https://', HTTPAdapter(max_retries=2))
    yield s
    s.close()


@pytest.fixture()
def requests_function():
    """用例级别 session， 每个用例都会执行一次"""
    s = http_session.HttpSession()
    # max_retries=2 重试2次
    s.mount('http://', HTTPAdapter(max_retries=2))
    s.mount('https://', HTTPAdapter(max_retries=2))
    yield s
    s.close()


@pytest.fixture(scope="module")
def requests_module():
    """模块级别 session， 每个模块仅执行一次"""
    s = http_session.HttpSession()
    # max_retries=2 重试2次
    s.mount('http://', HTTPAdapter(max_retries=2))
    s.mount('https://', HTTPAdapter(max_retries=2))
    yield s
    s.close()


def pytest_collect_file(file_path: Path, parent):  # noqa
    if file_path.suffix == ".yml" and file_path.name.startswith("test"):
        py_module = Module.from_parent(parent, path=file_path)
        # 动态创建 module
        module = types.ModuleType(file_path.stem)
        # 解析 yaml 内容
        raw_dict = yaml.safe_load(file_path.open(encoding='utf-8'))
        # 用例名称test_开头
        run = runner.RunYaml(raw_dict, module)
        run.run()  # 执行用例
        # 重写属性
        py_module._getobj = lambda: module  # noqa
        return py_module


def pytest_generate_tests(metafunc):  # noqa
    """测试用例参数化功能实现"""
    if hasattr(metafunc.module, 'params_data'):
        params_data = getattr(metafunc.module, 'params_data')
        params_len = 0    # 参数化 参数的个数
        if isinstance(params_data, list):
            if isinstance(params_data[0], list):
                params_len = len(params_data[0])
            elif isinstance(params_data[0], dict):
                params_len = len(params_data[0].keys())
            else:
                params_len = 1
        params_args = metafunc.fixturenames[-params_len:]
        metafunc.parametrize(
            params_args,
            params_data,
            scope="function"
        )


def pytest_configure(config):
    """配置日志文件和格式
    :param config:
        日志文件位置: log_file = ./xx.log
        日志文件等级: log_file_level = info
        日志文件格式: log_file_format = %(asctime)s %(filename)s:%(lineno)s [%(levelname)s]: %(message)s
        日志日期格式: log_file_date_format = %Y-%m-%d %H:%M:%S
    :return:
    """
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    # log_file default log file name
    if not config.getini('log_file') and not config.getoption('log_file'):
        config.option.log_file = Path(config.rootdir).joinpath('logs', f'{current_time }.log')
    if not config.getini('log_file_level') and not config.getoption('log_file_level'):
        config.option.log_file_level = "info"
    if config.getini('log_file_format') == '%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s' \
            and not config.getoption('log_file_format'):
        config.option.log_file_format = "%(asctime)s [%(levelname)s]: %(message)s"
    if config.getini('log_file_date_format') == '%H:%M:%S' and not config.getoption('log_file_date_format'):
        config.option.log_file_date_format = "%Y-%m-%d %H:%M:%S"
    # 设置 日志文件在控制台的输出格式
    if not config.getini('log_cli_format') and not config.getoption('log_cli_format'):
        config.option.log_cli_format = '%(asctime)s [%(levelname)s]: %(message)s'
    if not config.getini('log_cli_date_format') and not config.getoption('log_cli_date_format'):
        config.option.log_cli_date_format = '%Y-%m-%d %H:%M:%S'
