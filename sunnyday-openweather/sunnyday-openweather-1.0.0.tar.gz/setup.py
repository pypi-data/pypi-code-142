from setuptools import setup

setup(
    name = 'sunnyday-openweather',
    packages = ['sunnyday'],
    version = '1.0.0',
    license = 'MIT',
    description = 'Weather forecast data',
    author = 'Kasia Zysko',
    keywords = ['weather', 'forecast', 'openweather'],
    initiall_requires = ['requests'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools"
    ],

)