class FilterException(Exception):
    def __init__(
        self,
        field_name: str,
        field_value: str,
        message: str
    ):
        self.field_name = field_name
        self.field_value = field_value
        super().__init__(f'{field_name}: {message} with value {field_value}')


class RangeException(Exception):
    pass


class TypeMismatch(Exception):
    pass