import os
import pathlib

import asyncpg

from jija_orm import config
from jija_orm import exceptions


class JijaORM:
    APPS = None
    CONNECTION = None
    PROJECT_DIR = None

    def __init__(self, *, apps=None, connection=None, project_dir=None):
        self.__set_params(apps=apps, connection=connection, project_dir=project_dir)

        for app in JijaORM.APPS:
            app.check(JijaORM.PROJECT_DIR)
            app.load()

        JijaORM.CONNECTION.check()

    @classmethod
    async def async_init(cls, *, apps=None, connection=None, project_dir=None):
        cls.__set_params(apps=apps, connection=connection, project_dir=project_dir)

        for app in JijaORM.APPS:
            app.check(JijaORM.PROJECT_DIR)
            await app.async_load()

        await JijaORM.CONNECTION.async_check()

    @classmethod
    def __set_params(cls, *, apps, connection, project_dir):
        JijaORM.APPS = cls.__validate_apps(apps)
        JijaORM.CONNECTION = cls.__validate_connection(connection)
        JijaORM.PROJECT_DIR = project_dir or pathlib.Path(os.getcwd())

    @staticmethod
    def __validate_apps(apps):
        if not apps:
            return []

        if not isinstance(apps, (list, tuple)):
            raise exceptions.JijaORMConfigTypeError(apps=apps)

        for app in apps:
            if not isinstance(app, config.App):
                raise exceptions.JijaORMConfigTypeError(app=app)

        return apps

    @staticmethod
    def __validate_connection(connection):
        if not isinstance(connection, config.Connection):
            raise exceptions.JijaORMConfigTypeError(connection=connection)

        return connection

    @classmethod
    async def get_connection(cls) -> asyncpg.connection.Connection:
        return await cls.CONNECTION.get_connection()

    @classmethod
    def get_models(cls) -> dict[str, list]:
        models = {}

        for app in cls.APPS:
            models[app.name] = list(app.models.values())

        return models

    @classmethod
    def get_migrations_dir(cls, app_name):
        for app in cls.APPS:
            if app.name == app_name:
                return app.migrations_dir

        raise AttributeError(app)

    @classmethod
    def get_migrations(cls) -> dict[str, list]:
        migrations = {}

        for app in cls.APPS:
            migrations[app.name] = app.get_migrations()

        return migrations

    @classmethod
    def get_apps_names(cls) -> list[str]:
        return list(map(lambda app: app.name, cls.APPS))
