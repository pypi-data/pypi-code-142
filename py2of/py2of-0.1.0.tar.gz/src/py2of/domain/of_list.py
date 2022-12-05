from dataclasses import dataclass
from typing import List

from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_vector import OfVector


@dataclass()
class OfList:
    name: str
    elements: List[int | float | OfVector | OfTensor]

    def __str__(self) -> str:
        string = f"{self.name}"
        string += f"\tList<{self.element_type}>\n{len(self)}\n(\n"
        for i in self.elements:
            string += f"{i}\n"
        string += ");"
        return string

    def __len__(self) -> int:
        return len(self.elements)

    @property
    def element_type(self) -> str:
        python_element_type = type(
            self.elements[0]
        )  # TODO: make sure all the elements are the same type (__post_init___?)
        if python_element_type == int or python_element_type == float:
            return "scalar"
        elif python_element_type == OfVector:
            return "vector"
        elif python_element_type == OfTensor:
            return "tensor"
        else:
            raise TypeError()
