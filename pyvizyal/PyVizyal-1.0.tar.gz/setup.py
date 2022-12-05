import setuptools
with open(r'C:\Users\1\Desktop\README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='PyVizyal',
	version='1.0',
	author='SGG',
	author_email='dtumanov446@gmail.com',
	description='PyVizyal создаётся виртуальное окружуние',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=['PyVizyal'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)