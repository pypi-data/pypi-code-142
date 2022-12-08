
from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'Meu pacotezinho python aaaa \
      hmmmm que pacote interessante'
  
setup(
        name ='meu_pacote_aa',
        version ='1.8.0',
        author ='Rafael Nobre',
        author_email ='rafaelmedeirosnobre2001@gmail.com',
        description ='Um simples pacote python hmmmm',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'meu_pacote_aa = meu_pacote_aa.main:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='meu_pacote_aa',
        install_requires = requirements,
        zip_safe = False
)