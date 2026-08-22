#!/usr/bin/env python
# coding: utf8

import os
import re
from codecs import open
from setuptools import find_packages, setup

# Absoluten Pfad des Ordners ermitteln, in dem diese setup.py liegt
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def read_file(*parts):
    filepath = os.path.join(BASE_DIR, *parts)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


# Version dynamisch aus geocoder/__init__.py auslesen
init_content = read_file("geocoder", "__init__.py")
version_match = re.search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', init_content, re.MULTILINE
)

if not version_match:
    raise RuntimeError("Cannot find version information")

version = version_match.group(1)

# README einlesen (falls vorhanden)
try:
    readme = read_file("README.md")
except FileNotFoundError:
    readme = "Geocoder is a simple and consistent geocoding library."

requires = ["requests", "ratelim", "click", "six", "future"]

setup(
    name="geocoder",
    version=version,
    description="Geocoder is a simple and consistent geocoding library.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Denis Carriere",
    author_email="carriere.denis@gmail.com",
    url="https://github.com/DenisCarriere/geocoder",
    license="The MIT License",
    entry_points="""
        [console_scripts]
        geocode=geocoder.cli:cli
    """,
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)