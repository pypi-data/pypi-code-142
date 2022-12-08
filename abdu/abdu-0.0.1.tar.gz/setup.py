from setuptools import setup
#from ihao import __version__ as current_version

setup(
    name="abdu",
    version='0.0.1',
    description="France energy prediction",
    url="https://github.com/otmaneelallaki/HAX712X-DOS",
    author="DOS",
    author_email="otmane.allai1@gmail.com",
    license="MIT",
    packages=['abdu','abdu.Prediction','abdu.dataCollect','abdu.ot'],
    zip_safe=False,
)