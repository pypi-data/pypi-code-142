from __future__ import annotations

import datetime
import logging
import re
import typing as t
from collections import defaultdict
from importlib import metadata
from importlib.metadata import EntryPoint
from pathlib import Path
from typing import List

import click
import yaml


# pydevd.settrace(host='localhost', port=5678, stdoutToServer=True, stderrToServer=UnicodeTranslateError,
#                 suspend=False)

class ActionState:
    ACTION_STATE_FILE = Path('actions-state.yaml')

    def __init__(self, path: Path):

        if not path.is_absolute():
            raise Exception(f'State path should be absolute but got {path}')
        if (path / ActionState.ACTION_STATE_FILE).exists():
            with open(path / ActionState.ACTION_STATE_FILE) as f:
                self.__dict__ = yaml.unsafe_load(f)
        self.path = path

    def save(self):
        if not self.path.exists():
            self.path.mkdir(parents=True)
        with open(self.path / ActionState.ACTION_STATE_FILE, 'w') as f:
            f.write(yaml.dump(self.__dict__))


S = t.TypeVar('S', bound=ActionState)


class Action(t.Generic[S]):
    def __init__(self, actions: Actions, state: S):
        self.actions: Actions = actions
        self.state: S = state
        self._setup_logger()

    def _setup_logger(self):
        self.logger = logging.getLogger('Actions.' + self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        log_path: Path = self.state.path / 'logs' / (self.actions.datetime_prefix + '_log.txt')
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(filename=log_path)
        # file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(fmt=Actions.LOG_FMT))
        self.logger.addHandler(file_handler)


class Command(click.Command):
    pass


class Commands(click.MultiCommand):

    def __init__(
            self,
            name: t.Optional[str] = None,
            invoke_without_command: bool = False,
            no_args_is_help: t.Optional[bool] = None,
            subcommand_metavar: t.Optional[str] = None,
            chain: bool = False,
            result_callback: t.Optional[t.Callable[..., t.Any]] = None,
            command_entry_points: t.Optional[t.Dict[str, t.Optional[str]]] = None,
            commands: t.Optional[t.Dict[str, Command]] = None,
            **attrs: t.Any,
    ) -> None:
        super(Commands, self).__init__(name, invoke_without_command, no_args_is_help, subcommand_metavar, chain,
                                       result_callback, **attrs)
        self.commands = commands or {}

        if command_entry_points is None:
            return

            # initialize counters for existing names
        command_name_suffixes: dict[str, int] = defaultdict(int)
        for command_name in self.commands.keys():
            command_name_suffixes[command_name] += 1

        all_entry_points_dict: t.Dict[str, t.List[metadata.EntryPoint]] = metadata.entry_points()

        for action_group in command_entry_points:
            if action_group not in all_entry_points_dict:
                continue

            action_regex: str | None = command_entry_points[action_group]

            entry_points: List[EntryPoint] = all_entry_points_dict[action_group]

            for entry_point in entry_points:
                if action_regex is not None and not re.match(action_regex, entry_point.name):
                    continue
                command: Command = entry_point.load()
                if not isinstance(command, Command):
                    continue

                command_name = entry_point.name

                command_name_suffixes[command_name] += 1
                name_count = command_name_suffixes[command_name]
                if name_count > 1:
                    command_name += '-' + str(name_count)

                self.commands[command_name] = command

    def list_commands(self, ctx: click.Context) -> t.List[str]:
        return sorted(self.commands.keys())

    def get_command(self, ctx: click.Context, cmd_name: str) -> t.Optional[Command]:
        return self.commands[cmd_name]

    def invoke(self, ctx: click.Context) -> t.Any:
        ctx.ensure_object(Actions)
        super(Commands, self).invoke(ctx)


class _ColorFormatter(logging.Formatter):
    FORMATTERS: t.Dict[int, logging.Formatter] = {}

    def __init__(self, name_format: str, message_format: str, date_format: str = None, style='%'):
        super(_ColorFormatter, self).__init__(fmt=message_format, datefmt=date_format)
        _ColorFormatter.FORMATTERS[logging.NOTSET] = logging.Formatter(fmt=f'{name_format}\u001b[37m{message_format}\u001b[0m',
                                                                       style=style)
        _ColorFormatter.FORMATTERS[logging.DEBUG] = logging.Formatter(fmt=f'{name_format}\u001b[37m{message_format}\u001b[0m',
                                                                      style=style)
        _ColorFormatter.FORMATTERS[logging.INFO] = logging.Formatter(fmt=f'{name_format}\u001b[92m{message_format}\u001b[0m',
                                                                     style=style)
        _ColorFormatter.FORMATTERS[logging.WARN] = logging.Formatter(fmt=f'{name_format}\u001b[93m{message_format}\u001b[0m',
                                                                     style=style)
        _ColorFormatter.FORMATTERS[logging.ERROR] = logging.Formatter(fmt=f'{name_format}\u001b[95m{message_format}\u001b[0m',
                                                                      style=style)
        _ColorFormatter.FORMATTERS[logging.CRITICAL] = logging.Formatter(
            fmt='\u001b[91m' + message_format + '\u001b[0m',
            style=style)

    def format(self, record):
        formatter = self.FORMATTERS.get(record.levelno)
        return formatter.format(record)


class Actions:
    LOG_FMT = '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
    # CONSOLE_LOG_FMT = '%(name)s: %(message)s'
    LOG_DATE_FMT = '%Y-%m-%d %H:%M:%S,uuu'

    def __init__(self, actions_home_path: Path = Path.cwd(), log_level: str = 'DEBUG'):
        self.datetime: datetime.datetime = datetime.datetime.now()
        self.actions_home_path: Path = actions_home_path
        self.log_level: str = log_level

        self.actions_home_path.mkdir(parents=True, exist_ok=True)
        self.state: ActionState = ActionState(self.actions_home_path)
        self.action_states: t.Dict[Path, ActionState] = {}

        self._setup_logger()

    def _setup_logger(self):

        self.console_handler: logging.Handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.INFO)
        self.console_handler.formatter = _ColorFormatter(name_format='%(name)s: ', message_format='%(message)s')

        log_path = self.actions_home_path / 'logs' / (self.datetime_prefix + "_log.txt")
        log_path.parent.mkdir(parents=True, exist_ok=True)
        self.file_handler = logging.FileHandler(log_path)
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.formatter = logging.Formatter(fmt=Actions.LOG_FMT)

        self.logger: logging.Logger = logging.getLogger('Actions')
        self.logger.setLevel(self.log_level)
        self.logger.propagate = False
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)

    @property
    def datetime_prefix(self):
        return self.datetime.strftime('%Y.%m.%d_%H.%M.%S')

    def get_action_state(self, path: t.Union[Path, str], state_type=ActionState, create: bool = True):
        if isinstance(path, str):
            path = Path(path)
        if not path.is_absolute():
            path = self.actions_home_path / path
        if path not in self.action_states and create:
            self.action_states[path] = state_type(path.resolve())
        return self.action_states[path]

    def save(self):
        self.state.save()
