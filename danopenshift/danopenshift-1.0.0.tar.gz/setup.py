from setuptools import setup, find_packages


setup(
    name='danopenshift',
    version='1.0.0',
    license='MIT',
    author="Dan",
    author_email='tuyentd@yandex.com',
    packages=find_packages(include='openshift.*'),
    url='https://github.com/dansolo1304/openshift-restclient-python',
    keywords='Openshift',
    install_requires=[
        'jinja2',
        'kubernetes',
        'python-string-utils',
        'ruamel.yaml',
        'six',
        'requests',
        'requests-oauthlib',

      ],

)