import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	# Here is the module name.
	name="amoeba-db",

	# version of the module
	version="0.0.1",

	# Name of Author
	author="Georgia Tech Database System Implementation",

	# your Email address
	author_email="gtcs6422@gmail.com",

	# #Small Description about module
	description="SQL Fuzzing Module",
# 
	# long_description=long_description,

	# Specifying that we are using markdown file for description
	long_description=long_description,
	long_description_content_type="text/markdown",

	# Any link to reach this module, ***if*** you have any webpage or github profile
	# url="https://github.com/username/",
	packages=setuptools.find_packages(),


	# if module has dependencies i.e. if your package rely on other package at pypi.org
	# then you must add there, in order to download every requirement of package



	#	 install_requires=[
	#	 "package1",
	# "package2",
	# ],


	license="",

	# classifiers like program is suitable for python3, just leave as it is.
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)
