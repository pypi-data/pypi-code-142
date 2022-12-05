from redisopy.base.field import BaseField
from redisopy.errors import CannotOverwriteError
from redisopy.utils.model_var import ModelClassVar


class ModelMeta(type):

    def __new__(cls, name, bases, attrs):
        attrs["class_var"] = ModelClassVar(cls_name=name, meta=attrs.get("Meta", None))
        for key, value in attrs.items():
            if isinstance(value, BaseField):
                setattr(cls, key, value)
                attrs["class_var"].model_fields[key] = value
                attrs["class_var"].keys.add(key)
        return super().__new__(cls, name, bases, attrs)

    class Meta:
        # key_prefix
        pass


class BaseModel(metaclass=ModelMeta):
    """
    基础操作，主要是实例方法
    @property 标记的都是实例变量
    """
    class_var = None
    _record_id: int = None  # key 中的 id, 如果 model 有 id 字段，那么就是 id 字段的值。
    _key: str = ""  # redis instance key

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"{self.__class__.__name__}{str(self.fields)}"

    def __repr__(self):
        return str(self)

    def save(self, ex: int = 0, is_override: bool = False) -> int:
        if getattr(self, "id", None) and (not is_override):
            if self.class_var.conn.exists(self.key):
                raise CannotOverwriteError("Cannot overwrite the data in redis. If want, set is_override=True")
        self.class_var.conn.hset(self.key, mapping=self.redis_data)
        if ex:
            self.class_var.conn.expire(self.key, ex)
        return self.record_id

    def delete(self):
        self.class_var.conn.delete(self.key)

    @property
    def record_id(self):
        """如果 model 有 id 字段，那么就是 id 字段的值; 否则就通过 _record_id 来生成"""
        db_id = getattr(self, "id", None)
        return db_id if db_id else self._record_id

    @record_id.setter
    def record_id(self, value: int):
        self._record_id = value

    @property
    def key(self) -> str:
        if not self._key:
            prefix = self.class_var.key_prefix
            if self.record_id:
                self._key = f"{prefix}{self.record_id}"
            else:
                keys = self.class_var.conn.keys(f"{prefix}*")
                ids = [int(key.split(":")[-1]) for key in keys]
                self.record_id = max(ids) + 1 if ids else 1
                self._key = f"{prefix}{self.record_id}"
        return self._key

    @property
    def fields(self):
        data = {}
        for k in self.class_var.keys:
            data[k] = getattr(self, k)
        return data

    @property
    def redis_data(self):
        data = {}
        for k, v in self.class_var.model_fields.items():
            data[k] = v.validator.from_py_to_redis(getattr(self, k))
        return data
