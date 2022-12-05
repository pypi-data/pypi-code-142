import setuptools

setuptools.setup(
    # 项目的名称
    name="classes_tools",
    # 项目的版本
    version="0.1.0",
    # 项目的作者
    author="XCreeperPa",
    # 作者的邮箱
    author_email="499574564@qq.com",
    # 项目描述
    description="一些关于Python类的工具。",
    # 项目的长描述
    long_description="一些关于Python类的工具。",
    # 以哪种文本格式显示长描述
    long_description_content_type="text/markdown",
    # 所需要的依赖
    install_requires=[],
    # 项目主页
    url="https://gitee.com/xcpcn/classes_tools",
    # 项目中包含的子包，find_packages() 是自动发现根目录中的所有的子包。
    packages=setuptools.find_packages(),
    # 其他信息，这里写了使用 Python3，MIT License许可证，不依赖操作系统。
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
