from os.path import join as pjoin
from setuptools import setup, find_packages

setup(
    name="colmap",
    version="0.1.0",
    install_requires=["numpy"],
    packages=find_packages("scripts/python"),
    package_dir={"": "scripts/python"},
    python_requires=">=3.6",
)
