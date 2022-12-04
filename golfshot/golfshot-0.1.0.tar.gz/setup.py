from setuptools import setup

setup(
    name='golfshot',
    version='0.1.0',
    packages=['golfshot'],
    license='MIT',
    author='Andrew Van Gerpen',
    author_email='andrew.vangerpen@gmail.com',
    description='2D simulation of a golf ball using basic concepts from kinematics and aerodynamics',
    install_requires=[
        'numpy',
        'plotly',
        'pandas'
    ]
)