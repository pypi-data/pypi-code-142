import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kili_object_storage",
    version="0.0.1",
    author="Ken.Hu",
    author_email="ken.hu@kilimall.com",
    description="A object storage package for kilimall lite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "boto3==1.23.10",
        "esdk-obs-python==3.22.2",
        "opencv-python==4.6.0.66"
    ]
)
