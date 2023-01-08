import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "bingX-connector"
VERSION = "0.0.5"
AUTHOR = "Ming119"
URL = "https://github.com/Ming119/bingX-connector-python"

setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    url=URL,
    description="A simple connector to BingX Public API",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(exclude=["test", "docs"]),
    package_data={
        "perpetual": ["*", "*/*"],
    },

    license='GPLv3',

    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
)