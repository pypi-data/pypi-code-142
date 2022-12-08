from setuptools import setup, find_packages

setup(
    name="newsrec",
    version="0.0.1",
    license="MIT",
    author="Johannes Kruse",
    author_email="johannes-kruse@hotmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="",
    keywords="Recommender Systems",
    install_requires=["numpy", "spicy", "pytest"],
)
