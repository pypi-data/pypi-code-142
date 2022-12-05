import inspect

import pendulum


class TypeValidator(object):
    """Validate/Convert that the value is of the correct type."""

    def __init__(self, t):
        self.type = t

    def from_redis_to_py(self, value):
        func_name = inspect.currentframe().f_code.co_name
        func = getattr(self, f'{func_name}_{self.type.__name__}')
        return func(value)

    def from_py_to_redis(self, value):
        func_name = inspect.currentframe().f_code.co_name
        func = getattr(self, f'{func_name}_{self.type.__name__}')
        return func(value)

    # 具体类型函数
    def from_py_to_redis_float(self, value):
        return str(value)

    def from_py_to_redis_int(self, value):
        return str(value)

    def from_py_to_redis_str(self, value):
        return str(value)

    def from_py_to_redis_bool(self, value):
        return '1' if value else ''

    def from_py_to_redis_fork_datetime(self, value):
        return value.in_timezone('UTC').format('YYYY-MM-DD HH:mm:ss')

    def from_redis_to_py_float(self, value):
        return float(value)

    def from_redis_to_py_int(self, value):
        return int(value)

    def from_redis_to_py_str(self, value):
        return str(value)

    def from_redis_to_py_bool(self, value):
        return bool(value)

    def from_redis_to_py_fork_datetime(self, value):
        if isinstance(value, pendulum.DateTime):
            return value.in_tz('UTC')
        return pendulum.parse(value, strict=False, tz='UTC')
