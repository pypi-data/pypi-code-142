import discord
import json
from discord import app_commands
from discord.ext import commands
import discordsimplimised
import sys
bot = commands.Bot(command_prefix=".", intents = discord.Intents.all())

token: str = "OTk4MzU3MTY5NTQ2MjE1NTQ3.GVmv4b.7XhJ1R4wGacCmP1_2OgCQh7LkfcfY8T7rd7BOI"
@bot.tree.command(name='hello')
async def hello(interaction: discord.Interaction):
    await dcs.respond(interaction, say = "hello")

@bot.event
async def on_ready():
    print(f"Bot logged in")
    await dcs.tree_sync()

if len(sys.argv) > 0:
    token = sys.argv[1]
    bot.run(token)
