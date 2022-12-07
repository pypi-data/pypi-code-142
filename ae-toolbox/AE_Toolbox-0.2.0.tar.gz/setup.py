import setuptools


setuptools.setup(
    name="AE_Toolbox",
    version="0.2.0",
    author="test",
    author_email="1429030919@qq.com",
    description="A toolbox for adversarial examples",
    py_modules=["AE_Toolbox.common"],
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    # 自动找到项目中导入的模块
    packages=setuptools.find_packages(),
    # 依赖模块
    install_requires=['foolbox==3.3.3',
                      'matplotlib==3.1.2',
                      'torch==1.13.0',
                      'torchvision==0.14.0'],
    python_requires=">=3.8"
)