from setuptools import setup


with open("readme.md", 'r') as f:
    readme = f.read()
setup(
    name="PyDInjector",
    version="1.0.1",
    license="MIT License",
    author="Ivan Muniz Rosa",
    long_description=readme, 
    author_email="ivanmrosa@gmail.com",
    keywords=["dependency injection", "DI", "inversion of control", "IOC", "container", "Dependency Injection", "Inversion of Control", "Python"],
    description=u"Simple dependency injection container for python",
    packages=["PyDInjector"],
    url="https://github.com/ivanmrosa/PYDInjector",
    long_description_content_type="text/markdown"
)