import discord
from discord.ext import commands


def getTextChannel(ID: discord.TextChannel) -> discord.TextChannel:
    return ID


def textChannelName(ID: discord.TextChannel) -> discord.TextChannel.name:
    return ID.name


def textChannelID(Name: discord.TextChannel) -> discord.TextChannel.id:
    return Name.id


def textChannel():
    pass


def getCurrentTextChannel(ctx: commands.Context.channel) -> commands.Context:
    return ctx


def getVcChannel(ID: discord.VoiceChannel):
    return ID
