from typing import Set

from redisopy.base.model import BaseModel
from redisopy.errors import NoSuchIdError


class Model(BaseModel):
    """增删改查, id 自动生成，不要加 id 字段"""

    @classmethod
    def filter(cls, include: Set[str] = None, exclude: Set[str] = None, **kwargs):
        """
        :param include/exclude: can use one
        :param kwargs: filter by field
        :return:
        """
        conn = cls.class_var.conn
        keys = conn.keys(f"{cls.class_var.key_prefix}*")
        res = []
        for key in keys:
            is_match = True
            if include:
                row = conn.hmget(key, include)
            elif exclude:
                sub_keys = cls.class_var.keys - exclude
                row = conn.hmget(key, sub_keys)
            else:
                row = conn.hgetall(key)

            for k, v in kwargs.items():
                if row[k] != v:
                    is_match = False
                    break
            if is_match:
                res.append(cls(**row))
        return res

    @classmethod
    def get_by_id(cls, r_id: int):
        conn = cls.class_var.conn
        key = f"{cls.class_var.key_prefix}{r_id}"
        row = conn.hgetall(key)
        if row:
            return cls(**row)
        else:
            raise NoSuchIdError(f"{cls.class_var.cls_name} No such id: {r_id}")
