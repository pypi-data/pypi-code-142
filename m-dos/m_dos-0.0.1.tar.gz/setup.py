from setuptools import setup

setup(
    name="m_dos",
    version='0.0.1',
    description="France energy prediction",
    url="https://github.com/otmaneelallaki/HAX712X-DOS",
    author="DOS",
    author_email="otmane.allai1@gmail.com",
    license="MIT",
    packages=['enr_fra','enr_fra.Prediction.classMod','enr_fra.Prediction.collectData','enr_fra.Prediction.Ld_pred'],
    zip_safe=False,
)