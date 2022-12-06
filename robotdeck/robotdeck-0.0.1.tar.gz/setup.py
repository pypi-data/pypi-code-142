#pylint: disable=invalid-name
#pylint: disable=missing-module-docstring
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RobotDeck",
    version="0.0.1.8",
    author="Ant Solutions SRL",
    author_email="info@ant-solutions.be",
    description="RobotDeck",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://perdu.com",
    packages=["RobotDeck"],
    package_dir={"RobotDeck": "RobotDeck"},
    package_data={"RobotDeck":[
            "Interface/*",
            "Interface/Components/*",
            "Interface/Scripts/*",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pillow',
        "pyside6",
        "pyautogui",
        "opencv-python",
        "pyperclip",
        "robotframework",
    ],
    scripts=[
        "scripts/robotdeck"
    ],
    python_requires='>=3.6',
)
