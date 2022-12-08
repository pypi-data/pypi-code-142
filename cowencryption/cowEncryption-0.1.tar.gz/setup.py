from distutils.core import setup, Extension

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name = "cowEncryption",
	packages = ["cowEncryption"], 
	package_dir = {"cowEncryption": "src/cowEncryption"},
	version = "0.1",
	license ="MIT",
	description = "This library is used for Encryption your code",
	long_description = long_description,
	long_description_content_type = "text/markdown", 
	author = "Muhammad Latif Harkat",
	author_email = "latipharkat176@gmail.com",
	url = "https://github.com/Latip176/cowEncryption",
	download_url = "https://github.com/Latip176/cowEncryption/archive/cowEncryption.tar.gz", 
	keywords = [
		"cowEncryption", 
		"Cow Encryption", 
		"Python Encryption", 
		"Latip176", 
		"Encryption",
        "Muhammad Latif Harkat"
	], 
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Build Tools",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
	],
)