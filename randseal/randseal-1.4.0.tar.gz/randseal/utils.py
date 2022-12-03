import discord

async def fetchrole(context, id: int):
	"""
	Returns a `discord.Role` from ID, regardless of the state of your bot's internal cache.
	# Parameters
	`context`: Can be any object with the `discord.Guild` object in it. 
	`id`: The ID of the role you want to get
	### Context Examples:
	`discord.Message` (if message is in a guild), `discord.Member`, `discord.ApplicationContext`, `discord.ext.commands.Context`.
	"""
	roles = await context.guild.fetch_roles()
	role = discord.utils.get(roles, id=id)
	return role

def blank() -> int:
	"""Returns a colour hex exacly like a `discord.Embed`."""
	return 0x2f3136
