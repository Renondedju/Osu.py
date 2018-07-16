import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name     = "osu.py",
    version  = "0.4.2",
    author   = "Renondedju",
    description = ("A basic wrapper for the Osu API."),
    license = "MIT",
    url = "https://github.com/Renondedju/Osu.py",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Stable",
        "Programming Language :: Python :: 3.6",
    ],
)