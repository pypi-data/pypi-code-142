import abc
import enum
from typing import TypeVar

from IPython.core.display import HTML
from bs4 import BeautifulSoup
from pydantic.main import ModelMetaclass


class Explanation(abc.ABC):
    ...


Exp = TypeVar("Exp", bound=Explanation)


class HTMLExplanation(HTML, Explanation):
    ...


class ExplainableMeta(abc.ABCMeta):
    @abc.abstractmethod
    def get_explanation(cls) -> Explanation:
        ...


class ExplainableModelMeta(ModelMetaclass, ExplainableMeta, abc.ABC):
    ...


class Explainable(abc.ABC):
    @abc.abstractmethod
    def get_explanation(self) -> Explanation:
        ...


class DescriptiveEnumMeta(enum.EnumMeta, ExplainableMeta):
    def get_explanation(cls) -> Explanation:
        return cls

    def __repr__(cls):
        space = " " * 3
        delimiter = ",\n" + space
        sorted_members = sorted(cls._member_names_)
        return f"<{cls.__name__}(\n{space}{delimiter.join(sorted_members)}\n)>"

    @property
    def soup(cls) -> BeautifulSoup:
        return BeautifulSoup("<ul>" + "".join([f"<li>{m}</li>" for m in sorted(cls._member_names_)]) + "</ul>")


class DescriptiveEnum(enum.Enum, metaclass=DescriptiveEnumMeta):
    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
