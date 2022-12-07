from setuptools import setup

setup(
    name = 'modeldeploy-proxy-lib',
    version = '0.2.0',
    description = 'The lib for modeldeploy-proxy.',
    author = 'ever cheng',
    author_email = 'ever_cheng@asus.com',
    license = 'Apache License Version 2.0',
    packages = [
        'modeldeploy_proxy_lib',
    ],
    install_requires = [
        'Pillow',
        'Flask',
    ],
    extras_require = {
        'dev': [
            'pytest',
        ]
    },
    python_requires = '>=3.6.0',
    include_package_data = True,
    zip_safe = False
)
