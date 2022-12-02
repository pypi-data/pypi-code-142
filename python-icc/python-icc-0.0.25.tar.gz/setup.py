from setuptools import setup

README = """
Home automation data models, packaged to prevent code duplication throughout microservices.
"""

setup(name='python-icc',
      version='0.0.25',
      long_description_content_type="text/markdown",
      long_description=README,
      description='IoT Control Center home automation project packages',
      url='https://github.com/patterson-project/icc-models',
      author='Patterson Project',
      author_email='patterson.n.adrian@gmail.com',
      license='MIT',
      packages=['icc'],
      zip_safe=False)
