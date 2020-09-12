import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="realnet-item",
    version="0.0.1",
    description="Realnet item",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/virtual-space/realnet-item",
    author="Marko Laban",
    author_email="marko.laban@l33tsystems.com",
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["realnet_server"],
    include_package_data=True,
    install_requires=["pynecone==0.0.18"],
    entry_points={
        "console_scripts": [
            "realnet-item=realnet_item.__main__:main",
        ]
    },
)
