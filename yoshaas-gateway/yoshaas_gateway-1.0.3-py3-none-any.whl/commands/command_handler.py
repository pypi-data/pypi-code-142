from __future__ import annotations

import asyncio
import threading
from inspect import signature
from typing import Callable

from .command_context import CommandContext
from discord_gateway import GatewayBot, GatewayMessage

import logging as log


__all__ = (
    'CommandsBot',
)


class CommandsBot(GatewayBot):
    def __init__(self, *args, command_prefix: str, case_sensitivity: bool = False,
                 notify_errors: bool = False, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.case_sensitivity = case_sensitivity
        self.prefix = command_prefix
        self.__commands: dict = {}
        self.add_listener(self.message_listener, event='message_create', type='default')
        self.notify_errors = notify_errors

    async def message_listener(self, msg: GatewayMessage) -> None:
        """
        Default on_message_create,\n
        register messages as commands\n
        :param msg: :class:`GatewayMessage`
            The message to check for
        """
        if not msg.data.content.startswith(self.prefix) or not msg.data.__dict__.get('guild_id', False) or \
                msg.data.author['id'] == self.user.id:
            return
        self.register_commands(CommandContext(msg.data, self.api))

    def command(self, aliases: list = ()) -> Callable[[{__name__}], None]:
        """
        **Decorator**\n
        Used to assign a function with a command\n
        :param aliases: :class:`list[str]`
            Aliases for the given command
        :return: :class:`Callable[[{__name__}], None]`
            The nested function
        """

        def decorator(command: Callable) -> None:
            """
            **Nested Decorator**\n
            Takes a function and assign with a command\n
            :param command: :class:`Callable`
                The function to assign
            """
            self.__commands[command.__name__] = command
            for alias in aliases:
                self.__commands[str(alias)] = command

        return decorator

    def register_commands(self, msg: CommandContext) -> None:
        """
        Checks for available assigned commands\n
        if true:\n
        \tExecutes the commands\n
        if false:\n
        \tIgnores or raises an error depends on your settings\n
        :param msg: :class:`CommandContext`
            The command, data
        """
        command_name = msg.content.replace(self.prefix, '', 1).split(' ')[0]
        if command_name in self.__commands:
            func = self.__commands[command_name]
            sig = signature(func).parameters
            if not any([sign.kind == sign.VAR_POSITIONAL for sign in sig.values()]):
                non_default = filter(lambda sign: sign.default is sign.empty, sig.values())
                args = msg.content.split(' ')[1:len(sig)]
                if len(list(non_default)) - 1 > len(args):
                    print(f'Error: Command {command_name} missing required arguments')
                    return
            else:
                args = msg.content.replace(self.prefix, '', 1).split(' ')[1:]
            log.info(f'running command: {command_name}({", ".join(args)})')
            args = [str(sign) if sign.annotation is sign.empty else sign.annotation(arg) for arg, sign in
                    zip(args, list(sig.values())[1:])]
            threading.Thread(target=asyncio.run, args=(func(msg, *args),)).start()
        elif self.notify_errors:
            print(f'Warning: Unknown command {command_name}')
