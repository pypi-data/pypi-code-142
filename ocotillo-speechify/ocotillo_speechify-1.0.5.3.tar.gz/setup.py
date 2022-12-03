import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ocotillo_speechify",
    packages=["ocotillo"],
    version="1.0.5.3",
    author="Tyler",
    author_email="tyler@speechify.com",
    description="A fork of a simple & fast speech transcription toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/speechifyInc/ocotillo_speechify",
    project_urls={},
    install_requires=[
        'tqdm',
        'scipy',
        'torch>=1.8',
        'torchaudio>0.9',
        'audio2numpy',
        'transformers',
        'tokenizers',
        'requests',
        'ffmpeg',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)