import discord, random
from importlib import resources
from .utils import blank

def file():
	"""
	Ouputs a `discord.File` of a seal.
	## Returns
	### `discord.File`
	"""
	try:
		try:
			sealrand = f"{random.randrange(1, 82)}"
		finally:
			if len(sealrand) == 1:
				try:
					sussy = sealrand
				finally:
					sealrand = "0" + f"{sussy}"
	finally:
		try:
			f = resources.open_text('randseal', f'00{sealrand}.jpg')
		finally:
			try:
				return discord.File(fp=f.name, filename=f"{sealrand}.png")
			finally:
				f.close()

def embed(embed: discord.Embed):
	"""
	Ouputs a modifed `discord.Embed`
	## Parameters
	### embed
	A `discord.Embed` that will be modified by the function, setting the image to a seal.
	## Returns
	#### `discord.Embed`
	"""
	try:
		try:
			sealrand = f"{random.randrange(1, 82)}"
		finally:
			if len(sealrand) == 1:
				try:
					sussy = sealrand
				finally:
					sealrand = "0" + f"{sussy}"
	finally:
		try:
			embeda = embed
		finally:
			try:
				embeda.set_image(url=f"https://raw.githubusercontent.com/mariohero24/randseal/main/randseal/00{sealrand}.jpg")
			finally:
				return embeda

# python3 -m twine upload --repository pypi dist/*