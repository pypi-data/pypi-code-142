from random import randrange
from importlib import resources
from discord import File, Embed

def file():
	"""
	Ouputs a `discord.File` of a seal.
	## Returns
	### `discord.File`
	"""
	try:
		try:
			sealrand = f"{randrange(1, 82)}"
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
				return File(fp=f.name, filename=f"{sealrand}.png")
			finally:
				f.close()

def embed(embed: Embed):
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
			sealrand = str({randrange(1, 83)})
		finally:
			try:
				if sealrand == "7":
					sealrand = "83"
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