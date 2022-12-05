import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_openai",
    version="0.0.2",
    author="InariInDream",
    author_email="inariindream@163.com",
    description="A plugin for nonebot to chat",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/InariInDream/nonebot_plugin_openai",
    packages=setuptools.find_packages(),
    install_requires=["pydantic>=1.9.0",
                      "Pillow>=9.0.0",
                      "nonebot-plugin-PicMenu>=0.1.5"
                      "nonebot-plugin-apscheduler>=0.1.3",
                      'nonebot-adapter-onebot>=2.0.0-beta.1',
                      'nonebot2>=2.0.0-beta.4'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", ]

)