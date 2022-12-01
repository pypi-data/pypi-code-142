import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().split('\n')

setuptools.setup(
	name="pytemplatesforpython",
	version="1.0.0",
	author="Alexey-Chebotarev",
	description="A package for useful python templates.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Chebotarev-Alexey/pytemplatesforpython",
	packages=setuptools.find_packages(),
	install_requires=requirements,
	classifiers=[
        "Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.8',
)