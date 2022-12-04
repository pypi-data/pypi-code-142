import discord, random
from importlib import resources
from .utils import blank

def File():
	"""
	Returns a `discord.File()` of a seal for py-cord
	"""
	try:
		try:
			sealrand = f"{random.randrange(1, 82)}"
		finally:
			if len(sealrand) == 1:
				sussy = sealrand
				sealrand = "0" + f"{sussy}"
	finally:
		with resources.open_text('randseal', f'00{sealrand}.jpg') as f:
			return discord.File(fp=f.name, filename=f"{sealrand}.png")

def Embed(title: str = random.choice(["Here is your seal!", "Arff Arff!", ":3", "Seap!"])):
	"""
	Returns a `discord.Embed()` of a seal
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
			embeda = discord.Embed(colour=blank(), title=title).set_image(url=f"https://raw.githubusercontent.com/mariohero24/randseal/main/randseal/00{sealrand}.jpg")
		finally:
			return embeda

# python3 -m twine upload --repository pypi dist/*