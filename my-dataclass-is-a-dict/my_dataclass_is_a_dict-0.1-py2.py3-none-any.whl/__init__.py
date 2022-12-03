""" dunder init file for the my_dataclass_is_a_dict """


from .dict_mixin import DictionaryMixin

_ = DictionaryMixin  # prevent linter warning (not-used)

__all__ = ["DictionaryMixin"]
