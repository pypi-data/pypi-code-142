from setuptools import setup

setup(
    name='tiktokget',
    version='1.0.2',
    author='github.com/charmparticle',
    scripts=['bin/tiktokget'],
    url='https://github.com/charmparticle/tiktokget',
    license='BSD 3-Clause License',
    description='A tiktok getter.',
    long_description=open('README.md').read(),
    install_requires=[
        "yt-dlp",
        "requests",
        "selenium"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

