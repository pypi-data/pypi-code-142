import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jiale",                     
    version="0.1.0",                      
    author="Jia Le",                  
    description="Jia Le's Python Library",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                     
    python_requires='>=3.6',                
    py_modules=["jiale"],            
    package_dir={'':'src/jiale'},   
    install_requires=[]                     
)