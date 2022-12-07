"""
The client class for the randseal package
"""

import discord, aiohttp, requests, random, io
from importlib import metadata

class Client:
	"""
	The client class for the randseal package
	"""
	def __init__(self, session: aiohttp.ClientSession=None):
		self.session = aiohttp.ClientSession(auto_decompress=False) or session

	async def asyncFile(self):
		"""
		Returns a `discord.File()` of a seal for py-cord in a non-blocking way
		"""
		try:
			try:
				sealrand = f"{random.randrange(1, 82)}"
			finally:
				if len(sealrand) == 1:
					sussy = sealrand
					sealrand = "0" + f"{sussy}"
		finally:
			async with self.session.get(f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg") as r:
				hi = io.BytesIO(await r.read())
				return discord.File(fp=hi, filename=sealrand + ".jpg")


	def File(self):
		"""
		Returns a `discord.File()` of a seal for py-cord in a potentially blocking way
		"""
		try:
			try:
				sealrand = f"{random.randrange(1, 82)}"
			finally:
				if len(sealrand) == 1:
					sussy = sealrand
					sealrand = "0" + f"{sussy}"
		finally:
			r = requests.get(f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg", stream=True)
			e=io.BytesIO(r.content)
			return discord.File(fp=e, filename=sealrand + ".jpg")



	def Embed(self, title: str = random.choice(["Here is your seal!", "Arff Arff!", ":3", "Seap!"])):
		"""
		Returns a `discord.Embed()` of a seal which can be edited or used in a message
		"""
		try:
			try:
				sealrand = f"{random.randrange(1, 82)}"
			finally:
				if len(sealrand) == 1:
						sussy = sealrand
						sealrand = "0" + f"{sussy}"
		finally:
			try:
				embeda = discord.Embed(colour=Client.blank(), title=title).set_image(url=f"https://raw.githubusercontent.com/mariohero24/randseal/fbba6657532d0b6db21c91986843a08a7ab19f26/randseal/00{sealrand}.jpg")
			finally:
				return embeda

	async def fetchrole(self, context, id: int) -> discord.Role | None:
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

	def blank(self) -> int:
		"""Returns a colour hex exacly like a `discord.Embed`."""
		return 0x2f3136

__author__ = "Guard Boi"
__email__ = "guard@cow.futbol"
__description__ = "Generates a random seal image for py-cord"
__licence__ = "MIT"
__version__ = metadata.version("randseal")

# python3 -m twine upload --repository pypi dist/*