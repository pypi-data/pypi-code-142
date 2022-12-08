import setuptools
with open(r'E:\tuzikmediatools\tuzikmediatools\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='tuzikmediatools',
	version='1.0.0',
	author='rimmirk',
	author_email='xktrimall@gmail.com',
	description='',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/TuzikMedia/tuzikmediatools',
	packages=['tuzikmediatools'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)