"""Python setup.py for gettyt package"""
import io
import os
from setuptools import find_packages, setup

setup(
    name="gettyt",
    version='0.1.0',
    description="getty download tool",
    url="https://github.com/klaufir216/gettyt/",
    author="klaufir216",
    packages=find_packages(),
    install_requires=['requests', 'PIL']
)
