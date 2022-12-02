import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "odesf",
    version = "0.0.2",
    author = "Xiaodu Hu",
    author_email= "xiaodu.hu@outlook.com",
    description = "Ordinary Differential Equations String Function generator.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = ['python', 'ode', 'string', 'function'],
    license = "MIT",
    # url = "",
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS"
    ],
    package_dir={'':'src'},
    py_modules=["odesf"],
    packages = setuptools.find_packages('src'),
)

# python setup.py sdist bdist