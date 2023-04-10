import os
from setuptools import setup, find_packages


def get_requires():
    this_dir = os.path.dirname(__file__)
    req_path = os.path.join(this_dir, "requirements.txt")
    return [line.rstrip("\n") for line in open(req_path, encoding="utf-16")]


setup(
    name="fuckvkeypad",
    version="0.1.0",
    description="Bypassing vKeyboard using OpenCV",
    author="Soul Lee",
    url="https://github.com/soulee-dev/fuckvkeypad",
    packages=find_packages(),
    install_requires=get_requires(),
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points={"console_scripts": ["vkeypad-studio = fuckvkeypad.studio:main"]},
)
