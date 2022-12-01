import ast
import inspect
from typing import Any, List, Dict, Set, Tuple

from cinnaroll_internal.infer_func_deps_finder import types
from cinnaroll_internal.infer_func_deps_finder.imports import Import
from cinnaroll_internal.infer_func_deps_finder.types import (
    is_lambda_assignment,
    is_function_or_class_def
)
from cinnaroll_internal.infer_func_deps_finder.shadowed_names import get_shadowed_names


class VariableWithPositionInLine:
    def __init__(self, name: str, start_column: int):
        self.name = name
        self.start_column = start_column
        self.name_length = len(name)


class UsedGlobalVariables:
    def __init__(self, code: str, main_module_members: Dict[str, Any], used_imports: Dict[str, Import]):
        self.code = code
        self.main_module_members = main_module_members
        self.used_imports = used_imports
        self.used_global_var_names: Set[str] = set()

        number_of_lines = len(self.code.splitlines())
        self.used_global_var_locations: List[List[VariableWithPositionInLine]] = [
            [] for _ in range(number_of_lines)
        ]

        self.names, self.locations = self.find_used_global_vars_from_main_with_their_locations()
        self.variables: Dict[str, Any] = {}
        for name in self.names:
            self.variables[name] = main_module_members[name]

    def find_used_global_vars_from_main_with_their_locations(
            self
    ) -> Tuple[Set[str], List[List[VariableWithPositionInLine]]]:
        visited_nodes: Set[ast.AST] = set()

        root = ast.parse(self.code)
        ast.fix_missing_locations(root)

        for node in root.body:
            if not any([is_lambda_assignment(node), is_function_or_class_def(node)]):
                raise RuntimeError(f"Unexpected code node in user-written infer function dependencies: {node}")

            self.add_global_vars(
                node,  # type: ignore
                visited_nodes,
                set()
            )

        for line in self.used_global_var_locations:
            line.sort(key=lambda x: x.start_column)
        return self.used_global_var_names, self.used_global_var_locations

    def add_global_vars(
            self,
            node: types.FunctionOrClassDefOrLambdaType,
            visited_nodes: Set[ast.AST],
            shadowed_names_in_outer_scope: Set[str],
    ) -> None:
        # use a separate variable so that recursive calls don't interfere with each other
        shadowed_names_in_this_scope = get_shadowed_names(node).union(
            shadowed_names_in_outer_scope
        )

        for child_node in ast.walk(node):
            if child_node is node:
                continue
            if child_node in visited_nodes:
                continue
            if is_function_or_class_def(child_node) or isinstance(child_node, ast.Lambda):
                self.add_global_vars(
                    child_node,  # type: ignore
                    visited_nodes,
                    shadowed_names_in_this_scope
                )
            self.add_node_if_is_unshadowed_name(child_node, shadowed_names_in_this_scope)
            visited_nodes.add(child_node)

    def add_node_if_is_unshadowed_name(
            self, node: ast.AST, shadowed_names_in_current_scope: Set[str]
    ) -> None:
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Load):
                if node.id not in shadowed_names_in_current_scope:
                    if self.is_global_variable(node):
                        self.used_global_var_names.add(node.id)
                        self.used_global_var_locations[node.lineno - 1].append(
                            VariableWithPositionInLine(node.id, node.col_offset)
                        )

    def is_global_variable(self, node: ast.Name) -> bool:
        if node.id in self.main_module_members:
            if node.id not in self.used_imports:
                obj = self.main_module_members[node.id]
                if not inspect.isclass(obj) and not inspect.isfunction(obj):
                    return True
        return False
