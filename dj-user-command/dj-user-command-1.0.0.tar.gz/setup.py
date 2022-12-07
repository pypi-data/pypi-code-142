from setuptools import setup

setup(
    name='dj-user-command',
    version='1.0.0',
    packages=['dj-user-command'],
    include_package_data=True,
    install_requires=[
        'django>=3.0',
    ],
    # entry_points={
    #     'console_scripts': [
    #         # 'dj-user-command = dj-user-command.manage:main',
    #     ],
    # },
)

