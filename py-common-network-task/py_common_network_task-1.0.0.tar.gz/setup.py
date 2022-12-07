from setuptools import setup

setup(name='py_common_network_task',
      version='1.0.0',
      description='Network Task packages',
      author='Mor Dvash',
      author_email='mordvash1@gmail.com',
      packages=['py_common',
                'py_common.message_queue'],
      python_requires='>=3.8',
      install_requires=[
          # minimum requirement safety - can be commented out after all services are aligned
          'kafka-python==2.0.2',
      ],
      zip_safe=False)
