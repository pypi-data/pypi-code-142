from setuptools import setup, find_packages

with open("C:/Users/kayef.ahamad/PycharmProjects/timescaleutils/READMEFILE.md", "r") as fh:
    long_description = fh.read()
setup(
    name='timescaleutils',
    version='0.2.0',
    description='Utility for TimescaleDB',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Knowledge Lens',
    author_email='kayef.ahamad@knowledgelens.com',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=['pytz', 'sqlalchemy', 'setuptools'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
