import discord
from discord.ext import commands


def getTextChannel(ID: discord.TextChannel) -> discord.TextChannel:
    return ID


def textChannelName(ID: discord.TextChannel) -> discord.TextChannel:
    return ID.name


def textChannelID(Name: discord.TextChannel) -> discord.TextChannel.id:
    return Name.id


def getCurrentTextChannel(ctx) -> discord.TextChannel:
    return ctx.message.channel


# Is useless returning the ID of the voice channel by passing it by a parameter
# So I think that we can return the voice channel ID by passing his name
def getVoiceChannelID(name: discord.VoiceChannel) -> discord.VoiceChannel.id:
    return name.id


def getVoiceChannelName(id: discord.VoiceChannel) -> discord.VoiceChannel.name:
    return id.name


# The number of seconds a member must wait between sending messages
def getDelay(ID: discord.TextChannel) -> discord.TextChannel.id:
    return ID.slowmode_delay


# This method returns a boolean value, to check if a channel is NSFW (Not Safe For Work) or not
def getNSFW(ID: discord.TextChannel):
    return ID.nsfw


# Setter Method, This method can consent the programmer to set the nsfw flag to
# TRUE if he wants to make NSFW his text channel or FALSE if the channel passed by his ID is not NSFW
def setNSFW(ID: discord.TextChannel, value: bool) -> discord.TextChannel.id:
    ID.nsfw = value


# With this method is possible to change the Text channel name
def setTextChannelName(ID: discord.TextChannel, newName) -> discord.TextChannel.name:
    ID.name = newName


def setVoiceChannelName(ID: discord.VoiceChannel, newName) -> discord.VoiceChannel.name:
    ID.name = newName