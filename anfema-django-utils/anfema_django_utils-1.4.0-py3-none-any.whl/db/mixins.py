from typing import Any, Dict, Iterable, Tuple

from django.db import models
from django.db.models.signals import post_init
from django.dispatch import receiver


LoadedFieldValues = Dict[str, Any]
ChangedFieldValues = Dict[str, Tuple[Any, Any]]


class ChangedFieldValuesMixinBase:
    _loaded_values: LoadedFieldValues

    @property
    def changed_field_values(self) -> ChangedFieldValues:
        changes = {}
        for field_name, old_value in getattr(self, '_loaded_values', {}).items():
            new_value = getattr(self, field_name)
            if old_value != new_value:
                changes[field_name] = (old_value, new_value)
        return changes


class ChangedFieldValuesModelMixin(ChangedFieldValuesMixinBase):
    """Mixin to keep track of changed field values.

    All changes (since loading the model from the database) are available
    in the `changed_field_values` property. The property contains a mapping
    where the key is the changed field name and the value a tuple of the old
    and new field value.

    To just check if a field was changed use the `in` operator:
    >>> 'field_name' in self.changed_field_values
    """

    @classmethod
    def from_db(cls, db, field_names, values) -> models.Model:
        instance = super().from_db(db, field_names, values)
        instance._loaded_values = dict(zip(field_names, values))
        return instance


class SnapshotFieldValuesModelMixin(ChangedFieldValuesMixinBase):
    """Mixin to keep track of changed field values based on snapshots.

    Field value snapshots are created whenever a model instance is initialized.
    This happens on model initialization, creation or `refresh_from_db` calls for example.

    To manually create a field value snapshot, call the :meth:`snapshot_field_values` method.

    Only concrete (and non-deferred) field values are captured currently, for foreign keys
    for example only the `<fk_field>_id` key is present.
    """

    @property
    def current_field_value_snapshot(self) -> LoadedFieldValues:
        return self._loaded_values.copy()

    def snapshot_field_values(self, field_names: Iterable[str] = None) -> None:
        if field_names is None:
            field_names = [f.attname for f in self._meta.concrete_fields if f.attname not in self.get_deferred_fields()]
        self._loaded_values = {field_name: getattr(self, field_name) for field_name in field_names}


@receiver(post_init)
def snapshot_field_values(sender: Any, instance: SnapshotFieldValuesModelMixin, *args, **kwargs):
    if isinstance(instance, SnapshotFieldValuesModelMixin):
        instance.snapshot_field_values()
