# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import os

from baitoolkit.common import file_util, logger_factory, context_manager, type_util
from baitoolkit.common.constant import ConstBase
from baitoolkit.common.context_manager import AppContext
from baitoolkit.common.type_util import Singleton
from baitoolkit.exception.errors import InternalError


class ConfigCenterType(ConstBase):
    Nacos = 'nacos'
    Zookeeper = 'zookeeper'
    Local = 'local'


class ConfigAware(metaclass=Singleton):
    """load app.yml"""

    __logger = logger_factory.get_logger(__name__)

    def __init__(self):
        # set value by parse_app_yaml
        self._app_root_path = None
        self._app_yml_abs_path = None
        self._app_id = None
        self._app_version = None
        self._environment = None
        self._namespace = None
        self._config_center_type = None
        self._config_center_kwargs: dict = None
        self._config_set_ids = None
        # set value by self.reload_config_sets
        self._config_sets: dict = None

    def parse_app_yaml(self, app_root_path, app_yml_abs_path):
        """Read and parse app.yml."""
        self._app_root_path = app_root_path
        self._app_yml_abs_path = app_yml_abs_path
        app_dict = file_util.read_yaml(self._app_yml_abs_path)
        self._app_id = app_dict['app_id']
        self._app_version = app_dict['app_version']
        self._namespace = app_dict['namespace']
        self._environment = app_dict['environment']
        self._config_set_ids = app_dict['config_set_ids']
        self._config_center_type = app_dict.get('config_center_type')
        self._config_center_kwargs = app_dict.get('config_center_kwargs')

    def reload_config_sets(self) -> bool:
        """Read config from config center"""
        getters = {
            ConfigCenterType.Zookeeper: self._read_raw_config_from_zookeeper,
            ConfigCenterType.Nacos: self._read_raw_config_from_nacos,
            ConfigCenterType.Local: self._read_raw_config_from_local
        }
        self._config_sets = None
        config_sets = None
        try:
            config_sets = getters[self._config_center_type](self._config_set_ids)
        except BaseException as e:
            self.__logger.exception(
                f"error of reading config from {self._config_center_type} and try to load from local.e={e}")
            config_sets = getters[ConfigCenterType.Local](self._config_set_ids)
        finally:
            self._update_config_to_local(config_sets)
            self._config_sets = self._post_process_config_sets(config_sets)
        return True

    def initialize_context(self) -> AppContext:
        """init context_manager.Context"""
        context_manager.global_ctx.initialize(self._namespace, self._app_id, self._environment, self._app_version,
                                              self._app_root_path, self._config_sets)
        return context_manager.global_ctx

    def refresh_context(self) -> AppContext:
        """refresh context while config value is changed in config center."""
        context_manager.global_ctx.refresh(self._config_sets)
        return context_manager.global_ctx

    def _post_process_config_sets(self, config_sets):
        for key, raw_value in config_sets.items():
            if raw_value is None:
                raise InternalError(f'no config is found to "{key}" or its content is empty.')
            raw_value = self._replace_variables(raw_value)
            config_sets[key] = self._convert_raw_value(raw_value)
        return config_sets

    def _replace_variables(self, string):
        """Replace variables in raw config string."""
        string = string.replace('{{APP_ROOT_PATH}}', self._app_root_path)
        return string

    def _convert_raw_value(self, string):
        try:
            value = type_util.yaml_to_object(string)
        except Exception as e:
            self.__logger.exception(f'raw config content is not yaml format, try to decode in json format. e={e}')
            try:
                value = type_util.json_to_object(string)
            except BaseException as e:
                self.__logger.exception(f'raw config content is not json format, use raw value instead. e={e}')
                value = string
        return value

    def _read_raw_config_from_nacos(self, config_set_ids) -> dict:
        """Read raw config from nacos"""
        from baitoolkit.database.dbclients import NacosClient
        nacos_client = NacosClient(self._config_center_kwargs)
        config_sets = dict()
        for config_set_id in config_set_ids:
            config_sets[config_set_id] = nacos_client.engine.get_config_set(self._namespace, self._app_id,
                                                                            self._environment, config_set_id)
        return config_sets

    def _read_raw_config_from_zookeeper(self, config_set_ids) -> dict:
        """Read raw config from zookeeper"""
        from baitoolkit.database.dbclients import ZkClient
        zk_client = ZkClient(self._config_center_kwargs)
        # Todo..
        return list()

    def _read_raw_config_from_local(self, config_set_ids):
        """Read config from local"""
        config_sets = dict()
        for config_set_id in config_set_ids:
            fp = self._get_local_config_path(config_set_id)
            config_sets[config_set_id] = file_util.read_file(fp)
        return config_sets

    def _get_local_config_path(self, config_set_id):
        """Get local config absolute path."""
        fp = os.path.join(self._app_root_path, 'configs', self._namespace, self._environment)
        os.makedirs(fp, exist_ok=True)
        fp = os.path.join(fp, '{}.yaml'.format(config_set_id))
        return fp

    def _update_config_to_local(self, config_sets) -> bool:
        """Refresh local config cache"""
        for key, config_set in config_sets.items():
            fp = self._get_local_config_path(key)
            file_util.write_file(fp, config_set)
        return True


__config_aware = ConfigAware()


def initialize_context(run_dir, app_yml_abs_path) -> AppContext:
    """Initialize Context."""
    global __config_aware
    __config_aware.parse_app_yaml(run_dir, app_yml_abs_path)
    __config_aware.reload_config_sets()
    return __config_aware.initialize_context()


def refresh_context() -> AppContext:
    """refresh context while config value is changed in config center."""
    global __config_aware
    return __config_aware.refresh_context()
