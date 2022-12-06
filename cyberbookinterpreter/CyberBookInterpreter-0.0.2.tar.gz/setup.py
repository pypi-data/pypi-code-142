from setuptools import setup

# python setup.py sdist
# twine upload dist/*

setup(name='CyberBookInterpreter',
      version='0.0.2',
      description='Utilizes CyberBook as a CLI utility.',
      url='https://github.com/ClutchTech/CyberBookInterpreter',
      keywords='cyberbook encoders tools cli',
      author='Clutch_Reboot',
      author_email='clutchshadow26@gmail.com',
      license='GNU General Public License v3.0',
      packages=[
            'CyberBookInterpreter'
      ],
      zip_safe=False,
      long_description=open('README.md', 'rt').read(),
      long_description_content_type='text/markdown',
      python_requires='>=3.10',
      install_requires=['CyberBook'],
      )
