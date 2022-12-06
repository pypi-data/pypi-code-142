from setuptools import setup, find_packages
import codecs, sys


try:
    with codecs.open( "README.md", 'r', errors='ignore' ) as file:
        readme_contents = file.read()

except Exception as error:
    readme_contents = ""
    sys.stderr.write( "Warning: Could not open README.md due %s\n" % error )

classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'Intended Audience :: Education'
]

setup(
    name="apiComs",
    version="1.0.3",
    description="This is a package to stremaline api method calls",
    long_description = readme_contents,
    long_description_content_type='text/markdown',
    url="https://github.com/demecode/winter-api-commons",
    author="Deme Xavier",
    author_email="clabsvc@gmail.com",
    license="MIT",
    classifiers=classifiers,
    keywords=["api automation", "api testing", "api commons", "python api", "api automation using python" "common repo"],
    packages=find_packages(),
    install_requires=[
        "jsonschema==4.4.0",
        "requests==2.27.1"
        ]
)