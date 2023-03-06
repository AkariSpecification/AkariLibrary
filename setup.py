# AkariLib - AkariSpecification's Python Lib
# Author: Takahashi Akari <akaritakahashioss@gmail.com>
# License: MIT License Copyright (c) 2023 Takahashi Akari <akaritakahashioss@gmail.com>
# Version: 0.0.1
# Date: 2023-03-06
# Python: 3.10.9
# Description: prime-faster - Faster Prime Number Generator

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="akarilib",
    version="0.0.1",
    author="Takahashi Akari",
    author_email="akaritakahashioss@gmail.com",
    description="AkariLib - AkariSpecification's Python Lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takahashi-akari/AkariLib",
    install_requires=["fabric"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)