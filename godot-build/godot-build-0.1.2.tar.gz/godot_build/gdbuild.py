#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Main module."""
from argparse import ArgumentParser
from sys import argv
from sys import exit as sys_exit

from godot_build import godot
from godot_build.config import patch_presets, save_default


def __parse_args() -> dict:
    parser = ArgumentParser("gdbuild", "gdbuild --preset HTML5")
    parser.add_argument("-p",
                        "--path",
                        default="./",
                        type=str,
                        help="path to godot project directory")
    parser.add_argument("-o",
                        "--output",
                        default="./build/game",
                        type=str,
                        help="path to output directory")
    parser.add_argument("--preset",
                        default=None,
                        type=str,
                        help="name of preset")
    parser.add_argument("--pack",
                        default=False,
                        type=bool,
                        help="export pack (*.pck or *.zip)")
    parser.add_argument("--debug",
                        default=False,
                        type=bool,
                        help="export debug build")
    parser.add_argument("--test",
                        default=None,
                        type=str,
                        choices=("internal", "all", "command"),
                        help="run test")
    parser.add_argument("-i",
                        "--init",
                        default=False,
                        action='store_true',
                        help="initialize gdbuild project")
    parser.add_argument("-d",
                        "--download",
                        default=False,
                        action='store_true',
                        help="download engine and templates")
    if len(argv) == 1:
        argv.append("-h")
    return vars(parser.parse_known_args(argv)[0])


def __init_project(path: str):
    save_default(path)


def __test(params: dict):
    test_runner = godot.TestRunner(params["path"])
    if params["test"] == "all":
        test_runner.run_test(godot.TestType.ALL)
    elif params["test"] == "internal":
        test_runner.run_test(godot.TestType.INTERNAL)
    else:
        test_runner.run_test(godot.TestType.COMMAND)


def __build_command(params: dict) -> list:
    command = ["{godot}", "--no-window", "--path", params["path"]]
    export = "--export"
    if params["debug"]:
        export = "--export-debug"
    elif params["pack"]:
        export = "--export-pack"
    command.append(export)
    command.append(f"{params['preset']}")
    command.append(f"{params['output']}")
    return command


def main():
    """Run gdbuild."""
    arguments = __parse_args()
    if not arguments["init"] and arguments["test"] != "internal":
        vers_manager = godot.VersionManager(arguments["path"])
        vers_manager.add_version(vers_manager.config["version"])
    if arguments["test"]:
        __test(arguments)
    elif arguments["init"]:
        __init_project(arguments["path"])
    else:
        if vers_manager.config["custom"]["templates"]:
            patch_presets(arguments["path"], vers_manager.config["version"])
        else:
            patch_presets(arguments["path"], vers_manager.config["version"],
                          True)
        runner = godot.GodotRunner(arguments["path"])
        cmd = __build_command(arguments)
        cmd[0] = runner.format(cmd[0])
        completed = runner.run(cmd)
        if completed.returncode == 0:
            for line in completed.stdout.splitlines():
                print(line)
            print("Export done!")
        else:
            for line in completed.stderr.splitlines():
                print(line)
            sys_exit(1)


if __name__ == "__main__":
    main()
