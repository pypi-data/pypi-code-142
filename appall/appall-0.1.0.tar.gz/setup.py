from setuptools import setup


with open('README.md', 'r') as description_file:
    long_description = description_file.read()


setup(
    name='appall',
    version='0.1.0',
    description='Project for horizontally juxtapozing text in terminal',
    url='https://github.com/zeionara/appall',
    author='Zeio Nara',
    author_email='zeionara@gmail.com',
    packages=[
        'appall',
    ],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
    long_description = long_description,
    long_description_content_type = 'text/markdown'
)
