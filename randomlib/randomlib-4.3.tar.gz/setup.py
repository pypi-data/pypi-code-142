from setuptools import setup

setup(
    name='randomlib',
    version='4.3',
    # author='L3Cube',
    # author_email='l3cube.pune@gmail.com',
    # description='An NLP Library for Marathi Language',
    # url='https://github.com/l3cube-pune/MarathiNLP.git',
    packages=['randomlib','randomlib.autocomplete', 'randomlib.datasets', 'randomlib.hate', 'randomlib.maskFill', 'randomlib.modelRepo', 'randomlib.preprocess', 'randomlib.sentiment', 'randomlib.similarity', 'randomlib.tagger', 'randomlib.tokenizer'],# can also use setuptools.find_packages()
    include_package_data=True,
    install_requires=['importlib_resources','huggingface_hub==0.11.1','tqdm','pandas','sentence_transformers','transformers','numpy','torch','IPython'], #'openpyxl'
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
