import setuptools

setuptools.setup(
    name="lison_technology",
    version="0.0.3",  # 版本
    author="HuiBuBu",  # 开发人员
    author_email="huibubu2022@163.com",  # 开发人员邮箱
    description="Welcome to lison_technology",  # 一句话简介
    maintainer='HuiBuBu',  # 维护者
    maintainer_email='huibubu2022@163.com',  # 维护者邮箱
    install_requires=['time','os'],  # 依赖包
    # long_description=open('README.md', encoding='utf-8').read(),  # 读取方法介绍文件
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # 编写时的应用
    python_requires='>=3.0',  # Python的版本
)