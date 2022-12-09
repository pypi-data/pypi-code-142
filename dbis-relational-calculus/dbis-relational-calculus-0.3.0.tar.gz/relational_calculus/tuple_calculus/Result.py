from __future__ import annotations
from abc import ABC, abstractclassmethod

from typeguard import typechecked

import relational_calculus.tuple_calculus as tc


class Result:
    @typechecked
    def __init__(
        self,
        all_attributes: set[tc.Variable],
        selected_attributes: dict[tc.Variable, str | set[str] | list[str]],
    ) -> None:
        """
        Parameters
        ----------
        all_attribute : set[Variable]
            Return variables, from which all attributes are returned.
        selected_attributes : dict[Variable, str | set[str] | list[str]]
            Return variables, from which only a selection of attributes are returned.
        """
        self.all_attributes = all_attributes
        self.selected_attributes = selected_attributes
        self.verify()

    def verify(self) -> bool:
        # no variable (name) can be in all_attributes and selected_attributes
        if (
            len(
                [
                    key.name
                    for key in self.selected_attributes.keys()
                    if key.name in [variable.name for variable in self.all_attributes]
                ]
            )
            != 0
        ):
            raise Exception(
                "Cannot return both all attributes and only a selection of attibutes from a variable."
            )

        # attribute selection for each variable cannot be empty
        for key, val in self.selected_attributes.items():
            if isinstance(val, set | list):
                if len(val) == 0:
                    raise Exception(
                        f"The attribute selection for variable {key.name} cannot be empty."
                    )

        # CONDITION: must return something
        if len(self.all_attributes.union(set(self.selected_attributes.keys()))) == 0:
            raise Exception("Result must contain some keys.")

        return True

    @typechecked
    def __repr__(self) -> str:
        output = "["
        for variable in self.all_attributes:
            output += f"\\text{{{variable.name}}}, "
        for variable, value in self.selected_attributes.items():
            if isinstance(value, str):
                attribute = value
                output += f"\\text{{{variable.name}.{attribute}}}, "
            elif isinstance(value, list) or isinstance(value, set):
                attributes = value
                for attribute in attributes:
                    output += f"\\text{{{variable.name}.{attribute}}}, "
            else:
                raise Exception(
                    "The selected attributes must consist of a variable and either a attribute as a string or a list of attributes each as a string!"
                )
        output = output[: -len(", ")]
        output += "]"
        return output
