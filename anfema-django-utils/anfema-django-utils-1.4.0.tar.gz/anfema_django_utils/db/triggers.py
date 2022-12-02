import contextlib
import warnings

import django
from django.core.exceptions import ValidationError
from django.db import DEFAULT_DB_ALIAS, NotSupportedError
from django.db.models.constraints import BaseConstraint
from django.utils.translation import gettext_lazy as _


if django.VERSION < (4, 1):
    warnings.warn(f"{__name__}.DenyFieldUpdateTrigger requires django v4.1+")


class DenyFieldUpdateTrigger(BaseConstraint):
    """Creates a database trigger to deny any updates to the specified field.

    Add it like any other `Constraint` to `Meta.constraints`.

    Implemented as constraint to get automatic support for (vendor specific)
    sql in migrations and automatic model validation.

    Supports the `postgresql` and `mysql` backends.
    """

    default_trigger_error_message = _("Direct update of “%(field)s” is forbidden.")

    def __init__(self, field, name, violation_error_message=None, trigger_error_message=None):
        super().__init__(name, violation_error_message=violation_error_message)
        if not field:
            raise ValueError(f"{self.__class__.__qualname__}.field must be set.")
        self.field = field
        if trigger_error_message is not None:
            self.trigger_error_message = trigger_error_message
        else:
            self.trigger_error_message = self.default_trigger_error_message

    def _validate_field_name(self, model):
        if self.field not in [f.attname for f in model._meta.concrete_fields]:
            raise ValueError(f"{self.field} is not a concrete field of {model.__name__}.")

    def constraint_sql(self, model, schema_editor):
        self._validate_field_name(model)
        # we can't embed the trigger sql into the "CREATE TABLE" statement
        warnings.warn(
            f"{self.__class__.__qualname__} doesn't support the {schema_editor.connection.vendor} backend. "
            "Skipping creation of triggers."
        )

    def create_sql(self, model, schema_editor) -> str:
        self._validate_field_name(model)
        name = schema_editor.quote_name(self.name)
        field = schema_editor.quote_name(self.field)
        table = schema_editor.quote_name(model._meta.db_table)
        error_message = schema_editor.quote_value(self.trigger_error_message % {"field": self.field})

        if schema_editor.connection.vendor == "postgresql":
            return f"""
                CREATE FUNCTION {name}() RETURNS trigger
                   LANGUAGE plpgsql AS
                $$BEGIN
                   RAISE EXCEPTION {error_message};
                END;$$;

                CREATE TRIGGER {name}
                   BEFORE UPDATE OF {field} ON {table}
                   FOR EACH ROW
                   WHEN (OLD.{field} != NEW.{field})
                   EXECUTE PROCEDURE {name}();
               """
        elif schema_editor.connection.vendor == "mysql":
            return f"""
                CREATE TRIGGER {name}
                    BEFORE UPDATE ON {table}
                    FOR EACH ROW
                    BEGIN
                        IF OLD.{field} <> NEW.{field} THEN
                            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = {error_message};
                        END IF;
                    END;
                """

        raise NotSupportedError(
            f"{self.__class__.__qualname__} doesn't support the {schema_editor.connection.vendor} backend."
        )

    def remove_sql(self, model, schema_editor) -> str:
        self._validate_field_name(model)
        name = schema_editor.quote_name(self.name)
        table = schema_editor.quote_name(model._meta.db_table)

        if schema_editor.connection.vendor == "postgresql":
            return f"""
                DROP TRIGGER {name} ON {table};
                DROP FUNCTION {name}();
                """
        elif schema_editor.connection.vendor == "mysql":
            return f"""
                DROP TRIGGER {name};
                """

        raise NotSupportedError(
            f"{self.__class__.__qualname__} doesn't support the {schema_editor.connection.vendor} backend."
        )

    def validate(self, model, instance, exclude=None, using=DEFAULT_DB_ALIAS) -> None:
        if instance.pk is None:
            return

        if exclude and self.field in exclude:
            return

        queryset = model._default_manager.using(using)

        with contextlib.suppress(model.DoesNotExist):
            db_instance = queryset.get(pk=instance.pk)
            old_value = getattr(db_instance, self.field)
            new_value = getattr(instance, self.field)
            if new_value != old_value:
                raise ValidationError(self.get_violation_error_message())

    def deconstruct(self):
        path, args, kwargs = super().deconstruct()
        kwargs["field"] = self.field
        if self.trigger_error_message is not None and self.trigger_error_message != self.default_trigger_error_message:
            kwargs["trigger_error_message"] = self.trigger_error_message
        return path, args, kwargs

    def __repr__(self):
        return f"<{self.__class__.__qualname__}: field={repr(self.field)}>"

    def __eq__(self, other):
        if isinstance(other, DenyFieldUpdateTrigger):
            return (
                self.name == other.name
                and self.field == other.field
                and self.violation_error_message == other.violation_error_message
                and self.trigger_error_message == other.trigger_error_message
            )
        return super().__eq__(other)
