# -*- coding: utf-8 -*-
import os
import re

from setuptools import find_packages, setup

NAME = "jupyter-notebook-tools"

with open("README.md", "r") as f:
    readme = f.read()

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name=NAME,
    version=find_version("nbstripout", "__init__.py"),
    url=f"https://github.com/akuhnregnier/{NAME}",
    author="Alexander Kuhn-Regnier",
    author_email="ahf.kuhnregnier@gmail.com",
    long_description=readme,
    packages=find_packages(),
    entry_points={
        "console_scripts": ["nbstripout-fast=nbstripout.nbstripout_fast:main"]
    },
    python_requires=">=3.6",
    install_requires=(),
)
