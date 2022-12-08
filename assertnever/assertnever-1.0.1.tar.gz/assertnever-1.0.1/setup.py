from setuptools import Extension, setup

with open("./README.md") as f:
    long_desc: str = f.read()

if __name__ == "__main__":
    setup(
        name="assertnever",
        description="Syntactical sugar for assert never.",
        readme="README.md",
        author="ZeroIntensity",

        version="1.0.1",
        license="MIT",
        project_urls={
            "Source": "https://github.com/ZeroIntensity/assertnever",
        },
        ext_modules=[Extension("an", ["an.c"])],
        package_data={'an': ['py.typed', '*.pyi']},
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: Implementation :: CPython",
        ],
        keywords=["assert", "never"],
        long_description_content_type="text/markdown",
        long_description=long_desc,
    )