from setuptools import setup,find_packages
VERSION = '0.0.4'
DESCRIPTION = 'avi'
LONG_DESCRIPTION = 'A package to perform arithmetic operations'

# Setting up
setup(
    name="domain_finder_r",
    version=VERSION,
    author="Rohit",
    author_email="rk0901308@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['arithmetic', 'math', 'mathematics', 'python tutorial', 'avi upadhyay'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)