from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()


REQUIREMENTS = ["djangorestframework"]

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]

setup(name='djangojr',
      version='1.0.5',
      description='Django app to json rest api provide api views, serializer, rate limit, pagination, authentication, permission,lazy response,blacklist etc.',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      author='Esref Yigitbasi',
      author_email='esrefyigitbasi.dev@gmail.com',
      url="https://github.com/esrefyigitbasi-dev/django_json_rest",
      license='MIT',
      packages=["djangojr", "djangojr.ratelimit", "djangojr.token",
                "djangojr.ratelimit.migrations", "djangojr.token.migrations"],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='django restframework djangojr json parse response request api wrapper lazyresponse ratelimit pagination permissions token authentication'
      )
