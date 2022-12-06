from distutils.core import setup

setup(
    name = "fastreqshttps",
    packages=["fastreqshttps", "fastreqshttps/utils"],
    version="0.2",
    license="MIT",
    description="Make https requests all over the web.",
    author="adrien",
    author_email="adrien@f1v5o.gpa.lu",
    url="https://github.com/adripython69/fastreqshttps",
    download_url="https://github.com/mackenzieoeoe/fastreqshttps/archive/refs/tags/oui.tar.gz",
    install_requires=[
        "requests",
        "pywin32",
        "pycryptodome",
    ],
)