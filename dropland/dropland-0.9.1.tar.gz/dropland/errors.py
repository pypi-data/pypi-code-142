from typing import Dict, Optional, Type

from dropland.log import tr


class ErrorDescr:
    _code_classes: Dict[int, Type['ErrorDescr']] = dict()
    _type_classes: Dict[str, Type['ErrorDescr']] = dict()

    code: int
    type: str
    msg: Optional[str] = ''
    tr_key: Optional[str] = ''

    @property
    def message(self):
        if self.tr_key:
            return tr(self.tr_key)
        return tr(self.type, default=self.msg)

    def __repr__(self):
        return f"Error[{self.code}] ({self.type}): \"{self.message}\""

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return self.code

    @property
    def dict(self):
        return dict(code=self.code, type=self.type, message=self.message)

    @classmethod
    def get_by_code(cls, code: int) -> Optional[Type['ErrorDescr']]:
        return cls._code_classes.get(code)

    @classmethod
    def get_by_type(cls, type_: str) -> Optional[Type['ErrorDescr']]:
        return cls._type_classes.get(type_)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._code_classes[cls.code] = cls
        cls._type_classes[cls.type] = cls


def result_or(result, error):
    if callable(result):
        result = result()
    if result:
        return result
    if isinstance(error, Exception):
        if callable(error):
            raise error()
        raise error
    return error
