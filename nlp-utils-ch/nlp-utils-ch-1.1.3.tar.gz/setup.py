from setuptools import setup, find_packages

setup(
    name="nlp-utils-ch",
    version="1.1.3",
    description="nlp基础工具",
    author="peng.su",
    packages=find_packages(),
    # include_package_data=True,
    package_data={
                '':[
                    'zhconv/zhcdict.json',
                    'resources/*.txt'
                    ],
               
    			},
    install_requires=[
        'ahocorasick'
      ],
    author_email="alweeq5@163.com",
)
