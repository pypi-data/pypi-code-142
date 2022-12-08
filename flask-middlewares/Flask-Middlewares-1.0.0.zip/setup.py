from setuptools import setup, find_packages


BEAUTIFUL_PACKAGE_NAME = 'Flask-Middlewares'
PACKAGE_NAME = 'flask_middlewares'

VERSION = '1.0.0'

REQUIRES = ['beautiful_repr==1.1.1', 'Flask==2.2.2', 'flask_sqlalchemy==3.0.2']


with open('README.md') as readme_file:
    LONG_DESCRIPTION = readme_file.read()


setup(
    name=BEAUTIFUL_PACKAGE_NAME,
    version=VERSION,
    license_files = ('LICENSE',),
    description="Middlware library for your Flask application",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/TheArtur128/Flask-middlewares',
    download_url=f'https://github.com/TheArtur128/Flask-middlewares/archive/refs/tags/v{VERSION}.zip',
    author='Arthur',
    author_email='s9339307190@gmail.com',
    install_requires=REQUIRES,
    python_requires='>=3.11',
    packages={
        PACKAGE_NAME: PACKAGE_NAME,
        f'{PACKAGE_NAME}.standard': f'{PACKAGE_NAME}/standard'
    }
)