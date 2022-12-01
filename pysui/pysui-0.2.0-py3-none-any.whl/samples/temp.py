#    Copyright 2022 Frank V. Castellucci
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#        http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

# -*- coding: utf-8 -*-

"""pysui Package metadata example."""

import argparse
import os
import sys
import pathlib
from typing import Any, Sequence, Union


PROJECT_DIR = pathlib.Path(os.path.dirname(__file__))
PARENT = PROJECT_DIR.parent

sys.path.insert(0, str(PROJECT_DIR))
sys.path.insert(0, str(PARENT))
sys.path.insert(0, str(os.path.join(PARENT, "pysui")))
from pysui.sui import SuiConfig, SuiClient, SuiAddress, GetPackage, GetFunctionArgs
from sui.sui_types import ObjectID, SuiString


class ValidateAddress(argparse.Action):
    """Address validator."""

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = ...,
    ) -> None:
        """Validate."""
        try:
            if isinstance(values, list):
                values = [SuiAddress.from_hex_string(v) for v in values]
            else:
                values = SuiAddress.from_hex_string(values)
        except ValueError:
            parser.error(f"'{values}' is not valid address.")
            sys.exit(-1)
        setattr(namespace, self.dest, values)


def build_parser(in_args: list) -> argparse.Namespace:
    """build_parser Simple command line for app.

    :param in_args: list of argument strings
    :type in_args: list
    :return: Parse results
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(add_help=True, usage="%(prog)s [options] command [--command_options]")
    parser.add_argument("-a", "--address", required=True, help="Package address", action=ValidateAddress)
    return parser.parse_args(in_args if in_args else ["--help"])


def parameter_base_builder(indata: dict) -> str:
    """Recursive."""
    base = None
    match_key = list(indata.keys())[0]
    match match_key:
        case "MutableReference":
            struct_name = indata[match_key]["Struct"]["name"]
            base = f" &mut {struct_name}"
        case "TypeParameter" | "Vector":
            base = f" {match_key}<{indata[match_key]}>"
        case "Reference":
            if "Struct" in indata[match_key]:
                struct_name = indata[match_key]["Struct"]["name"]
            else:
                struct_name = parameter_base_builder(indata[match_key])
            base = f" &{struct_name}"
        case _:
            struct_name = indata[match_key]["name"]
            base = f" &{struct_name}"
    return base


def parameter_to_str(indata: Union[str, dict], last_one: bool = False) -> str:
    """Do it."""
    if isinstance(indata, str):
        return f" {indata}" if last_one else f" {indata},"
    base = parameter_base_builder(indata)
    # match_key = list(indata.keys())[0]
    # match match_key:
    #     case "MutableReference":
    #         struct_name = indata[match_key]["Struct"]["name"]
    #         base = f" &mut {struct_name}"
    #     case "TypeParameter" | "Vector":
    #         base = f" {match_key}<{indata[match_key]}>"
    #     case "Reference":
    #         if "Struct" in indata[match_key]:
    #             struct_name = indata[match_key]["Struct"]["name"]
    #         else:
    #             struct_name = indata[match_key]
    #         base = f" &{struct_name}"
    #     case _:
    #         struct_name = indata[match_key]["name"]
    #         base = f" &{struct_name}"
    return f"{base}" if last_one else f"{base},"


def package(client: SuiClient, args: argparse.Namespace) -> None:
    """package Summarizes package information.

    :param args: Arguments
    :type args: argparse.Namespace
    """
    builder = GetFunctionArgs(
        package="0x4bc57a9dfe1f0b90b3927c11d1aa05be46d17f10",
        module=SuiString("dancer"),
        function=SuiString("add_values"),
    )
    result = client.execute(builder)
    if result.is_ok():
        print(result.result_data.to_json(indent=2))
    else:
        print(result.result_string)
    # builder = GetPackage(args.address)
    # result = client.execute(builder)
    # if result.is_ok():
    #     print("\nModules")
    #     print("-------")
    #     for module_name, module_details in result.result_data.modules.items():
    #         print(module_name)
    #         print(f"\n{module_name} Functions (all)")
    #         for func_name, func_def in module_details.exposed_functions.items():
    #             print(f"  {func_name:<20} entry: {func_def.is_entry!s:5} args: ", end="")
    #             parm_len = len(func_def.parameters)
    #             for index in range(parm_len):
    #                 if index == parm_len - 1:
    #                     print(parameter_to_str(func_def.parameters[index], True))
    #                 else:
    #                     print(parameter_to_str(func_def.parameters[index]), end="")
    #     print()
    # else:
    #     print(f"Error: {result.result_string}")


def main() -> None:
    """Main entry point."""
    arg_line = sys.argv[1:].copy()
    cfg_file = None
    # Handle a different client.yaml than default
    if arg_line and arg_line[0] == "--local":
        cfg_file = arg_line[1:2]
        arg_line = arg_line[2:]
    parsed = build_parser(arg_line)
    if cfg_file:
        cfg = SuiConfig.from_config_file(cfg_file[0])
    else:
        cfg = SuiConfig.default()
    print(f"Using configuration from {cfg.configuration_path}")
    package(SuiClient(cfg), parsed)


if __name__ == "__main__":
    main()
