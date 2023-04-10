import os
from setuptools import setup, find_packages


def get_requires():
    this_dir = os.path.dirname(__file__)
    req_path = os.path.join(this_dir, "requirements.txt")
    return [line.rstrip("\n") for line in open(req_path)]


setup(
    name="fuckvkeypad",
    version="0.2.0",
    description="Bypassing vKeyboard using OpenCV",
    author="Soul Lee",
    url="https://github.com/soulee-dev/fuckvkeypad",
    packages=find_packages(),
    install_requires=get_requires(),
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    platforms="OS Independent",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points={"console_scripts": ["vkeypad-studio = fuckvkeypad.studio:main"]},
)
