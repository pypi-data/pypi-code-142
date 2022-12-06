# When loading data from a table we
# - determine the Pydantic instance to use
# - determine the model to use
# - do an "update_or_create" on the model

import importlib
from datetime import datetime
from pathlib import Path
from types import ModuleType
from typing import Iterator, Type, Union

import pytz
from django.db import models
from pydantic import BaseModel

from mdb_codegen.djaccess import AccessTableNames, PNDSAccessTableNames
from mdb_codegen.jsontools import FieldRenamer, NamerProto
from mdb_codegen.mdbtools import AccessDatabase, AccessTable


def _get_pk(model: Type[models.Model]) -> models.Field:
    for field in model._meta.fields:
        if getattr(field, "primary_key", False) is True:
            return field
    raise KeyError("No primary key?")


class ModelUpdater:
    def __init__(
        self,
        app_label: str,
        table_renamer: Type[AccessTableNames] = AccessTableNames,
        field_namer: Type[NamerProto] = FieldRenamer,
    ):
        self.table_renamer: AccessTableNames = table_renamer()
        self.field_namer: FieldRenamer = field_namer()
        self.models_: ModuleType = importlib.import_module(f"{app_label}.models")
        self.base_models_: ModuleType = importlib.import_module(f"{app_label}.base_models")

    def update_from_table(self, table: AccessTable):
        django_model: models.Model = getattr(self.models_, self.table_renamer.model(table))
        pydantic_base_model: BaseModel = getattr(self.base_models_, self.table_renamer.base_model(table))

        # List the current primary keys. Anything NOT in the list needs
        # to be created.

        # Fields to be updated are everything except for PK

        update_fields = [f for f in django_model._meta.fields if not f.primary_key]

        qs: models.QuerySet = django_model.objects
        # A Generator returning django model instances

        # This should have worked but I encountered a Django SQL bug where
        # db_column attributes were not taken into account
        # for the "ON_CONFLICT" clause!
        # qs.bulk_create(instances, update_conflicts=True,
        #     update_fields=[f.name for f in update_fields],
        #     unique_fields=[f.name for f in unique_fields]
        # )

        # So instead we do an UPDATE and then a CREATE
        # While generating the models, we need to handle "naive" datetimes

        pydantic_instances = [
            pydantic_base_model.parse_raw(json.replace(b"1900-01-00", b"1900-01-01")) for json in table.json()
        ]
        for instance in pydantic_instances:
            for attribute_key, attribute_value in instance:
                # Hacky approach to timezonify times
                if isinstance(attribute_value, datetime):
                    setattr(instance, attribute_key, pytz.utc.localize(attribute_value))

        django_pk = _get_pk(django_model).name
        database_primary_keys = set(qs.values_list("pk", flat=True))

        create: Iterator[django_model] = (
            django_model(**{i: j for i, j in instance})
            for instance in pydantic_instances
            if getattr(instance, django_pk) not in database_primary_keys
        )
        update: Iterator[django_model] = (
            django_model(**{i: j for i, j in instance})
            for instance in pydantic_instances
            if getattr(instance, django_pk) in database_primary_keys
        )

        print(table)
        qs.bulk_create(create, batch_size=100)
        print("created")
        qs.bulk_update(update, batch_size=100, fields=[f.name for f in update_fields])
        print("updated")

    def __call__(self, target: Union[AccessDatabase, AccessTable]):
        if isinstance(target, AccessTable):
            self.update_from_table(target)
        elif isinstance(target, AccessDatabase):
            for table in target.tables.values():
                self.__call__(table)
        elif isinstance(target, Path):
            self.__call__(AccessDatabase(target))
        else:
            raise TypeError("Expected either a Table or a Database instance")


class PndsModelUpdater(ModelUpdater):
    def __init__(self):
        super().__init__(app_label="pnds_data", table_renamer=PNDSAccessTableNames)

    def __call__(self, target=AccessDatabase(Path.home() / "PNDS_Interim_MIS-Data.accdb")):
        super().__call__(target=target)
