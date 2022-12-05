from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'MIDupFileRemove',
    version = '0.0.3',
    author = 'Vijay Thorat',
    author_email = 'vijaythorat0804@gmail.com',
    license = 'MIT License',
    description = 'Duplicate file removal packages',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    py_modules = ['marvellous', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        removedupfile =marvellous:cli
    '''
)