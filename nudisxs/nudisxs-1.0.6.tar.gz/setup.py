from skbuild import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="nudisxs",
    version="1.0.6",
    author = "Vadim A.Naumov and K.Kuzmin",
    maintainer = "Dmitry V.Naumov",
    maintainer_email = "dmitryvnaumov@gmail.com",
    description="A python interface to fortran code developed by Vadim A.Naumov and Konstantin Kuzmin, calculating neutrino-nucleon deep inelastic charged/neutral current cross-sections.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license="MIT",
    classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy"],
    url = "https://git.jinr.ru/dnaumov/nudisxs",
    packages=['nudisxs','nudisxs/tests'],
    cmake_args=['-DSKBUILD=ON']
)
