from setuptools import setup


def readme():
    """
    用README当作long description
    """
    with open("README.md") as f:
        return f.read()


setup(
    name='pystopwords',
    version='0.0.1',
    author='huangchao',
    author_email='huangchao.cpp@gmail.com',
    url='https://github.com/chaoswork/pystopwords',
    description='中文停用词大全',
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords=["停用词", "stopwords", "中文", "chinese"],
    packages=['pystopwords'],
    package_data={'pystopwords': ['data/*.txt']},

    install_requires=[],
)
