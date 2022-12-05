from setuptools import setup, find_packages

setup(
    name="repo_ranger",
    version="0.1.0",
    packages=find_packages(),
    author="Panagiotis Nezis",
    author_email="your.email@example.com",
    description="A command-line tool for managing a set of Git repositories",
    install_requires=["PyYAML", "termcolors"],
    entry_points={"console_scripts": ["repo_ranger = repo_ranger:main"]},
    data_files=[("man/man1", ["man/man1/repo_ranger.1"])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
