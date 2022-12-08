import discord
from discord.ext import commands
import asyncio

global bots


class Start(discord.Client):
    def __init__(self, prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None, **options):
        global bots
        self.prefix = prefix
        self.case_insensitive = case_insensitive
        self.intented = intents
        self._help_command = help_command
        self._clients = ''
        self.intent = ''
        self._activity = activity
        if "all" in self.intented:
            self.intent = discord.Intents.all()
        elif "default" in self.intented:
            self.intent = discord.Intents.default()
        else:
            self.intent = discord.Intents.default()
        if "message" in self.intented:
            self.intent.message_content = True
        if "members" in self.intented:
            self.intent.members = True
        if "presences" in self.intented:
            self.intent.presences = True

        if self._activity is None:
            self._clients = commands.Bot(command_prefix=self.prefix, case_insensitive=self.case_insensitive, intents=self.intent,
                                         help_command=self._help_command)
            bots = self._clients


        else:
            self._clients = commands.Bot(command_prefix=self.prefix, case_insensitive=self.case_insensitive, intents=self.intent,
                                         activity=self._activity,
                                         help_command=self._help_command)
            bots = self._clients
        super().__init__(intents=self.intent)

    def run(self, token: str):
        global bots
        bots.run(token)

    # Random Functions here for testing
    async def wait(self, ctx, types: str, check=None, timer=60, everyone: bool = False):
        global bots
        timeout = "ASYNCIO TIMEOUT ERROR"
        if check is None:
            try:
                if everyone is False:
                    def check(msg):
                        if msg.author == ctx.author:
                            return True

                    return await bots.wait_for(types.lower(), check=check, timeout=timer)
                else:
                    return await bots.wait_for(types.lower(), timeout=timer)
            except asyncio.TimeoutError:
                raise TimeoutError(timeout)
        else:
            try:
                return await bots.wait_for(types.lower(), check=check, timeout=timer)
            except asyncio.TimeoutError:
                return TimeoutError(timeout)

    @property
    def clients(self):
        return self._clients


class Events:
    global bots

    ########################################
    #              EVENTS                  #
    ########################################
    # Wrapping the original Coroutine into our own functions that'll make them into decorators
    # The functions then aren't limited to the name of the event

    # Application Commands
    def onApplicationCommand(self, Func):
        @bots.event
        async def on_application_command(*args, **kwargs):
            Func(*args, **kwargs)

        return Func

    def onApplicationCommandComplete(self, Func):
        @bots.event
        async def on_application_command_completion(*args, **kwargs):
            Func(*args, **kwargs)

        return Func

    def onApplicationCommandError(self, Func):
        @bots.event
        async def on_application_command_error(*args, **kwargs):
            Func(*args, **kwargs)

        return Func

    # AutoMod

    def onAutoModRuleCreate(self, Func):
        @bots.event
        async def on_auto_moderation_rule_create(*args, **kwargs):
            Func(*args, **kwargs)

        return Func

    def onAutoModRuleUpdate(self, Func):
        @bots.event
        async def on_auto_moderation_rule_update(*args, **kwargs):
            Func(*args, **kwargs)

        return Func

    def onAutoModRuleDelete(self, Func):
        @bots.event
        async def on_auto_moderation_rule_update(*args, **kwargs):
            Func(*args, **kwargs)

        return Func

    def onReady(self, Func):
        global bots

        @bots.event
        async def on_ready(*args, **kwargs):
            Func(*args, **kwargs)

        return Func

    def onMessage(self, Func):
        global bots

        @bots.event
        async def on_message(*args, **kwargs):
            Func(*args, **kwargs)

        return Func


def Bot(prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None):
    l = Start(prefix, case_insensitive, intents, activity, help_command)
    working = l.clients
    return working
