# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from copy import deepcopy

from baitoolkit.common import logger_factory
from baitoolkit.common.constant import ConstBase
from baitoolkit.common.type_util import Singleton
from baitoolkit.database.dbclient_manager import DBClientManager
from baitoolkit.exception import assert_util
from baitoolkit.exception.errors import InternalError
from baitoolkit.parallel import mutex

"""
The global attributes holder.
"""


class ConfigSetId(ConstBase):
    logging = 'logging'
    web = 'web'
    gunicorn = 'gunicorn'
    database = 'database'
    other = 'other'


class AppContext(object, metaclass=Singleton):

    def __init__(self):
        self._namespace = None
        self._app_id = None
        self._environment = None
        self._app_version = None
        self._app_root_path = None
        self._db_client_manager = None
        self._config_sets = None
        self._arbitrary = dict()
        self.__initialized = False
        self.__lock = mutex.create_lock()

    def initialize(self, namespace, app_id, environment, app_version, app_root_path, config_sets: dict):
        """Should be called while starting and only initialized once."""
        assert_util.assert_required(namespace, 'namespace')
        assert_util.assert_required(app_id, 'app_id')
        assert_util.assert_required(environment, 'environment')
        assert_util.assert_required(app_version, 'app_version')
        assert_util.assert_required(app_root_path, 'app_root_path')
        assert_util.assert_required(config_sets, 'config_sets')
        try:
            self.__lock.acquire()
            if self.__initialized:
                raise InternalError('initialized was called before.')
            self._namespace = namespace
            self._app_id = app_id
            self._environment = environment
            self._app_version = app_version
            self._app_root_path = app_root_path
            self.refresh(config_sets)
            self.__initialized = True
        finally:
            self.__lock.release()
        return True

    @property
    def app_id(self):
        return self._app_id

    @property
    def app_version(self):
        return self._app_version

    @property
    def environment(self):
        return self._environment

    @property
    def app_root_path(self):
        return self._app_root_path

    @property
    def namespace(self):
        return self._namespace

    @property
    def db_client_manager(self) -> DBClientManager:
        """Get DBClientManager object. if No db client config set is found, return None."""
        return self._db_client_manager


    @property
    def arbitrary(self) -> dict:
        """Store arbitrary attributes."""
        return self._arbitrary

    def get_config_value(self, config_set_id, item_id=None):
        """Return the config set of config_set_id"""
        config_set = self._config_sets[config_set_id]
        return config_set.get(item_id) if item_id is not None else config_set

    def get_web_config_value(self, item_id=None):
        """Return web config item value."""
        config_set_id = ConfigSetId.web
        return self.get_config_value(config_set_id, item_id=item_id)

    def get_database_config_value(self, item_id=None):
        """Return database config item value."""
        config_set_id = ConfigSetId.database
        return self.get_config_value(config_set_id, item_id=item_id)

    def get_gunicorn_config_value(self, item_id=None):
        """Return gunicorn config item value."""
        config_set_id = ConfigSetId.gunicorn
        return self.get_config_value(config_set_id, item_id=item_id)

    def get_scheduler_config_value(self, item_id=None):
        """Return scheduler config item value."""
        config_set_id = ConfigSetId.scheduler
        return self.get_config_value(config_set_id, item_id=item_id)

    def get_other_config_value(self, item_id=None):
        """Return other config item value."""
        config_set_id = ConfigSetId.other
        return self.get_config_value(config_set_id, item_id=item_id)

    def refresh(self, config_sets: dict) -> bool:
        self._config_sets = config_sets
        self._db_client_manager = self._refresh_db_clients(config_sets.get(ConfigSetId.database))
        self._refresh_logging(config_sets.get(ConfigSetId.logging))
        return True

    @staticmethod
    def _refresh_db_clients(database_config_sets) -> DBClientManager:
        if database_config_sets is None:
            return None
        db_client_manager = DBClientManager()
        for key, config_set in database_config_sets.items():
            client_name = config_set['client_name']
            config = deepcopy(config_set)
            del config['client_name']
            db_client_manager.add_db_client(key, client_name, config)
        return db_client_manager


    @staticmethod
    def _refresh_logging(logging_config_set):
        logger_factory.dict_config(logging_config_set, attach_pid=True)


global_ctx = AppContext()
