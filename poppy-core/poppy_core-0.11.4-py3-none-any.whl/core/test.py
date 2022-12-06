#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import unittest.mock as mock

from poppy.core.conf import settings
from poppy.pop.scripts import import_module_from_path
from sqlalchemy import (create_engine)
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker

# global application scope. create Session class, engine
Session = sessionmaker()


class TaskTestCase:
    """
    The TaskTestCase class is designed to be overridden in derived classes to create unit tests for tasks.

    Example:
        class TestMyPluginTasks(TaskTestCase):
            def test_task1(self):
                # --- initialize the task ---
                from my_plugin import task1

                self.task = task1()

                # --- create some fake data ---
                # (you can use directly pipeline attributes)

                self.task.pipeline.properties.input_dir = 'my_input_dir'
                self.task.pipeline.properties.output  = 'my_output_dir'

                # (...)

                # --- run the task ---

                self.run_task()

                # --- make assertions ---

                # test the result
                assert self.task.pipeline.properties.result == 'my_result'

                # (...)

            def test_task2(self):
                # --- initialize the task ---
                from my_plugin import task2

                self.task = task2()

                # (...)
    """

    def setUp(self):
        """
        Setup the pipeline before each test
        :return:
        """

        # reset the task
        self._task = None

    def run_task(self):
        if self.task is None:
            raise ValueError('The task has not been initialized')
        else:
            self.task.run()

    @property
    def task(self):
        return self._task

    @task.setter
    def task(self, task):
        # store the task
        self._task = task

        # mock the task to provide access to the pipeline property
        self._task.pipeline = mock.MagicMock()


class CommandTestCase:
    """
    The CommandTestCase class is designed to be overridden in derived classes to create unit tests for commands.

    Example:
        class TestMyPluginCommands(CommandTestCase):
            def test_sub_command1(self):

                # --- create some fake data ---

                value1 = 'value1'
                value2 = 'value2'

                # --- initialize the command ---

                command = ['pop',
                           'my_command',
                           'my_sub_command',
                           '--my_option1', value1,
                           '--my_option2', value2,
                           '--dry-run']

                # --- run the command ---

                self.run_command(command)

                # --- make assertions ---

                # test the result
                assert sorted(['file1', 'file2']) == sorted(os.listdir('my_result_path'))

                # (...)
    """

    # The absolute path to the configuration file used in the database setup
    config_path = None

    # The path to the settings file used in the database setup
    settings_path = None

    # The test database identifier
    database_identifier = None

    def mock_configure_settings(self, module=None, dictionary={}, ignore_pipeline_settings=False):

        # create a mock for the configure method
        def configure(instance, pipeline_settings):

            # ignore the pipeline settings if needed
            if not ignore_pipeline_settings:
                if isinstance(pipeline_settings, dict):
                    instance.from_dict(pipeline_settings)
                else:
                    instance.from_module(pipeline_settings)

            # load custom settings from module
            if module:
                instance.from_module(module)

            # load from dictionary
            if dictionary:
                instance.from_dict(dictionary)

        return configure

    @property
    def settings(self):
        from poppy.core.conf import settings as _settings
        return _settings

    def setup_method(self, method):
        """
        Setup the database before each test
        :return:
        """
        self.setup_database()

        # TODO: handle custom settings
        # using something like @mock.patch('poppy.core.conf.settings.PLUGINS', ['my.plugin1', 'my.plugin2'])
        # TODO: handle custom config

    def teardown_method(self, method):
        self.session.close()

        # rollback - everything that happened with the
        # Session above (including calls to commit())
        # is rolled back.
        self.transaction.rollback()

        # return connection to the Engine
        self.connection.close()

    def generate_url(self, **kwargs):
        """
        Generate the URL of the database from the parameters.
        """
        return '{vendor}://{admin}@{address}/{database}'.format(
            **kwargs
        )

    def load_settings(self):

        if self.settings_path is not None:
            settings_module = import_module_from_path('settings_module', self.settings_path)
        elif os.environ.get('PIPELINE_SETTINGS_FILE', None):
            settings_module = import_module_from_path('settings_module', os.environ['PIPELINE_SETTINGS_FILE'])
        else:
            try:
                import settings as settings_module
            except ModuleNotFoundError:
                # search for settings in the pipeline root dir
                settings_module_path = os.path.join(settings.ROOT_DIRECTORY, 'settings.py')

                if os.path.isfile(settings_module_path):
                    settings_module = import_module_from_path('settings_module', settings_module_path)
                else:
                    raise Exception('No settings file found')

        # update the default settings
        settings.configure(settings_module)

    def load_configuration(self):
        from poppy.core.configuration import Configuration

        if self.config_path is not None:
            self.configuration = Configuration(self.config_path)
        else:
            self.configuration = Configuration(os.getenv('PIPELINE_CONFIG_FILE', None))

        self.configuration.read()

    def setup_database(self):
        """
        Setup the database before the generation of the tested command

        :return:
        """

        # load settings and configuration
        self.load_configuration()
        self.load_settings()

        self.database_identifier = settings.TEST_DATABASE
        database_identifier = getattr(self, 'database_identifier', settings.TEST_DATABASE)

        database_info = list(filter(lambda database: database['identifier'] == database_identifier,
                                    self.configuration['pipeline.databases']))[0]

        url = self.generate_url(**database_info['login_info'])

        self.engine = create_engine(url)

        # connect to the database
        self.connection = self.engine.connect()

        # begin a non-ORM transaction
        self.transaction = self.connection.begin()

        # bind an individual Session to the connection
        self.session = Session(bind=self.connection)

        # start the session in a SAVEPOINT...
        self.session.begin_nested()

        # then each time that SAVEPOINT ends, reopen it
        @event.listens_for(self.session, 'after_transaction_end')
        def restart_savepoint(session, transaction):
            if transaction.nested and not transaction._parent.nested:
                # ensure that state is expired the way
                # session.commit() at the top level normally does
                # (optional step)
                session.expire_all()

                session.begin_nested()

    def mock_create_engine(self, database, *args, **kwargs):
        database.engine = self.engine

    def mock_create_connection(self, database, *args, **kwargs):
        database.db_connection = self.connection

    def mock_session_factory(self):
        return self.session

    def mock_configure(self):
        pass

    def run_command(self, command):
        from poppy.pop.scripts import main as pipeline_main
        # check if the command argument is a list and if it contains the 'pop' keyword
        if not isinstance(command, (list,)):
            try:
                arg_list = command.split()
            except:
                raise TypeError('The command attribute must be a list or a string')
        else:
            arg_list = command

        if next(iter(arg_list), None) != 'pop':
            raise ValueError('The command must start with "pop"')

        # apply mocks on the pipeline main function
        @mock.patch.object(sys, 'argv', arg_list)
        @mock.patch('poppy.core.db.database.Database.scoped_session', new_callable=mock.PropertyMock)
        @mock.patch('poppy.core.db.database.Database.configure', side_effect=self.mock_configure)
        @mock.patch('poppy.core.db.database.Database.create_engine', side_effect=self.mock_create_engine, autospec=True)
        @mock.patch('poppy.core.db.database.Database.create_connection', side_effect=self.mock_create_connection,
                    autospec=True)
        def main(mock_create_connection, mock_create_engine, mock_configure, mock_scoped_session):
            mock_scoped_session.return_value = self.session
            pipeline_main()

        # call the mocked main
        main()
