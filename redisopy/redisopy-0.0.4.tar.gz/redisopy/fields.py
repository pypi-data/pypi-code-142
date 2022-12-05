from redisopy.base.field import BaseField
from redisopy.utils.alias import ForkDatetime


class BooleanField(BaseField):
    field_type = bool


class StringField(BaseField):
    field_type = str


class IntField(BaseField):
    field_type = int


class FloatField(BaseField):
    field_type = float


class DatetimeField(BaseField):
    field_type = ForkDatetime
