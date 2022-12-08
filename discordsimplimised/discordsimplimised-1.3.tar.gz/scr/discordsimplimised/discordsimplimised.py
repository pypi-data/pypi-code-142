#This is dcs by Sheep26

import discord
from discord import app_commands
from discord.ext import commands
import os
bot = commands.Bot(command_prefix=".", intents = discord.Intents.all())

async def respond(interaction: discord.Interaction, say: str):
    await interaction.response.send_message(say)

async def tree_sync():
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands')
    except Exception as e:
        print(e)

def example(token):
    os.system("example.py " + token)