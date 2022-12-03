#!/usr/bin/env python
import setuptools
from assistant import __version__

catchphrase = "Your very own Assistant. Because you deserve it."
fail_catchphrase = "Where am I? Hey! It's me Assistant."

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = fail_catchphrase

version = __version__

required_packages = [
        #'rasa~=3.2.10',
        #'rasa-sdk~=3.2.2',
        'dmt>=1.5.1',
        'ftfy',
        'pydub',
        'pygments',
        'xonsh',
        'attrs',
        'questionary',
#        'nest-asyncio',
        'transformers',
        'sentencepiece',
    ]

setuptools.setup(
    name='assistant',
    version=version,
    license='MIT',
    author='Danny Waser',
    author_email='danny@waser.tech',
    description=catchphrase,
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.8,<3.11',
    install_requires=required_packages,
    packages=['assistant', 'assistant.ptk_shell', 'assistant.rasa', 'assistant.manager', 'assistant.predictor', 'assistant.responder', 'assistant.api', 'assistant.say', 'assistant.listen', 'assistant.entry_points', 'xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    entry_points={
        'console_scripts': [
            'assistant = assistant.entry_points.run_assistant:run',
            'manager = assistant.manager.__main__:run'
        ]
    },
    url='https://gitlab.com/waser-technologies/technologies/assistant',
    project_urls={
        "Documentation": "https://gitlab.com/waser-technologies/technologies/assistant/blob/master/README.md",
        "Code": "https://gitlab.com/waser-technologies/technologies/assistant",
        "Issue tracker": "https://gitlab.com/waser-technologies/technologies/assistant/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Natural Language :: French",
        "Topic :: System :: Shells",
        "Programming Language :: Unix Shell",
        "Topic :: Terminals",
    ]
)
