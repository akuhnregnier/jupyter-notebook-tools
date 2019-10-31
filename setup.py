from nbstripout import NAME, VERSION
from setuptools import find_packages, setup

setup(
    name=NAME,
    version=VERSION,
    url=f"https://github.com/akuhnregnier/{NAME}",
    author="Alexander Kuhn-Regnier",
    author_email="ahf.kuhnregnier@gmail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["nbstripout-fast=nbstripout.nbstripout_fast:main"]
    },
    python_requires=">=3.6",
    install_requires=(),
)
