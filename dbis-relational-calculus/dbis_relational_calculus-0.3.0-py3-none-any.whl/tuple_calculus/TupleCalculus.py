from __future__ import annotations
from abc import ABC, abstractclassmethod

from typeguard import typechecked

import relational_calculus.tuple_calculus as tc


class TupleCalculus:
    @typechecked
    def __init__(self, result: tc.Result, formula: tc.Formula) -> None:
        """
        Parameters
        ----------
        result : Result
            The result that should be returned.
        formula : Formula
            The formula that every result has to satisfy.
        """
        self.result = result
        self.formula = formula

    @typechecked
    def verify(self) -> bool:
        """
        Verify the correctness of the result/formula combination (e.g. one must specify the type of a variable before returning it).

        Returns
        -------
        bool
            True if the result/formula combination is correct, False otherwise.
        """
        assert self.formula is not None
        assert self.result is not None

        check = self.formula.verify()

        # Get Types of return variables
        variables = self.result.all_attributes.union(
            set(self.result.selected_attributes.keys())
        )

        for variable in variables:
            check = check and self.formula.check_variable_legality(variable)

        return check

    @typechecked
    def __repr__(self) -> str:
        return f"\\{{{self.result} \\vert {self.formula}\\}}"

    @typechecked
    def to_sql(self, optimize: bool = True) -> str:
        """
        Convert the domain calculus to a SQL query.

        Parameters
        ----------
        optimize : bool, optional
            If the query should be optimized, by default True

        Returns
        -------
        str
            The SQL query.
        """
        # Get Types of return variables
        variables = self.result.all_attributes.union(
            set(self.result.selected_attributes.keys())
        )

        select_query = ""
        for variable in self.result.all_attributes:
            select_query += f"{variable.name}.*, "
        for variable, value in self.result.selected_attributes.items():
            if isinstance(value, set | list):
                attributes = value
                for attribute in attributes:
                    select_query += f"{variable.name}.{attribute}, "
            else:  # isinstance(value, str)
                attribute = value
                select_query += f"{variable.name}.{attribute}, "

        select_query = select_query[: -len(", ")]

        from_variables = variables
        formula = self.formula
        if optimize:
            formula = formula.optimize()
            if formula is not None:
                if isinstance(formula, tc.Exists):
                    if isinstance(formula.variable, set):
                        from_variables = from_variables.union(formula.variable)
                    else:
                        from_variables.add(formula.variable)
                    formula = formula.children[0]

        from_query = ""
        for variable in from_variables:
            from_query += f"{variable.type} {variable.name}, "
        from_query = from_query[: -len(", ")]

        query = f"SELECT DISTINCT {select_query} FROM {from_query}"

        where_query = None
        if formula is not None:
            where_query = formula.to_sql()

        if where_query is not None and where_query != "":
            query += f" WHERE {where_query}"
        return query
