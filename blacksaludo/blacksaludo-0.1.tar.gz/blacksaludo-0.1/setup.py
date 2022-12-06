from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='blacksaludo',
    packages=['blacksaludo'],  # this must be the same as the name above
    version='0.1',
    description='Esta es la descripcion de mi paquete',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='BlackByteD',
    author_email='',
    # use the URL to the github repo
    url='https://github.com/BlackByted/BlackS',
    download_url='https://github.com/BlackByted/BlackS/tarball/0.1',
    keywords=['testing', 'logging', 'example'],
    classifiers=[ ],
    license='MIT',
)