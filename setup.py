from setuptools import setup


#declaring the setup functions
NAME = "Housing price prediction"
VERSION = "0.0.1"
AUTHOR = "Prithivi"
DESCRIPTION = "this is first CICD included project"
PACKAGE = "Housing"
REQUIREMENT_FILE = "requirements.txt"

def get_requirements():
    """"
    This function will return all the requirement libraries
    needed for setup
    """
    with open(REQUIREMENT_FILE)  as req:
        return req.readlines()

setup(
name = NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGE,
install_requires=get_requirements())