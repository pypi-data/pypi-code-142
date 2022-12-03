from dataclasses import dataclass, fields, field, is_dataclass


def _get_children_status(class_name, item):
    status = []
    if is_dataclass(item):
        if item.empty_status:
            return [f'{class_name} -> {item.empty_status}']
        else:
            return [f'{class_name} -> {x}' for x in item.children_status]

    if type(item) is list:
        for sub_item in item:
            status.extend(
                _get_children_status(class_name, sub_item)
            )

    return status


@dataclass
class EmptyClass:
    def __post_init__(self):
        self.class_name = self._set_class_name()
        self.empty_status = self._check_is_empty()
        self.children_status = self._check_children_status()

    @classmethod
    def _set_class_name(cls) -> str:
        return cls.__name__

    def _iterate_over(self):
        class_fields = [x for x in fields(self.__class__)
                        if x not in ['class_name', 'empty_status', 'children_status']]
        for class_field in class_fields:
            item = getattr(self, class_field.name)
            yield item

    def _check_is_empty(self) -> None | str:
        for item in self._iterate_over():
            if item:
                return None
        return f'{self.class_name} is empty!'

    def _check_children_status(self) -> (bool, list):
        children_status = []
        for item in self._iterate_over():
            children_status.extend(
                _get_children_status(self.class_name, item)
            )

        return children_status


