import discord
from discord.ext import commands
import asyncio
global bots


def Bot(prefix: str, case_insensitive: bool = False, intents: tuple = ("default",), activity=None, help_command=None):
    if "all" in intents:
        intent = discord.Intents.all()
    elif "default" in intents:
        intent = discord.Intents.default()
    else:
        intent = discord.Intents.default()
        if "message" in intents:
            intent.message_content = True
        if "members" in intents:
            intent.members = True
        if "presences" in intents:
            intent.presences = True

    if activity is None:
        clients = commands.Bot(command_prefix=prefix, case_insensitive=case_insensitive, intents=intent, help_command=help_command)
    else:
        clients = commands.Bot(command_prefix=prefix, case_insensitive=case_insensitive, intents=intent, activity=activity, help_command=help_command)
    return clients


def run(bot, token: str, startMessage: str = None, intents: str = "all"):
    global bots
    bots = bot

    @bot.event
    async def on_ready():
        if startMessage is None:
            return
        else:
            if "None" in startMessage:
                startMessage1 = startMessage.replace("None", str(bot.user.name))
                print(startMessage1)
                return
            else:
                print(startMessage)
                return
    bot.run(token)


# Random Functions here for testing
async def wait(ctx, types: str, check=None, timer=60, everyone: bool = False):
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
